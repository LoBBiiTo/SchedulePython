import schedule
import time
import pywhatkit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Para el calendario
import json
from plyer import notification  # Para notificaciones locales
import threading  # Para manejar hilos
import pyautogui  # Para simular el clic en "Enviar"

# Función para enviar mensaje por WhatsApp
def enviar_mensaje_whatsapp(numero, mensaje, progress_bar, status_label):
    try:
        print(f"Intentando enviar mensaje a {numero}...")
        status_label.config(text=f"Enviando mensaje a {numero}...")
        root.update_idletasks()  # Actualiza la interfaz
        
        # Envía el mensaje usando pywhatkit con un tiempo de espera mayor
        pywhatkit.sendwhatmsg_instantly(f"+{numero}", mensaje, wait_time=10)
        
        # Simula presionar la tecla "Enter" para enviar el mensaje automáticamente
        time.sleep(2)  # Espera 5 segundos para asegurarse de que el mensaje esté escrito
        pyautogui.press('enter')  # Presiona la tecla "Enter" para enviar el mensaje
        
        print(f"Mensaje enviado a {numero}: {mensaje}")
        mostrar_notificacion(f"Mensaje enviado a {numero}", mensaje)
        status_label.config(text=f"Mensaje enviado a {numero}")
        root.update_idletasks()  # Actualiza la interfaz
    except Exception as e:
        print(f"Error al enviar mensaje a {numero}: {e}")
        mostrar_notificacion("Error", f"No se pudo enviar el mensaje a {numero}. Detalles: {e}")
        status_label.config(text=f"Error al enviar mensaje a {numero}")
        root.update_idletasks()  # Actualiza la interfaz
    finally:
        # Actualiza la barra de progreso
        progress_bar['value'] += 1
        root.update_idletasks()

# Función para mostrar notificaciones locales
def mostrar_notificacion(titulo, mensaje):
    notification.notify(
        title="Programador de Mensajes WhatsApp",  # Título personalizado
        message=mensaje,
        timeout=10  # Duración de la notificación en segundos
    )

# Función para enviar mensajes de inmediato
def enviar_de_inmediato():
    numeros = numero_entry.get().split(',')
    mensaje = mensaje_combobox.get() if mensaje_combobox.get() else mensaje_entry.get("1.0", END).strip()

    if not numeros or not mensaje:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    total_mensajes = len(numeros)
    progress_bar['maximum'] = total_mensajes
    progress_bar['value'] = 0
    status_label.config(text="Iniciando envío de mensajes...")
    root.update_idletasks()

    for numero in numeros:
        numero = numero.strip()
        if numero:
            enviar_mensaje_whatsapp(numero, mensaje, progress_bar, status_label)

    status_label.config(text="Todos los mensajes han sido enviados.")
    root.update_idletasks()

# Función para programar el envío de mensajes con horario
def programar_con_horario():
    numeros = numero_entry.get().split(',')
    mensaje = mensaje_combobox.get() if mensaje_combobox.get() else mensaje_entry.get("1.0", END).strip()
    horario = horario_entry.get()
    fecha_seleccionada = fecha_calendario.get_date()

    if not numeros or not mensaje or not horario:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    hora, minuto = map(int, horario.split(':'))

    def tarea_programada():
        total_mensajes = len(numeros)
        progress_bar['maximum'] = total_mensajes
        progress_bar['value'] = 0
        status_label.config(text="Iniciando envío de mensajes...")
        root.update_idletasks()

        for numero in numeros:
            numero = numero.strip()
            if numero:
                enviar_mensaje_whatsapp(numero, mensaje, progress_bar, status_label)

        status_label.config(text="Todos los mensajes han sido enviados.")
        root.update_idletasks()

    # Programa la tarea según la fecha y horario seleccionados
    schedule.every().day.at(f"{hora:02d}:{minuto:02d}").do(tarea_programada).tag("horario_task")
    messagebox.showinfo("Éxito", f"Mensajes programados para las {horario} del {fecha_seleccionada}.")

