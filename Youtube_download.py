import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidgets():
      
    link_label = Label(root, text="Link Youtube     ", bg="#90EE90")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Penyimpanan    ", bg="#90EE90")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=60, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_button = Button(root, text="Browse", command=browse, width=10, bg="#90EE90")
    browse_button.grid(row=2, column=2, pady=1, padx=1)

    download_button = Button(root, text="Download", command=download_video, width=25, bg="#90EE90")
    download_button.grid(row=3, column=1, pady=3, padx=3)

    
    author_label = Label(root, text="Program By Rzkyads_", bg="#708090")
    author_label.grid(row=7, column=1, pady=5, padx=5) 


def browse():
    dowload_direktori = filedialog.askdirectory(initialdir="Your directory Path")

    download_path.set(dowload_direktori)


def download_video():
    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_streams = get_video.streams.filter(res="720p").first()
    get_streams.download(folder)

    messagebox.showinfo("Berhasil", "Download telah selesai!")


root = tk.Tk()

root.geometry('600x170')
root.resizable(False, False)
root.title("Youtube_Downloader")
root.config(background=	"#708090")

video_link = StringVar()
download_path = StringVar()

createWidgets()
root.mainloop()