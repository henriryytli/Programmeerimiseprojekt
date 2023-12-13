import webbrowser
import tkinter as tk
import yt_dlp
import lyricsgenius

# Looge Genius Lyrics objekt
genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)

def otsi_laulud():
    # Küsi kasutajalt artisti nimi
    global artisti_nimi
    artisti_nimi = artisti_sisend.get()

    # Otsi artisti laulud
    global artist 
    artist = genius.search_artist(artisti_nimi, max_songs=3)

    # Kontrolli, kas leiti laule
    if artist.songs:
        laulud_valik.configure(state="normal")
        laulud_valik.delete(1.0, tk.END)
        laulud_valik.insert(tk.END, "Vali laul:\n")
        for i, song in enumerate(artist.songs):
            laulud_valik.insert(tk.END, f"{i+1}. {song.title}\n")
        laulud_valik.configure(state="disabled")
    else:
        laulud_valik.configure(state="normal")
        laulud_valik.delete(1.0, tk.END)
        laulud_valik.insert(tk.END, "Antud artisti laule ei leitud.")
        laulud_valik.configure(state="disabled")

def kuvada_sonad():
    # Hangi valitud laulu number
    valitud_laul = int(laulu_valik.get())

    # Kontrolli, kas valitud laulu number on kehtiv
    if 1 <= valitud_laul <= len(artist.songs):
        valitud_laul = artist.songs[valitud_laul - 1]

        # Hangi valitud laulu sõnad
        lyrics = valitud_laul.lyrics
        sõnade_kuvamine.configure(state="normal")
        sõnade_kuvamine.delete(1.0, tk.END)
        sõnade_kuvamine.insert(tk.END, "Valitud laulu sõnad:\n")
        sõnade_kuvamine.insert(tk.END, lyrics)
        sõnade_kuvamine.configure(state="disabled")

        # Hangi valitud laulu YouTube link
        ydl = yt_dlp.YoutubeDL()
        laulu_info = ydl.extract_info(f"ytsearch:{valitud_laul.title} {artisti_nimi}", download=False)
        video_url = laulu_info['entries'][0]['webpage_url']

        # Ava URL veebibrauseris, et hakata videot mängima
        webbrowser.open(video_url)

        # Hangi valitud laulu vaatamiste arv YouTube'is
        views = laulu_info['entries'][0]['view_count']
        vaatamiste_arv.configure(state="normal")
        vaatamiste_arv.delete(1.0, tk.END)
        vaatamiste_arv.insert(tk.END, "Valitud laulu vaatamiste arv YouTube'is:\n")
        vaatamiste_arv.insert(tk.END, views)
        vaatamiste_arv.configure(state="disabled")

    else:
        sõnade_kuvamine.configure(state="normal")
        sõnade_kuvamine.delete(1.0, tk.END)
        sõnade_kuvamine.insert(tk.END, "Vigane valik. Palun sisesta kehtiv laulu number.")
        sõnade_kuvamine.configure(state="disabled")

# Looge tkinter aken
aken = tk.Tk()
aken.title("Lauluinfo")

# Looge kasutajaliidese elemendid
artisti_silt = tk.Label(aken, text="Sisesta artisti nimi:")
artisti_silt.pack()

artisti_sisend = tk.Entry(aken)
artisti_sisend.pack()

otsi_nupp = tk.Button(aken, text="Otsi laulud", command=otsi_laulud)
otsi_nupp.pack()

laulu_valik = tk.Entry(aken)
laulu_valik.pack()

sõnade_kuvamine = tk.Text(aken, height=10, width=50)
sõnade_kuvamine.configure(state="disabled")
sõnade_kuvamine.pack()

vaatamiste_arv = tk.Text(aken, height=1, width=50)
vaatamiste_arv.configure(state="disabled")
vaatamiste_arv.pack()

laulud_valik = tk.Text(aken, height=10, width=50)
laulud_valik.configure(state="disabled")
laulud_valik.pack()

kuvada_nupp = tk.Button(aken, text="Kuva sõnad ja info", command=kuvada_sonad)
kuvada_nupp.pack()

# Käivita tkinter aken
aken.mainloop()

import webbrowser
import tkinter as tk
import yt_dlp
import lyricsgenius

# Looge Genius Lyrics objekt
genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)

def otsi_laulud():
    # Küsi kasutajalt artisti nimi
    artisti_nimi = artisti_sisend.get()
    
    # Otsi laule Genius Lyrics API abil
    artist = genius.search_artist(artisti_nimi, max_songs=3)
    
    # Kuvada leitud laulud
    laulud_valik.configure(state="normal")
    laulud_valik.delete("1.0", tk.END)
    for i, song in enumerate(artist.songs):
        laulud_valik.insert(tk.END, f"Song {i+1}: {song.title}\n")
    laulud_valik.configure(state="disabled")

def kuvada_sonad():
    # Hangi valitud laulu number
    valitud_laul = int(laulu_valik.get())
    
    # Hangi artisti laulud
    artist = genius.search_artist("The Beatles", max_songs=3)
    
    # Kuvada laulu sõnad ja info
    if 1 <= valitud_laul <= len(artist.songs):
        song = artist.songs[valitud_laul - 1]
        sõnade_kuvamine.configure(state="normal")
        sõnade_kuvamine.delete("1.0", tk.END)
        sõnade_kuvamine.insert(tk.END, f"Lyrics for {song.title}:\n\n{song.lyrics}")
        sõnade_kuvamine.configure(state="disabled")
    else:
        sõnade_kuvamine.configure(state="normal")
        sõnade_kuvamine.delete("1.0", tk.END)
        sõnade_kuvamine.insert(tk.END, "Invalid song selection")
        sõnade_kuvamine.configure(state="disabled")

# Looge tkinter aken
aken = tk.Tk()
aken.title("Lauluinfo")

# Looge kasutajaliidese elemendid
artisti_silt = tk.Label(aken, text="Sisesta artisti nimi:")
artisti_silt.pack()

artisti_sisend = tk.Entry(aken)
artisti_sisend.pack()

otsi_nupp = tk.Button(aken, text="Otsi laulud", command=otsi_laulud)
otsi_nupp.pack()

laulu_valik = tk.Entry(aken)
laulu_valik.pack()

sõnade_kuvamine = tk.Text(aken, height=10, width=50)
sõnade_kuvamine.configure(state="disabled")
sõnade_kuvamine.pack()

vaatamiste_arv = tk.Text(aken, height=1, width=50)
vaatamiste_arv.configure(state="disabled")
vaatamiste_arv.pack()

laulud_valik = tk.Text(aken, height=10, width=50)
laulud_valik.configure(state="disabled")
laulud_valik.pack()

kuvada_nupp = tk.Button(aken, text="Kuva sõnad ja info", command=kuvada_sonad)
kuvada_nupp.pack()

# Käivita tkinter aken
aken.mainloop()

def vali_laul(event):
    valitud_laul = laulu_valik.get()
    # Tehke midagi valitud lauluga, näiteks kuvage sõnad või info
