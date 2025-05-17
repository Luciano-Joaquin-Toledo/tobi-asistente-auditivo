<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>🎧 T.O.B.I. – Transmisor Operativo Básico e Inmersivo</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  :root {
    --primary-color: #1a73e8;
    --secondary-color: #f9f9f9;
    --accent-color: #ff5722;
    --text-color: #333;
    --bg-gradient: linear-gradient(135deg, #1a73e8 0%, #3f87f5 100%);
    --shadow-light: rgba(26, 115, 232, 0.25);
    --font-sans: 'Inter', sans-serif;
  }

  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    font-family: var(--font-sans);
    background: var(--secondary-color);
    color: var(--text-color);
    line-height: 1.6;
    padding: 2rem;
    scroll-behavior: smooth;
  }

  h1, h2, h3 {
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
  }

  h1 {
    font-size: 2.8rem;
    letter-spacing: 1.5px;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 2px 6px var(--shadow-light);
  }

  h2 {
    border-bottom: 3px solid var(--accent-color);
    padding-bottom: 0.3rem;
    margin-top: 2rem;
  }

  p {
    font-size: 1.1rem;
  }

  .container {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    border-radius: 12px;
    padding: 2rem 3rem;
    box-shadow: 0 8px 24px var(--shadow-light);
    animation: fadeInUp 1s ease forwards;
  }

  /* Icons & emojis style */
  .emoji {
    font-size: 1.5rem;
    margin-right: 0.5rem;
    vertical-align: middle;
  }

  /* Lists with custom bullets */
  ul {
    padding-left: 1.2rem;
  }

  ul li {
    margin-bottom: 0.5rem;
    position: relative;
    padding-left: 1.3rem;
  }

  ul li::before {
    content: '▹';
    position: absolute;
    left: 0;
    color: var(--accent-color);
  }

  /* Separator */
  hr {
    border: none;
    border-top: 2px solid var(--primary-color);
    margin: 2rem 0;
    opacity: 0.3;
  }

  /* Highlighted text */
  strong {
    color: var(--primary-color);
  }

  /* Footer note */
  .footer {
    text-align: center;
    font-style: italic;
    margin-top: 3rem;
    color: #777;
    font-size: 0.9rem;
  }

  /* Links style */
  a {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
  }
  a:hover {
    text-decoration: underline;
  }

  /* Smooth fade-in animation */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Responsive */
  @media (max-width: 600px) {
    body {
      padding: 1rem;
    }
    .container {
      padding: 1.5rem 1.5rem;
    }
    h1 {
      font-size: 2rem;
    }
  }
</style>
</head>
<body>

