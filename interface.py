import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
import tkinter as tk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme("green")

# RAKENDUSE AKEN
app = ctk.CTk()
app.title("MEIE PROGRAMMI NIMI")
app.geometry("800x600")
app.resizable(False, False)

# SCROLLABLE FRAME FOR THE WHOLE PROGRAM
scroll = ctk.CTkScrollableFrame(app)
scroll.pack(fill='both', expand=True)

# SISEND + TEKST
artisti_nimi_tekst = ctk.CTkLabel(scroll, text="ARTISTI NIMI:")
artisti_nimi_tekst.pack(fill='x', padx=10, pady=10)
artisti_nime_sisend = ctk.CTkEntry(scroll)
artisti_nime_sisend.pack(fill='x', padx=10, pady=10)

def artisti_laulud():
    genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP")
    artist = artisti_nime_sisend.get()
    artistilauludobj = genius.search_artist(artist, max_songs=3)
    artistilaulud = [song.title for song in artistilauludobj.songs]
    koht_artistilauludeks.configure(text="\n".join(artistilaulud))
    
artistinupp =ctk.CTkButton(scroll, text="Artisti laulud", command=artisti_laulud)
artistinupp.pack(fill='x', padx=10, pady=10)

# SISEND + TEKST
laulu_nimi_tekst = ctk.CTkLabel(scroll, text="LAULU NIMI:")
laulu_nimi_tekst.pack(fill='x', padx=10, pady=10)
laulu_nime_sisend = ctk.CTkEntry(scroll)
laulu_nime_sisend.pack(fill='x', padx=10, pady=10)

# FUNK. LEIAB LAULU SÕNAD NING INSERTIB NAD ÕIGESSE KOHTA
def laulu_sõnad():
    genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP")
    laulunimi = laulu_nime_sisend.get()
    artist = artisti_nime_sisend.get()
    laul = genius.search_song(laulunimi, artist)
    sõnad = laul.lyrics
    koht_laulu_sõnadeks.configure(text=sõnad)

koht_artistilauludeks = ctk.CTkLabel(scroll, text="Artisti laulud on: ")
koht_artistilauludeks.pack(fill='both', padx=10, pady=10)

nupp = ctk.CTkButton(scroll, text="OTSI", command=laulu_sõnad)
nupp.pack(fill='x', padx=10, pady=10)

koht_laulu_sõnadeks = ctk.CTkLabel(scroll, text="")
koht_laulu_sõnadeks.pack(fill='both', padx=10, pady=10)

app.mainloop()
