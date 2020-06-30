from reddit_client import redditClient
from spotify_client import spotifyClient

def run():
    #Get song list from reddit

    reddit_client = redditClient()
    
    songs = reddit_client.getSongs()
    #Spotify shit with song list
    spotify_client = spotifyClient()

    spotify_client.addSongtoPlaylist(songs)


if __name__ == "__main__":
    run()