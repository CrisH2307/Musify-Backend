from supabase_py import create_client, Client
import os

# Supabase project details

url: str = os.environ.get("SUPABASE_URL","https://ruoaxfttcbppnoyzvvur.supabase.co")
key: str = os.environ.get("SUPABASE_KEY","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8")
if not url or not key:
    raise ValueError("Supabase URL and key must be set in the environment variables.")

supabase: Client = create_client(url, key)

def insert_album(albumid, artistid, albumtitle, albumimg, date):
    data = {
        "albumid": int(albumid),
        "artistid": int(artistid),
        "albumtitle": albumtitle,
        "albumimg" : albumimg,
        "date": int(date),
    }
    response = supabase.table("album").insert(data).execute()  

    if 'status' in response and response['status'] in [200, 201]:
        print('Artist successfully added:', response)
    else:
        print('Failed to add artist. Error:', response)

album_detail = [
    {
        "albumid": 100101,
        "artistid": 1001,
        "albumtitle": "Dawn FM",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/b/b9/The_Weeknd_-_Dawn_FM.png",
        "date": 2022
    },
    {
        "albumid": 100102,
        "artistid": 1001,
        "albumtitle": "After Hours",
        "albumimg": "https://ratedrnb.com/cdn/2020/02/the-weeknd-after-hours-album-cover.jpg",
        "date": 2020
    },
    {
        "albumid": 100103,
        "artistid": 1001,
        "albumtitle": "My Dear Melancholy",
        "albumimg": "https://lastfm.freetls.fastly.net/i/u/ar0/6498660830a525a64f6a78bf94a2ec58.jpg",
        "date": 2018
    },
    {
        "albumid": 100104,
        "artistid": 1001,
        "albumtitle": "Starboy",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/3/39/The_Weeknd_-_Starboy.png",
        "date": 2016
    },
    {
        "albumid": 100105,
        "artistid": 1001,
        "albumtitle": "Beauty Behind The Madness",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/b/bd/The_Weeknd_-_Beauty_Behind_the_Madness.png",
        "date": 2015
    },
    {
        "albumid": 100106,
        "artistid": 1001,
        "albumtitle": "Kiss Land",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/e/ed/The_Weeknd_-_Kiss_Land.png",
        "date": 2013
    },
    {
        "albumid": 100107,
        "artistid": 1001,
        "albumtitle": "Trilogy",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/9/96/The_Weeknd_-_Trilogy.png",
        "date": 2011
    },
    {
        "albumid": 100201,
        "artistid": 1002,
        "albumtitle": "For All The Dogs",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/0/05/Drake_-_For_All_The_Dogs.png",
        "date": 2023
    },
    {
        "albumid": 100202,
        "artistid": 1002,
        "albumtitle": "Rich Flex",
        "albumimg": "https://media.pitchfork.com/photos/636509072145df8a03cc87b0/master/pass/Drake.jpg",
        "date": 2022
    },
    
]

for each_album in album_detail:
    insert_album(**each_album)