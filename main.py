import lyricsgenius
import random
import tweepy

keys = ["have been defined in environment variables"]

genius = lyricsgenius.Genius('genius_client_access_token')
artist = genius.search_artist("Fleetwood Mac")

all_songs = [song for song in artist.songs]

def get_raw_lyrics():
    genius_client_access_token = "genius_client_access_token"
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "Fleetwood Mac").lyrics
    song = random_song_title.upper()
    return lyrics, song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)
    return tweet



