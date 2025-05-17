import pyaudio
import threading
import numpy as np
from scipy.signal import wiener

# Variables globales
streaming_activo = False
audio_interface = None
stream = None
FORMAT = pyaudio.paFloat32
CHUNK = 2048
CHANNELS = 2
RATE = 44100  # Tasa de muestreo comúnmente utilizada

volumen_izquierdo = 0.5  # Valores iniciales para el volumen
volumen_derecho = 0.5

# Lock para sincronizar el acceso a los recursos compartidos
stream_lock = threading.Lock()

# Función para aplicar reducción de ruido usando el filtro de Wiener
def reducir_ruido(data, ventana_wiener=11):
    data = np.frombuffer(data, dtype=np.float32)
    clean_data = wiener(data, mysize=ventana_wiener)
    return clean_data.astype(np.float32).tobytes()

# Función para ajustar el volumen del audio
def ajustar_volumen(data, volumen_izquierdo, volumen_derecho):
    audio_array = np.frombuffer(data, dtype=np.float32).copy()

    if CHANNELS == 2:
        audio_izquierdo = audio_array[::2]
        audio_derecho = audio_array[1::2]

        audio_izquierdo *= volumen_izquierdo
        audio_derecho *= volumen_derecho

        # Corrección de saturación
        audio_izquierdo = np.clip(audio_izquierdo, -1.0, 1.0)
        audio_derecho = np.clip(audio_derecho, -1.0, 1.0)

        audio_array[::2] = audio_izquierdo
        audio_array[1::2] = audio_derecho
    else:
        audio_array *= volumen_izquierdo
        audio_array = np.clip(audio_array, -1.0, 1.0)

    return audio_array.astype(np.float32).tobytes()



# Función para manejar el streaming de audio
def manejar_streaming():
    global stream
    try:
        while streaming_activo:
            with stream_lock:
                if stream is None:
                    raise ValueError("Stream is None")
                # Leer los datos de audio del stream
                data = stream.read(CHUNK, exception_on_overflow=False)

                # Reducir el ruido
                data = reducir_ruido(data)

                # Ajustar el volumen del audio
                data = ajustar_volumen(data, volumen_izquierdo, volumen_derecho)

                # Escribir los datos procesados en la salida
                stream.write(data, CHUNK)
    except Exception as e:
        print("* Error durante el streaming:", e)

# Función para alternar el inicio y fin del streaming
def alternar_streaming():   
    global streaming_activo, audio_interface, stream
    if not streaming_activo:
        try:
            audio_interface = pyaudio.PyAudio()
            stream = audio_interface.open(format=FORMAT,
                                          channels=CHANNELS,
                                          rate=RATE,
                                          input=True,
                                          output=True,
                                          frames_per_buffer=CHUNK // 4)

            streaming_activo = True
            threading.Thread(target=manejar_streaming, daemon=True).start()
        except Exception as e:
            print(f"Error al iniciar el streaming: {e}")
            detener_streaming()
    else:
        detener_streaming()

# Función para detener el streaming
def detener_streaming():
    global streaming_activo, audio_interface, stream
    with stream_lock:
        if streaming_activo:
            streaming_activo = False
            if stream is not None:
                stream.stop_stream()
                stream.close()
                stream = None
            if audio_interface is not None:
                audio_interface.terminate()
                audio_interface = None

# Función para verificar si el streaming está activo
def is_streaming_activo():
    global streaming_activo
    return streaming_activo

# Función para establecer la configuración de audio
def set_audio_config(format, chunk, channels, rate, vol_izq, vol_der):
    global FORMAT, CHUNK, CHANNELS, RATE, volumen_izquierdo, volumen_derecho
    print(f"Configuración de audio: FORMAT={format}, CHUNK={chunk}, CHANNELS={channels}, RATE={rate}")
    FORMAT = format
    CHUNK = chunk
    CHANNELS = channels
    RATE = rate
    volumen_izquierdo = vol_izq  # Actualiza el volumen izquierdo
    volumen_derecho = vol_der  # Actualiza el volumen derecho
