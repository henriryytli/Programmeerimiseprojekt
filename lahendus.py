import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
from tkinter import *
import webbrowser
import random
from PIL import Image

genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)

# FUNKTSIOONID

def artisti_laulud():
    artist = artisti_nime_sisend.get()
    artistilauludobj = genius.search_artist(artist, max_songs=7) 
    artistilaulud = [song.title for song in artistilauludobj.songs]
    suggested_songs = random.sample(artistilaulud, 3)  # Select three random songs from the list
    koht_artistilauludeks.configure(text="\n".join(suggested_songs))
    





# RAKENDUSE AKEN

app = ctk.CTk()
app.title("HENRI & AX MUSIC MACHINE")
app.geometry("800x600")
app.resizable(False, False)

# TAUSTAPILT
pilt = PhotoImage(file="BGROUND-01.png")
canvas = Canvas(app, width=800, height=600)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=pilt)

# PROGRAMM

canvas.create_text(400, 50, text="SISESTA ARTISTI NIMI", font=("Cynatar", 40), fill="#F9ED32")
artisti_nime_sisend = Entry(app, font=("Cynatar", 40), justify="center")
canvas.create_window(400, 150, window=artisti_nime_sisend, width=400, height=50)
nupp1 = Button(app, text="Artisti laulud", font=("Cynatar", 40), command=artisti_laulud)
canvas.create_window(400, 250, window=nupp1, width=400, height=50)

koht_artistilauludeks = ctk.CTkLabel(app, font=("Cynatar", 40), justify="center", fg_color="transparent")
canvas.create_window(400, 350, window=koht_artistilauludeks, width=400, height=50)

canvas.create_text(400, 250, text="SISESTA LAULU NIMI", font=("Cynatar", 40), fill="#F9ED32")

app.mainloop()