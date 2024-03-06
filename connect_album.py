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
    # The Weeknd
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
    # Drake
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
    {
        "albumid": 100203,
        "artistid": 1002,
        "albumtitle": "Views",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/a/af/Drake_-_Views_cover.jpg",
        "date": 2021
    },

    #J cole
    {
        "albumid": 100301,
        "artistid": 1003,
        "albumtitle": "The Off-Season",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/7/7d/TheOff-Season.jpeg",
        "date": 2021
    },
    {
        "albumid": 100302,
        "artistid": 1003,
        "albumtitle": "KOD",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/d/d3/JColeKOD.jpg?20180420211753",
        "date": 2018
    },
    {
        "albumid": 100303,
        "artistid": 1003,
        "albumtitle": "2014 Forest Hills Drive",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/2/2a/2014ForestHillsDrive.jpg",
        "date": 2014
    },
    #Bad Bunny
    {
        "albumid": 100401,
        "artistid": 1004,
        "albumtitle": "YHLQMDLG",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/3/3f/Bad_Bunny_-_Yhlqmdlg.png",
        "date": 2020
    },
    {
        "albumid": 100402,
        "artistid": 1004,
        "albumtitle": "El Último Tour Del Mundo",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/a/ae/Bad_Bunny_-_El_%C3%9Altimo_Tour_del_Mundo.png",
        "date": 2020
    },
    {
        "albumid": 100403,
        "artistid": 1004,
        "albumtitle": "X 100pre",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/e/e7/X100pre.jpg",
        "date": 2018
    },
    #travis scott
    {
        "albumid": 100501,
        "artistid": 1005,
        "albumtitle": "Rodeo",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/7/7b/Rodeo_-_Album_Cover_by_Travis_Scott%2C_September_4%2C_2015.jpg",
        "date": 2015
    },
    {
        "albumid": 1005002,  # Ensure this is a unique identifier
        "artistid": 1005,  # Travis Scott's artist ID
        "albumtitle": "ASTROWORLD",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/4/4b/Travis_Scott_-_Astroworld.png",  # Replace with the actual link to the album cover image
        "date": 2018  # The release year
    },
    {
        "albumid": 1005003,
        "artistid": 1005,
        "albumtitle": "Birds in the Trap Sing McKnight",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/6/61/Travis_Scott_-_Birds_in_the_Trap_Sing_McKnight.png",  # Replace with the actual link to the album cover image
        "date": 2016
    },
    #Juice WRLD
    {
        "albumid": 100601,
        "artistid": 1006,
        "albumtitle": "Legends Never Die",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/f/f6/Juice_Wrld_-_Legends_Never_Die.png",
        "date": 2020
    },
    {
        "albumid": 1006002,
        "artistid": 1006,
        "albumtitle": "Death Race for Love",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/0/04/Juice_Wrld_-_Death_Race_for_Love.png",
        "date": 2019
    },
    {
        "albumid": 1006003,
        "artistid": 1006,
        "albumtitle": "Goodbye & Good Riddance",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/8/86/Goodbye_%26_Good_Riddance_Album_Cover.jpg",
        "date": 2018
    },
    #Keshi
     {
        "albumid": 1007001,  
        "artistid": 1007,  
        "albumtitle": "Bandaids",
        "albumimg": "https://t2.genius.com/unsafe/385x385/https%3A%2F%2Fimages.genius.com%2F785964fb301c7b83e9c734b45a60c0db.758x758x1.jpg",
        "date": 2020 
    },
    {
        "albumid": 1007002,
        "artistid": 1007,
        "albumtitle": "Skeletons",
        "albumimg": "https://t2.genius.com/unsafe/600x600/https%3A%2F%2Fimages.genius.com%2F87cac3cb929a14ca907df61abbb75761.1000x1000x1.jpg",
        "date": 2019
    },
    {
        "albumid": 1007003,
        "artistid": 1007,
        "albumtitle": "Always",
        "albumimg": "https://t2.genius.com/unsafe/385x385/https%3A%2F%2Fimages.genius.com%2F826dcfc2835a2c0dbd45aa62fd65f1a7.575x575x1.jpg",
        "date": 2018
    },
    #kanye west
     {
        "albumid": 100801,  
        "artistid": 1008, 
        "albumtitle": "Donda",
        "albumimg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Almost_black_square_020305.png/440px-Almost_black_square_020305.png",
        "date": 2021
    },
    {
        "albumid": 100802,
        "artistid": 1008,
        "albumtitle": "Jesus is King",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/a/a4/Kanye_West_-_Jesus_Is_King.png",
        "date": 2019
    },
    {
        "albumid": 100803,
        "artistid": 1008,
        "albumtitle": "Ye",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/7/74/Ye_album_cover.jpg",
        "date": 2018
    }, 
    {
        "albumid": 100804,
        "artistid": 1008,
        "albumtitle": "VULTURE 1",
        "albumimg": "https://t2.genius.com/unsafe/600x600/https%3A%2F%2Fimages.genius.com%2F5f9a010dd8b351b82c9340044228bd8d.1000x1000x1.png",
        "date": 2024
    },
    #Kendrick Lamar
    {
        "albumid": 100901,
        "artistid": 1009,
        "albumtitle": "DAMN.",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/5/51/Kendrick_Lamar_-_Damn.png",
        "date": 2017
    },
    {
        "albumid": 100902,
        "artistid": 1009,
        "albumtitle": "To Pimp a Butterfly",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/f/f6/Kendrick_Lamar_-_To_Pimp_a_Butterfly.png",
        "date": 2015
    },
    {
        "albumid": 100903,
        "artistid": 1009,
        "albumtitle": "good kid, m.A.A.d city",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/9/93/KendrickGKMC.jpg",
        "date": 2012
    },
    #21 Savage
    {
        "albumid": 101001,
        "artistid": 1010,
        "albumtitle": "I Am > I Was",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/3/36/21_Savage_%E2%80%93_I_Am_Greater_Than_I_Was.png",
        "date": 2018
    },
    {
        "albumid": 101002,
        "artistid": 1010,
        "albumtitle": "Savage Mode II",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/0/08/21_Savage_and_Metro_Boomin_-_Savage_Mode_II.png",
        "date": 2020
    },
    {
        "albumid": 101003,
        "artistid": 1010,
        "albumtitle": "Issa Album",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/1/12/21_Savage_-_Issa_Album.png",
        "date": 2017
    },
    {
        "albumid": 101004,
        "artistid": 1010,
        "albumtitle": "American Dream",
        "albumimg": "https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/de/82/b9/de82b98d-56a1-e27b-10ea-46964f4585e4/196871714549.jpg/1200x1200bb.jpg",
        "date": 2024
    },
    #Metro Boomin
    {
        "albumid": 101101,
        "artistid": 1011,
        "albumtitle": "Not All Heroes Wear Capes",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/2/28/Metro_Boomin_%E2%80%93_Not_All_Heroes_Wear_Capes.png",
        "date": 2018
    },
    {
        "albumid": 101102,
        "artistid": 1011,
        "albumtitle": "Savage Mode",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/6/6e/21_Savage_and_Metro_Boomin_-_Savage_Mode.png",
        "date": 2016
    },
    {
        "albumid": 101103,
        "artistid": 1011,
        "albumtitle": "Double or Nothing",
        "albumimg": "https://upload.wikimedia.org/wikipedia/en/6/65/Big_Sean_and_Metro_Boomin_%E2%80%93_Double_or_Nothing.png",
        "date": 2017
    },
    {
        "albumid": 101104,
        "artistid": 1011,
        "albumtitle": "HEROES & VILLANS",
        "albumimg": "https://i.scdn.co/image/ab67616d0000b273c4fee55d7b51479627c31f89",
        "date": 2022
    }
]

for each_album in album_detail:
    insert_album(**each_album)