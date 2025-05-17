import os
import customtkinter as ctk
from PIL import Image, ImageTk
from retransmite import alternar_streaming, detener_streaming, is_streaming_activo, set_audio_config, FORMAT, CHANNELS

#                                       °°°°°°°°°°°°° Dependencias °°°°°°°°°°°°°
#                                 pip install customtkinter Pillow pyaudio numpy scipy

# Establecer el tema de color predeterminado
ctk.set_appearance_mode("Dark")

# Función para cerrar la ventana cuando se activa el protocolo de cierre
def cerrar_ventana():
    if is_streaming_activo():
        detener_streaming()
    ventana.quit()
    ventana.destroy()

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("PROTOTIPO - TOBI")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Dedicado a las imágenes

# Obtener la ruta actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa de la imagen
ruta_imagen = os.path.join(current_dir, "LogoTOBI.png")

# Cargar y redimensionar la imagen para usarla como ícono
icon_size = (64, 64)
imagen_icon = Image.open(ruta_imagen).resize(icon_size, Image.LANCZOS)
imagen_icon_tk = ImageTk.PhotoImage(imagen_icon)

# Establecer la imagen redimensionada como ícono de la ventana
ventana.iconphoto(False, imagen_icon_tk)

# Cargar y redimensionar la imagen para mostrarla en la interfaz
imagen_original = Image.open(ruta_imagen)
ancho_imagen = 365
alto_imagen = 240
imagen_tk = ImageTk.PhotoImage(imagen_original.resize((ancho_imagen, alto_imagen), Image.LANCZOS))

# Crear un Label para la imagen
imagen_label = ctk.CTkLabel(ventana, image=imagen_tk, text="")
imagen_label.place(relx=0.5125, rely=0.15, anchor='center')

# Frames que contienen todo en grids

# Crear un Frame para contener las etiquetas y entradas
frame_width = 350
frame_height = 340
frame = ctk.CTkFrame(ventana, width=frame_width, height=frame_height)
# Hace que no se ajuste al tamaño del frame
frame.grid_propagate(False)
# Centra vertical y horizontalmente en el frame
frame.place(x=(400 - frame_width) // 2, y=(650 - frame_height) // 2)
# Configurar el grid dentro del Frame para centrar los widgets
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

etiquetas = ["CALIDAD", "RADIO"]
valores_entendibles = {
    "CALIDAD": ["Muy Alta", "Alta", "Media"],
    "RADIO": ["Muy Alto", "Alto", "Medio"],
}

mapa_valores_tecnicos = {
    "CALIDAD": {"Muy Alta": "2048", "Alta": "1024", "Media": "512"},
    "RADIO": {"Muy Alto": "96000", "Alto": "48000", "Medio": "44100"},
}

# Se actualizan los valores seleccionados
valores_seleccionados = {etiqueta: valores_entendibles[etiqueta][0] for etiqueta in etiquetas}

# Añadir controles de volumen separados para cada oído
def cambiar_volumen(volumen, canal):
    if canal == 'Izquierdo':
        volumen_izquierdo.set(volumen)
        etiqueta_volumen = "Lado Izquierdo"
    elif canal == 'Derecho':
        volumen_derecho.set(volumen)
        etiqueta_volumen = "Lado Derecho"
    
    # Actualizar el valor seleccionado y el botón
    actualizar_valor_seleccionado(etiqueta_volumen, volumen)

def actualizar_valor_seleccionado(etiqueta, valor):
    # Actualizar los valores seleccionados
    valores_seleccionados[etiqueta] = valor
    
    # Obtener los valores actuales de los controles de volumen
    vol_izq = volumen_izquierdo.get()
    vol_der = volumen_derecho.get()

    # Detener el streaming y actualizar el botón
    detener_streaming()
    boton.configure(text="GUARDAR", fg_color="#C004E0")

comboboxes = {}

# Posicionamiento usando place para las etiquetas y comboboxes
y_start = 40
for i, etiqueta in enumerate(etiquetas):
    y_pos = y_start + i * 100
    
    # Label
    label = ctk.CTkLabel(frame, text=etiqueta)
    label.place(x=10, y=y_pos)
    
    # ComboBox
    combobox = ctk.CTkComboBox(frame, values=valores_entendibles[etiqueta], width=200, command=lambda value, e=etiqueta: actualizar_valor_seleccionado(e, value))
    combobox.set(valores_entendibles[etiqueta][0])
    combobox.place(x=130, y=y_pos)
    
    comboboxes[etiqueta] = combobox

# Posicionamiento usando place para las etiquetas y sliders
y_start_volumen = 240
etiqueta_volumen_izquierdo = ctk.CTkLabel(frame, text="Lado Izquierdo")
etiqueta_volumen_izquierdo.place(x=10, y=233.5)

volumen_izquierdo = ctk.CTkSlider(frame, from_=0, to=1, number_of_steps=100, command=lambda v: cambiar_volumen(v, 'Izquierdo'))
volumen_izquierdo.set(0.5)
volumen_izquierdo.place(x=130, y=y_start_volumen)

etiqueta_volumen_derecho = ctk.CTkLabel(frame, text="Lado Derecho")
etiqueta_volumen_derecho.place(x=10, y= 292.5)

volumen_derecho = ctk.CTkSlider(frame, from_=0, to=1, number_of_steps=100, command=lambda v: cambiar_volumen(v, 'Derecho'))
volumen_derecho.set(0.5)
volumen_derecho.place(x=130, y=y_start_volumen + 60)

def iniciar_streaming():
    if not is_streaming_activo():
        FORMAT
        CHUNK = int(mapa_valores_tecnicos["CALIDAD"][valores_seleccionados["CALIDAD"]])
        CHANNELS = 2
        RATE = int(mapa_valores_tecnicos["RADIO"][valores_seleccionados["RADIO"]])

        # Obtener los valores de los controles de volumen
        vol_izq = volumen_izquierdo.get()
        vol_der = volumen_derecho.get()

        set_audio_config(FORMAT, CHUNK, CHANNELS, RATE, vol_izq, vol_der)
        alternar_streaming()
        boton.configure(text="FINALIZAR", fg_color="#1D75CC")
    else:
        detener_streaming()
        boton.configure(text="INICIAR", fg_color="#1D75CC")

boton = ctk.CTkButton(ventana, text="INICIAR", fg_color="#1D75CC", command=iniciar_streaming)
boton.place(x=(400 - boton.winfo_reqwidth()) // 2, y=(750 - frame_height) // 2 + frame_height + 10)

ventana.mainloop()
