import customtkinter as ctk
import webbrowser
import yt_dlp
import lyricsgenius
from tkinter import *
import webbrowser
import re
from tkinter import messagebox
import emoji

# VÄRVID JA GENIUS LYRICS API
kollane = "#F9ED32"
tumesinine = "#0B0F19"
roosa = "#EF4D8D"
veel_tumedam_tumesinine = "#0A0D13"

genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)

# FUNKTSIOONID:

# FUNK. 1 : LEIAB ARTISTI LAULUD JA INSERTIB NAD ÕIGESSE KOHTA
def artisti_laulud(): 
    artist = artisti_nime_sisend.get()
    artistilauludobj = genius.search_artist(artist, max_songs=3)
    global artisti_laulud
    # RE TEEK MUUDAB KUSTUTAB ÄRA VEIDRAD "PEIDETUD" SÜMBOLID, MIS LAULU PEALKIRJA KLAPPIVUST KASUTAJA SISENDIGA VÕRDLEMIST TAKISTAVAD
    # [] SULGUDE SEES ON ERANDID, MIDA RE TEEK EI KUSTUTA, SEST NEED ESINEVAD PALJUDES LAULUPEALKIRJADES
    artisti_laulud = [re.sub(r'[^\w\'‘’()!?+,.]+', ' ', song.title.lower()).strip() for song in artistilauludobj.songs]
    
    
    global koht_artistilauludeks
    koht_artistilauludeks.configure(text="\n".join(artisti_laulud))
    koht_artistilauludeks.pack(fill='both', padx=10, pady=10) 

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

# FUNK. 2 : LEIAB LAULU SÕNAD NING INSERTIB NAD ÕIGESSE KOHTA
def laulu_sõnad():
    genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP")
    laulunimi = laulu_nime_sisend.get()
    artist = artisti_nime_sisend.get()
    laul = genius.search_song(laulunimi, artist)
    sõnad = laul.lyrics
    koht_laulu_sõnadeks.configure(text=sõnad)

# FUNK. 3 : LEIAB LAULU VIDEO YOUTUBEST JA AVAB SELLE
def video():
    selected_song = laulu_nime_sisend.get() + " " + artisti_nime_sisend.get()

    # Otsib laulu üles Youtube'ist
    ydl = yt_dlp.YoutubeDL({'format': 'bestaudio'})
    search_query = f"ytsearch:{selected_song}" 
    info = ydl.extract_info(search_query, download=False)

    # Sorteerib suuremast väiksemani
    sorted_results = sorted(info['entries'], key=lambda x: int(x['view_count']), reverse=True)

    # Võtab kõige vaadatuma video URLi
    video_url = sorted_results[0]['webpage_url']

    # Avab Youtube'i lingi veebilehitsejas
    webbrowser.open(video_url)

# FUNK. 4 : KUI KASUTAJA KLIKIB NUPPU OTSI SIIS KÄIVITAB FUNK. FUNKTSIOONID LAULU_SÕNAD JA VIDEO 
def otsi():
    user_input_lower = (laulu_nime_sisend.get()).lower()
    print("User input (lowercase):", user_input_lower)
    print("Suggested songs (lowercase):", [song.lower() for song in artisti_laulud])

    if user_input_lower not in [song.lower() for song in artisti_laulud]:
        messagebox.showerror("Viga", f"PAHA LUGU! '{user_input_lower}' ei ole üks kolmest soovitatud laulust. VAATA ÜLE, MIS SA KIRJUTASID!")
    else:
        laulu_sõnad()
        video()

# FUNK. 5 : Lähtestab kõik lahtrid ja nupud
def reset():
    if laulu_nimi_tekst:
        laulu_nimi_tekst.pack_forget()
    if laulu_nime_sisend:
        laulu_nime_sisend.pack_forget()
    if koht_laulu_sõnadeks:
        koht_laulu_sõnadeks.pack_forget()
    if nupp:
        nupp.pack_forget()
    if koht_artistilauludeks:
        koht_artistilauludeks.pack_forget()
        koht_artistilauludeks.configure(text="")
    if reset_nupp:
        reset_nupp.pack_forget()

    artistinupp.pack()
    koht_artistilauludeks.pack()
    reset_nupp.pack_forget()

# RAKENDUSE AKEN
app = ctk.CTk()
app.title(f"HENRI & AX MUSIC MACHINA {emoji.emojize(':call_me_hand:')}{emoji.emojize(':smiling_face_with_sunglasses:')}{emoji.emojize(':call_me_hand:')} MAC")
app.geometry("900x700")
app.resizable(False, False)

# TAUSTAPILT
pilt = PhotoImage(file="TAUST.png")
canvas = Canvas(app, width=900, height=700)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=pilt)

#CURSOR
app.configure(cursor="crosshair")


# KERITAV AKEN
scroll = ctk.CTkScrollableFrame(canvas, fg_color=tumesinine, width=500, height=400, scrollbar_button_color=veel_tumedam_tumesinine, scrollbar_button_hover_color=roosa, corner_radius=0)
scroll.place(relx=0.5, rely=0.5, anchor=CENTER)


# LAHTRID, MIS ALGUSEST PEALE NÄHTAVAD: ARTISTI NIMI, ARTISTI LAULUD
artisti_nimi_tekst = ctk.CTkLabel(scroll, text="ARTISTI NIMI:", fg_color=tumesinine, text_color=kollane, font=('Bebas Neue', 30), corner_radius=10)
artisti_nimi_tekst.pack(fill='x', padx=10, pady=10)
artisti_nime_sisend = ctk.CTkEntry(scroll, font=("Bebas Neue", 30), border_color=kollane, border_width=1, justify="center", fg_color=tumesinine, text_color=roosa, corner_radius=10)
artisti_nime_sisend.pack(fill='x', padx=10, pady=10)


# SÄTESTATUD KOHAD JA NUPUD, MIS HILJEM NÄHTAVAKS MUUDETAKSE
    
artistinupp = ctk.CTkButton(scroll, text="Artisti laulud", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=artisti_laulud)
artistinupp.pack(fill='x', padx=10, pady=10)

koht_artistilauludeks = ctk.CTkLabel(scroll, text="ARTISTI LAULUD ON: ", font=("Bebas Neue", 30), justify="center", fg_color=tumesinine, text_color=kollane, corner_radius=10)

reset_nupp = ctk.CTkButton(scroll, text="Reset", font=("Bebas Neue", 30), text_color=kollane, border_color=kollane, border_width=1, corner_radius=10, fg_color=tumesinine, hover_color=roosa, command=reset)


app.mainloop()
