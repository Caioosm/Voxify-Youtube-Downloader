import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from threading import Thread
import yt_dlp

# Função para baixar o áudio do vídeo
def download_audio(url, output_folder):
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook]
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Função de callback para atualizar a barra de progresso
def progress_hook(progress):
    if progress['status'] == 'downloading':
        percent = round(progress['downloaded_bytes'] / progress['total_bytes'] * 100, 2)
        progress_bar['value'] = percent
        progress_label.config(text=f"Progresso: {percent}%")
    elif progress['status'] == 'finished':
        progress_label.config(text="Download Concluído!")
        messagebox.showinfo("Download Concluído", "O download foi concluído com sucesso!")

# Função para escolher a pasta de destino
def choose_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=f"Pasta de Destino: {output_folder}")

# Função para iniciar o download
def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return
    if not output_folder:
        messagebox.showerror("Erro", "Por favor, escolha uma pasta de destino.")
        return

    # Iniciar download em uma thread separada para não travar a GUI
    Thread(target=download_audio, args=(url, output_folder)).start()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Download de Áudio do YouTube")

# Campo de entrada para URL
url_label = tk.Label(root, text="URL do Vídeo:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Botão para escolher a pasta de destino
choose_folder_button = tk.Button(root, text="Escolher Pasta de Destino", command=choose_folder)
choose_folder_button.pack()

# Label para exibir a pasta de destino escolhida
output_folder_label = tk.Label(root, text="Pasta de Destino:")
output_folder_label.pack()

# Botão para iniciar o download
download_button = tk.Button(root, text="Baixar Áudio", command=start_download)
download_button.pack()

# Barra de progresso
progress_label = tk.Label(root, text="Progresso:")
progress_label.pack()
progress_bar = tk.ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()

root.mainloop()
