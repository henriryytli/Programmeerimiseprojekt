import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
import tkinter as tk
import webbrowser

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
    genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)
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

def video():
    selected_song = laulu_nime_sisend.get()

    # Search for the selected song on YouTube
    ydl = yt_dlp.YoutubeDL({'format': 'bestaudio'})
    search_query = f"ytsearch:{selected_song}"  # Remove 'artist' and 'title' from the search query
    info = ydl.extract_info(search_query, download=False)

    # Sort the search results by view count in descending order
    sorted_results = sorted(info['entries'], key=lambda x: int(x['view_count']), reverse=True)

    # Get the URL of the video with the most views
    video_url = sorted_results[0]['webpage_url']

    # Open the YouTube video in a web browser
    webbrowser.open(video_url)


koht_artistilauludeks = ctk.CTkLabel(scroll, text="Artisti laulud on: ")
koht_artistilauludeks.pack(fill='both', padx=10, pady=10)

def otsi():
    laulu_sõnad()
    video()

nupp = ctk.CTkButton(scroll, text="OTSI", command=otsi)
nupp.pack(fill='x', padx=10, pady=10)

koht_laulu_sõnadeks = ctk.CTkLabel(scroll, text="")
koht_laulu_sõnadeks.pack(fill='both', padx=10, pady=10)

app.mainloop()
