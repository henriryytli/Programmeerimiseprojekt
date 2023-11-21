import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
import tkinter as tk

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme("green")

# RAKENDUSE AKEN
app = ctk.CTk()
app.title("MEIE PROGRAMM")
app.geometry("400x200")

# SISEND + TEKST
artisti_nimi_tekst = ctk.CTkLabel(app, text="ARTISTI NIMI:")
artisti_nimi_tekst.grid(row=0, column=0, padx=10, pady=10)
artisti_nime_sisend = ctk.CTkEntry(app)
artisti_nime_sisend.grid(row=0, column=1, padx=10, pady=10)

# SISEND + TEKST
laulu_nimi_tekst = ctk.CTkLabel(app, text="LAULU NIMI:")
laulu_nimi_tekst.grid(row=1, column=0, padx=10, pady=10)
laulu_nime_sisend = ctk.CTkEntry(app)
laulu_nime_sisend.grid(row=1, column=1, padx=10, pady=10)

# FUNK. LEIAB LAULU SÕNAD NING INSERTIB NAD ÕIGESSE KOHTA
def laulu_sõnad():
    genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP")
    laulunimi = laulu_nime_sisend.get()
    artist = artisti_nime_sisend.get()
    laul = genius.search_song(laulunimi, artist)
    sõnad = laul.lyrics
    koht_laulu_sõnadeks.configure(text=sõnad)

koht_laulu_sõnadeks = ctk.CTkLabel(app, text="")
koht_laulu_sõnadeks.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

scroll = ctk.CTkScrollableFrame(app)
scroll.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
# scroll.place(relx=0.5, rely=0.5, anchor="center")
scroll.configure(width=app.winfo_width() * 0.8, height=100)

# TEEB SÕNADE AKNA SCROLLABLEIKS
sõnad_tekst = ctk.CTkLabel(scroll, text="")
sõnad_tekst.pack()

nupp = ctk.CTkButton(app, text="OTSI", command=laulu_sõnad)
nupp.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



app.mainloop()
