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

# FUNKTSIOONID:

# FUNK. 1 : LEIAB ARTISTI LAULUD JA INSERTIB NAD ÕIGESSE KOHTA
def artisti_laulud():
    artist = artisti_nime_sisend.get()
    artistilauludobj = genius.search_artist(artist, max_songs=7) 
    artistilaulud = [song.title for song in artistilauludobj.songs]
    koht_artistilauludeks.configure(text="\n".join(artistilaulud))
    
artistinupp =ctk.CTkButton(scroll, text="Artisti laulud", command=artisti_laulud)
artistinupp.pack(fill='x', padx=10, pady=10)

# SISEND + TEKST
laulu_nimi_tekst = ctk.CTkLabel(scroll, text="LAULU NIMI:")
laulu_nimi_tekst.pack(fill='x', padx=10, pady=10)
laulu_nime_sisend = ctk.CTkEntry(scroll)
laulu_nime_sisend.pack(fill='x', padx=10, pady=10)

    global nupp
    nupp = ctk.CTkButton(scroll, text="OTSI", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=otsi)
    nupp.pack(fill='x', padx=10, pady=10)

    global koht_laulu_sõnadeks
    koht_laulu_sõnadeks = ctk.CTkLabel(scroll, text="", font=("Bebas Neue", 20), justify="center", fg_color=tumesinine, text_color=kollane)
    koht_laulu_sõnadeks.pack(fill='both', padx=10, pady=10)

    reset_nupp.pack(fill='x', padx=10, pady=10)

# FUNK. 2 : LEIAB LAULU SÕNAD NING INSERTIB NAD ÕIGESSE KOHTA
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

koht_artistilauludeks = ctk.CTkLabel(scroll, text="ARTISTI LAULUD ON: ", font=("Bebas Neue", 30), justify="center", fg_color=tumesinine, text_color=kollane, corner_radius=10)

reset_nupp = ctk.CTkButton(scroll, text="Reset", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=reset)


app.mainloop()