<div class="container" role="main" aria-label="Presentación del proyecto T.O.B.I.">
  <h1>🎧 T.O.B.I. – Transmisor Operativo Básico e Inmersivo</h1>
  <p><span class="emoji">🧪</span> Proyecto presentado en la Feria Regional de Ciencia, Educación, Arte y Tecnología 2024<br/>
  <span class="emoji">🏅</span> <strong>¡Seleccionado para la instancia provincial!</strong></p>

  <hr />

  <h2>📌 ¿Qué es T.O.B.I.?</h2>
  <p><strong>T.O.B.I.</strong> es un software diseñado para amplificar sonidos del entorno en tiempo real, ajustándose a las necesidades de personas con hipoacusia leve o moderada. Utiliza auriculares conectados a un celular o PC para captar y retransmitir el audio, sirviendo como una alternativa más simple, económica y accesible que los audífonos convencionales.</p>
  <p>🎧 <em>Se recomienda el uso de <strong>auriculares con micrófono</strong> para una experiencia óptima.</em></p>

  <h2>🎯 Objetivos</h2>
  <ul>
    <li>Brindar una herramienta simple para mejorar la audición cotidiana.</li>
    <li>Diseñar un software multiplataforma adaptable a computadoras y celulares.</li>
    <li>Fomentar el uso de soluciones tecnológicas inclusivas desde el ámbito educativo.</li>
  </ul>

  <h2>🛠 Tecnologías utilizadas</h2>
  <ul>
    <li><strong>Lenguaje:</strong> Python 3</li>
    <li><strong>Librerías:</strong>
      <ul>
        <li>pyttsx3 – Texto a voz</li>
        <li>speech_recognition – Reconocimiento de voz</li>
        <li>pyaudio – Entrada y salida de audio</li>
        <li>keyboard, os – Acceso a sistema y detección de teclas</li>
      </ul>
    </li>
  </ul>

  <h2>🔍 Materiales y Métodos</h2>
  <ul>
    <li><strong>Investigación documental:</strong> Lectura y análisis de informes de la OMS, artículos médicos y divulgativos.</li>
    <li><strong>Entrevistas y encuestas:</strong>
      <ul>
        <li>A personas con hipoacusia (ej. abuela de un integrante).</li>
        <li>A un médico otorrinolaringólogo de forma rápida y respetuosa.</li>
      </ul>
    </li>
    <li><strong>Programación:</strong> Desarrollo en Python con bibliotecas de reconocimiento y reproducción de audio. Pruebas funcionales con distintos dispositivos y usuarios.</li>
    <li><strong>Validación:</strong> Presentaciones dentro de la institución, con feedback positivo.</li>
  </ul>

  <h2>📊 Resultados</h2>
  <ul>
    <li>Se identificaron las principales causas por las que no se usan audífonos:
      <ul>
        <li>Costos elevados</li>
        <li>Dispositivos incómodos o difíciles de usar</li>
      </ul>
    </li>
    <li>El software fue probado con éxito en condiciones reales y en la institución educativa.</li>
    <li>Recepción positiva por parte de usuarios y evaluadores.</li>
    <li>Registro de avances y observaciones en agenda de trabajo.</li>
  </ul>

  <h2>✅ Conclusiones</h2>
  <ul>
    <li>El proyecto fue completado según lo planeado y superó nuestras expectativas iniciales.</li>
    <li>Confirmamos que es posible crear soluciones viables con recursos limitados y mucho compromiso.</li>
    <li>Abrimos la puerta a futuras mejoras: optimización para móviles, interfaz gráfica y personalización de perfiles auditivos.</li>
    <li>Aprendimos lo complejo pero gratificante que es llevar adelante un proyecto con impacto real.</li>
  </ul>

  <h2>📱 Próximos pasos</h2>
  <ul>
    <li>Interfaz gráfica multiplataforma (PC y móviles)</li>
    <li>Reducción de latencia y mejora en la calidad del audio</li>
    <li>Ampliación de pruebas con mayor cantidad de usuarios</li>
    <li>Validación con especialistas médicos de forma más formal</li>
  </ul>

  <h2>👨‍💻 Autores</h2>
  <p>
    - Demian Alejandro Gomez Saucedo<br/>
    - Santiago Nicolás Llamosas<br/>
    - Tobias Sotelo<br/>
    - Luciano Joaquín Toledo
  </p>
  <p>🎓 Instituto Técnico Dr. Emilio Lamarca<br/>
  📍 Lomas de Zamora, Provincia de Buenos Aires – CUE: 0614763-00<br/>
  🗓 Año cursado: 2024</p>

  <hr />

  <h2>📚 Bibliografía</h2>
  <ul>
    <li><a href="https://www.who.int/es/news-room/fact-sheets/detail/deafness-and-hearing-loss" target="_blank" rel="noopener noreferrer">OMS: Fact Sheet sobre sordera y pérdida auditiva</a></li>
    <li><a href="https://www.mayoclinic.org/es/diseases-conditions/hearing-loss/diagnosis-treatment/drc-20373077" target="_blank" rel="noopener noreferrer">Mayo Clinic: Diagnóstico y tratamiento de pérdida auditiva</a></li>
    <li><a href="https://www.argentina.gob.ar/justicia/derechofacil/leysimple/hipoacusia" target="_blank" rel="noopener noreferrer">Ley sobre hipoacusia en Argentina</a></li>
    <li><a href="https://masaudio.cl/faqs/son-todos-los-audifonos-para-sordos-iguales/" target="_blank" rel="noopener noreferrer">MasAudio: FAQ sobre audífonos para sordos</a></li>
    <li><a href="https://www.cronista.com/informacion-gral/no-es-solo-para-escuchar-el-estudio-cientifico-que-revelo-el-sorprendente-beneficio-de-usar-audifonos/" target="_blank" rel="noopener noreferrer">El Cronista: Beneficios de usar audífonos</a></li>
    <li><a href="https://dspace.ups.edu.ec/bitstream/123456789/25160/1/UPS-CT010613.pdf" target="_blank" rel="noopener noreferrer">Documento UPS: Investigación relacionada</a></li>
    <li><a href="https://www.nidcd.nih.gov/es/espanol/audifonos" target="_blank" rel="noopener noreferrer">Instituto Nacional de Sordera y Otros Trastornos de la Comunicación (NIDCD)</a></li>
    <li>Manual de encuestas sobre el cuidado del oído y audición – OMS</li>
  </ul>

  <hr />

  <h2>⚖️ Licencia</h2>
  <p>Este proyecto está bajo la licencia <strong>MIT</strong>. Libre para uso personal, educativo o social.</p>

  <p class="footer">Creado con esfuerzo, código y empatía 🧠💻</p>
</div>

</body>
</html>
