# Programador de Mensajes WhatsApp

Este es un programa en Python que te permite programar mensajes automáticos para enviar a través de WhatsApp Web. Puedes enviar mensajes de inmediato o programarlos para un horario específico. El programa también incluye una interfaz gráfica amigable con colores oscuros para facilitar su uso.

## Características Principales

- **Enviar mensajes de inmediato**: Envía mensajes sin necesidad de esperar.
- **Programar mensajes con horario**: Configura mensajes para que se envíen automáticamente a una hora específica.
- **Interfaz gráfica**: Una interfaz fácil de usar con opciones para ingresar números de teléfono, mensajes y horarios.
- **Notificaciones locales**: Recibe notificaciones cuando los mensajes se envían correctamente o si ocurre algún error.
- **Guardar y cargar configuraciones**: Guarda tus configuraciones (números, mensajes, horarios) para no tener que ingresarlas cada vez que ejecutes el programa.

## Requisitos Previos

Antes de ejecutar el programa, asegúrate de cumplir con los siguientes requisitos:

1. **Python 3.x**: Este programa está diseñado para funcionar con Python 3. Asegúrate de tenerlo instalado en tu sistema.
   - Puedes descargar Python desde [aquí](https://www.python.org/downloads/).

2. **WhatsApp Web**: Necesitarás tener WhatsApp Web abierto en tu navegador y conectado a tu cuenta de WhatsApp.

3. **Dependencias**:
   - Instala las bibliotecas necesarias ejecutando el siguiente comando:
     ```bash
     pip install schedule pywhatkit tkinter tkcalendar plyer pyautogui
     ```

## Instalación

1. **Clona este repositorio**:
```bash
git clone https://github.com/LoBBiiTo/programador-mensajes-whatsapp.git
cd programador-mensajes-whatsapp
```

2. **Instala las dependecias:**
```bash
pip install -r requirements.txt
```

3. Ejecuta el programa:
```bash
python whatsapp_scheduler.py
```
## Uso

1. **Ingresar datos**:
   - Ingresa los números de teléfono separados por comas en el campo correspondiente. Asegúrate de incluir el código de país (por ejemplo, `+5491121234567` en el caso de Argentina +54).
   - Selecciona un mensaje predefinido de la lista desplegable o escribe tu propio mensaje en el área de texto.
   - Configura el horario y la fecha en la que deseas enviar los mensajes. El formato del horario debe ser `HH:MM` (24 horas).

2. **Enviar mensajes**:
   - Haz clic en **"Enviar de Inmediato"** para enviar los mensajes sin esperar.
   - O haz clic en **"Programar con Horario"** para enviar los mensajes en un horario específico.

3. **Cargar configuraciones**:
   - Si ya tienes una configuración guardada (números, mensajes, horarios), puedes cargarla haciendo clic en **"Cargar Configuración"**.

4. **Notificaciones**:
   - Recibirás notificaciones locales cuando se envíen los mensajes o si ocurre algún error.

## Capturas de Pantalla

### Interfaz Gráfica
![Image Alt](https://github.com/LoBBiiTo/SchedulePython/blob/40043c16793a23bbb5fe4bebe881bae7442f1c84/Interfaz%20EnviarMensajeWpp.png)


## Contribuciones

Si deseas contribuir al proyecto, ¡eres bienvenido! Puedes hacerlo de las siguientes maneras:

- Reportar errores o problemas abriendo un **issue**.
- Proponer mejoras o nuevas características mediante **pull requests**.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Esto significa que puedes usar, modificar y distribuir el código libremente, siempre que incluyas la licencia original.

## Autor

- **LoBBiiTo** - (https://github.com/LoBBiiTo)
