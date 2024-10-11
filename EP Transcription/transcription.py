import whisper
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES

# Función para transcribir archivos con Whisper
def transcribir_archivo_whisper(ruta_archivo):
    try:
        modelo = whisper.load_model("base")  # Cargar el modelo base de Whisper
        resultado = modelo.transcribe(ruta_archivo)
        return resultado['text']
    except Exception as e:
        messagebox.showerror("Error", f"Error en la transcripción: {str(e)}")
        return ""

# Función para manejar el drag and drop
def on_drop(event):
    ruta_archivo = event.data
    ruta_archivo = ruta_archivo.strip('{}')  # Limpiar el formato del path si tiene llaves
    transcripcion = transcribir_archivo_whisper(ruta_archivo)
    
    # Mostrar la transcripción en la ventana
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, transcripcion)

# Función para abrir el explorador de archivos
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.mp4 *.wav *.m4a")])
    if ruta_archivo:
        transcripcion = transcribir_archivo_whisper(ruta_archivo)
        
        # Mostrar la transcripción en la ventana
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, transcripcion)

# Configuración de la interfaz gráfica
root = TkinterDnD.Tk()
root.title("Transcriptor Whisper con Drag and Drop")
root.geometry("600x400")

# Instrucciones para el usuario
label = tk.Label(root, text="Arrastra y suelta el archivo aquí o haz clic en 'Abrir archivo'", font=("Arial", 12))
label.pack(pady=10)

# Botón para abrir el explorador de archivos manualmente
btn_abrir = tk.Button(root, text="Abrir archivo", command=abrir_archivo, font=("Arial", 10))
btn_abrir.pack(pady=10)

# Área de texto donde se mostrará la transcripción
text_area = tk.Text(root, wrap=tk.WORD, height=15, font=("Arial", 10))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Configurar el área de drag and drop
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# Ejecutar la ventana
root.mainloop()
