import webbrowser
import yt_dlp
import lyricsgenius

# Prompt the user to enter the artist's name
artist_name = input("Enter the artist's name: ")

# Search for songs by the artist
genius = lyricsgenius.Genius("3-_YnHoVTUfnZK085ZibnT4i14Xr-nsMVNuXt_HS17Kbd0BcSAXPzhyl5wqc6ktP", timeout=60)
artist = genius.search_artist(artist_name, max_songs=3)

# Display the songs by the artist
print("Songs by", artist.name)
for i, song in enumerate(artist.songs):
    print(f"{i+1}. {song.title}")

# Prompt the user to select a song
song_choice = int(input("Select a song (enter the corresponding number): "))

# Get the selected song
selected_song = artist.songs[song_choice - 1]

# Search for the selected song on YouTube
ydl = yt_dlp.YoutubeDL({'format': 'bestaudio'})
search_query = f"ytsearch:{selected_song.artist} - {selected_song.title}"  # Add 'ytsearch:' prefix
info = ydl.extract_info(search_query, download=False)

# Sort the search results by view count in descending order
sorted_results = sorted(info['entries'], key=lambda x: int(x['view_count']), reverse=True)

# Get the URL of the video with the most views
video_url = sorted_results[0]['webpage_url']

# Open the YouTube video in a web browser
webbrowser.open(video_url)
