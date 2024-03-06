from supabase_py import create_client, Client
import os

# Supabase project details

url: str = os.environ.get("SUPABASE_URL","https://ruoaxfttcbppnoyzvvur.supabase.co")
key: str = os.environ.get("SUPABASE_KEY","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1b2F4ZnR0Y2JwcG5veXp2dnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDk2NzUxMzEsImV4cCI6MjAyNTI1MTEzMX0.PLg70dP9slrDuWLhEM5Z8fHiTtHkB_5j8XrddQ08oP8")
if not url or not key:
    raise ValueError("Supabase URL and key must be set in the environment variables.")

supabase: Client = create_client(url, key)

def insert_artist(artistid, name, artistimg, followers):
    data = {
        "artistid": int(artistid),
        "name": name,
        "artistimg": artistimg, 
        "followers": int(followers)
    }
    response = supabase.table("artist").insert(data).execute()  

    if 'status' in response and response['status'] in [200, 201]:
        print('Artist successfully added:', response)
    else:
        print('Failed to add artist. Error:', response)


artist_details = [
    {
        'artistid': 1001,
        'name': 'The Weeknd',
        'artistimg': 'https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/304927810_637294077766997_2634264056233842750_n.jpg?stp=cp6_dst-jpg&_nc_cat=1&ccb=1-7&_nc_sid=5f2048&_nc_ohc=C2dPtT6QxjYAX_hT-sH&_nc_oc=AQlCPrjMxO2x2XLMadZgHJ4HsqY_Ap_9CEZTJbe_83atpDCH6L7q65XBq2kmKHSfL8g&_nc_ht=scontent-ord5-1.xx&oh=00_AfA5o-5yBMKkfnUYPn2xeqVdop8u6cWhrdcSUQUPAJq5gQ&oe=65EC0A4F',
        'followers': 115125414
    },
    {
        'artistid': 1002,
        'name': 'Drake',
        'artistimg': 'https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/288254494_572489184248697_1127704317464671749_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=5f2048&_nc_ohc=VXB8WL0_xU8AX9yxgWR&_nc_ht=scontent-ord5-1.xx&oh=00_AfAu-B7ZyP4iJiClwb6PhsW-Na_mesEjXcNpGh17k5b2Hw&oe=65ED5165',
        'followers': 84249510
    },
    {
        'artistid': 1003,
        'name': 'J.Cole',
        'artistimg': 'https://scontent-ord5-1.xx.fbcdn.net/v/t1.6435-9/185091428_315294279955388_3967566245631882465_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=pxyghyU_O3AAX-JKrZO&_nc_ht=scontent-ord5-1.xx&oh=00_AfCUyqp_m3sH3JfzW0EXasNmPlYqKXWvcdZ0JKvYUVHD3g&oe=660F2E8C',
        'followers': 42760002
    },
    {
        'artistid': 1004,
        'name': 'Bad Bunny',
        'artistimg': 'https://yt3.googleusercontent.com/MH1BdZQE2X6k3WlIns2YlyBNude9Qh3nN0dnG-_zvkM1o5gzBS3upL-C2w6Xm6DysPyg4x8ZHhQ=s900-c-k-c0x00ffffff-no-rj',
        'followers': 69596478
    },
    {
        'artistid': 1005,
        'name': 'Travis Scott',
        'artistimg': 'https://i.ytimg.com/vi/yQORL_z-UsA/maxresdefault.jpg',
        'followers': 65829225
    },
    {
        'artistid': 1006,
        'name': 'Juice WRLD',
        'artistimg': 'https://www.billboard.com/wp-content/uploads/media/Juice-WRLD-bw-press-by-Nabil-Elderkin-2019-billboard-1548.jpg',
        'followers': 31230955
    },
    {
        'artistid': 1007,
        'name': 'Keshi',
        'artistimg': 'https://dynamicmedia.livenationinternational.com/e/p/l/930bdfee-de51-4aa8-a9da-9e5b2679419e.jpg?auto=webp&width=1507.2',
        'followers': 8212869
    },
    {
        'artistid': 1008,
        'name': 'Kanye West',
        'artistimg': 'https://images.impresa.pt/expresso/2022-03-22-kanye.jpg-812c1329',
        'followers': 76919660
    },
    {
        'artistid': 1009,
        'name': 'Kendrick Lamar',
        'artistimg': 'https://static01.nyt.com/images/2017/04/20/magazine/20mag-still-processing-1/20mag-still-processing-1-superJumbo.jpg',
        'followers': 53085390
    },
    {
        'artistid': 1010,
        'name': '21 Savage',
        'artistimg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/21_Savage_2018.jpg/1200px-21_Savage_2018.jpg',
        'followers': 64697072
    },
    {
        'artistid': 1011,
        'name': 'Metro Boomin',
        'artistimg': 'https://i.scdn.co/image/ab6761610000e5ebdf9a1555f53a20087b8c5a5c',
        'followers': 51974826
    }
]

for artist_detail in artist_details:
    insert_artist(**artist_detail)

