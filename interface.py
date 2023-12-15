import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
from tkinter import *
import webbrowser
import random

#VÄRVID

kollane = "#F9ED32"
tumesinine = "#0B0F19"
roosa = "#EF4D8D"


# RAKENDUSE AKEN
app = ctk.CTk()
app.title("HENRI & AX MUSIC MACHINE")
app.geometry("900x700")
app.resizable(False, False)

# Load background image
pilt = PhotoImage(file="TAUST.png")

# Create a Canvas widget to hold the background image
canvas = Canvas(app, width=900, height=700)
canvas.pack()

# Place the background image on the Canvas
canvas.create_image(0, 0, anchor=NW, image=pilt)

# SCROLLABLE FRAME FOR THE WHOLE PROGRAM
scroll = ctk.CTkScrollableFrame(canvas, fg_color=tumesinine, width=500, height=400, scrollbar_button_color=kollane, scrollbar_button_hover_color=roosa, corner_radius=0)
scroll.place(relx=0.5, rely=0.5, anchor=CENTER)

# SISEND + TEKST
artisti_nimi_tekst = ctk.CTkLabel(scroll, text="ARTISTI NIMI:", fg_color=tumesinine, text_color=kollane, font=("Bebas Neue", 30), corner_radius=10)
artisti_nimi_tekst.pack(fill='x', padx=10, pady=10)
artisti_nime_sisend = ctk.CTkEntry(scroll, font=("Bebas Neue", 30), border_color=kollane, border_width=1, justify="center", fg_color=tumesinine, text_color=roosa, corner_radius=10)
artisti_nime_sisend.pack(fill='x', padx=10, pady=10)

genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)

def artisti_laulud():
    artist = artisti_nime_sisend.get()
    artistilauludobj = genius.search_artist(artist, max_songs=7) 
    artistilaulud = [song.title for song in artistilauludobj.songs]
    suggested_songs = random.sample(artistilaulud, 3)  # Select three random songs from the list
    
    global koht_laulu_sõnadeks
    koht_artistilauludeks.configure(text="\n".join(suggested_songs))
    koht_artistilauludeks.pack(fill='both', padx=10, pady=10)  # Pack the label when the button is clicked

    global laulu_nimi_tekst
    laulu_nimi_tekst = ctk.CTkLabel(scroll, text="LAUL, MILLE SÕNU TAHAD:", fg_color=tumesinine, text_color=kollane, font=("Bebas Neue", 30), corner_radius=10)
    
    global laulu_nime_sisend
    laulu_nime_sisend = ctk.CTkEntry(scroll, font=("Bebas Neue", 30), border_color=kollane, border_width=1, justify="center", fg_color=tumesinine, text_color=roosa, corner_radius=10) 
    laulu_nime_sisend.pack(fill='x', padx=10, pady=10)

    global nupp
    nupp = ctk.CTkButton(scroll, text="OTSI", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=otsi)
    nupp.pack(fill='x', padx=10, pady=10)

    global koht_laulu_sõnadeks
    koht_laulu_sõnadeks = ctk.CTkLabel(scroll, text="", font=("Bebas Neue", 20), justify="center", fg_color=tumesinine, text_color=kollane)
    koht_laulu_sõnadeks.pack(fill='both', padx=10, pady=10)

    reset_nupp.pack(fill='x', padx=10, pady=10)

    
artistinupp = ctk.CTkButton(scroll, text="Artisti laulud", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=artisti_laulud)
artistinupp.pack(fill='x', padx=10, pady=10)

koht_artistilauludeks = ctk.CTkLabel(scroll, text="ARTISTI LAULUD ON: ", font=("Bebas Neue", 30), justify="center", fg_color=tumesinine, text_color=kollane, corner_radius=10)




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


def otsi():
    laulu_sõnad()
    video()

    if laulu_nimi_tekst:
        laulu_nimi_tekst.destroy()

def reset():
    if laulu_nimi_tekst:
        laulu_nimi_tekst.destroy()
    if laulu_nime_sisend:
        laulu_nime_sisend.destroy()
    if koht_laulu_sõnadeks:
        koht_laulu_sõnadeks.destroy()
    if nupp:
        nupp.destroy()
    if koht_artistilauludeks:
        koht_artistilauludeks.destroy()
    
    artisti_nimi_tekst = ctk.CTkLabel(scroll, text="ARTISTI NIMI:", fg_color=tumesinine, text_color=kollane, font=("Bebas Neue", 30), corner_radius=10)
    artisti_nimi_tekst.pack(fill='x', padx=10, pady=10)
    artisti_nime_sisend = ctk.CTkEntry(scroll, font=("Bebas Neue", 30), border_color=kollane, border_width=1, justify="center", fg_color=tumesinine, text_color=roosa, corner_radius=10)
    artisti_nime_sisend.pack(fill='x', padx=10, pady=10)

    artistinupp = ctk.CTkButton(scroll, text="Artisti laulud", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=artisti_laulud)
    artistinupp.pack(fill='x', padx=10, pady=10)

    koht_artistilauludeks = ctk.CTkLabel(scroll, text="ARTISTI LAULUD ON: ", font=("Bebas Neue", 30), justify="center", fg_color=tumesinine, text_color=kollane, corner_radius=10)

        



reset_nupp = ctk.CTkButton(scroll, text="Reset", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=reset)


app.mainloop()