# Función para guardar configuraciones en un archivo JSON
def guardar_configuracion(numeros, mensaje, horario, fecha):
    configuracion = {
        "numeros": numeros,
        "mensaje": mensaje,
        "horario": horario,
        "fecha": str(fecha)
    }
    with open("configuracion.json", "w") as archivo:
        json.dump(configuracion, archivo)
    print("Configuración guardada.")

# Función para cargar configuraciones desde un archivo JSON
def cargar_configuracion():
    try:
        with open("configuracion.json", "r") as archivo:
            configuracion = json.load(archivo)
            numero_entry.delete(0, END)
            numero_entry.insert(0, ', '.join(configuracion["numeros"]))
            mensaje_entry.delete("1.0", END)
            mensaje_entry.insert(END, configuracion["mensaje"])
            horario_entry.delete(0, END)
            horario_entry.insert(0, configuracion["horario"])
            fecha_calendario.set_date(configuracion["fecha"])
        messagebox.showinfo("Éxito", "Configuración cargada correctamente.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró ningún archivo de configuración.")

# Función para ejecutar el bucle de tareas programadas en un hilo separado
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Interfaz gráfica con Tkinter
def crear_interfaz():
    global root
    root = Tk()
    root.title("Programador de Mensajes WhatsApp")
    root.geometry("600x700")
    root.configure(bg="#2d2d2d")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", background="#2d2d2d", foreground="white")
    style.configure("TButton", background="#4CAF50", foreground="white")
    style.configure("TEntry", fieldbackground="#444", foreground="white")

    # Etiqueta y entrada para los números de teléfono
    Label(root, text="Números de Teléfono (separados por comas, con código de país):", bg="#2d2d2d", fg="white").pack(pady=5)
    global numero_entry
    numero_entry = Entry(root, bg="#444", fg="white", width=50)
    numero_entry.pack(pady=5)

    # Combobox para mensajes predefinidos
    Label(root, text="Selecciona un mensaje predefinido o escribe uno nuevo:", bg="#2d2d2d", fg="white").pack(pady=5)
    global mensaje_combobox
    mensaje_combobox = ttk.Combobox(root, values=[
        "Recuerda tomar un descanso",
        "Es hora de almorzar",
        "No olvides hidratarte",
        "Hora de hacer ejercicio"
    ])
    mensaje_combobox.pack(pady=5)

    # Área de texto para el mensaje personalizado
    Label(root, text="O escribe tu propio mensaje:", bg="#2d2d2d", fg="white").pack(pady=5)
    global mensaje_entry
    mensaje_entry = Text(root, height=5, width=50, bg="#444", fg="white")
    mensaje_entry.pack(pady=5)

    # Botón para enviar mensajes de inmediato
    ttk.Button(root, text="Enviar de Inmediato", command=enviar_de_inmediato).pack(pady=10)

    # Entrada para programar con horario
    Label(root, text="Programar con Horario (HH:MM):", bg="#2d2d2d", fg="white").pack(pady=5)
    global horario_entry
    horario_entry = Entry(root, bg="#444", fg="white")
    horario_entry.pack(pady=5)

    # Calendario para seleccionar la fecha
    Label(root, text="Fecha:", bg="#2d2d2d", fg="white").pack(pady=5)
    global fecha_calendario
    fecha_calendario = DateEntry(root, date_pattern='yyyy-mm-dd', background="#444", foreground="white")
    fecha_calendario.pack(pady=5)

    ttk.Button(root, text="Programar con Horario", command=programar_con_horario).pack(pady=5)

    # Botón para cargar configuraciones
    ttk.Button(root, text="Cargar Configuración", command=cargar_configuracion).pack(pady=5)

    # Barra de progreso
    global progress_bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=10)

    # Etiqueta de estado
    global status_label
    status_label = Label(root, text="Esperando...", bg="#2d2d2d", fg="white")
    status_label.pack(pady=5)

    # Iniciar el bucle de schedule en un hilo separado
    threading.Thread(target=run_schedule, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()