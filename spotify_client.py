import json
import requests

userId = 'mr.redderson'
spotifyToken = 'BQDnBs7zT-nW_O4Y9D5U3grbIme_ri5wNN5y_BmRIkOAE9dgwpHTkhLcbCVdGBbCW2tKf7PKKMisiClAJqcmHBrgkE3lU3DBGt5KQawrIcVZdRkU4AyRZd35Nhct32hBUiG5LOY7fX_1MVyf0clxXfPd'
songInfo = {}
class spotifyClient():
    def __init__(self):
        self.userId = userId
        self.spotifyToken = spotifyToken
        self.songInfo = songInfo

    def createPlaylist(self):
        requestBody = json.dumps({
            "name": "r/listentothis indie songs",
            "description": "A playlist for all the indie r/listentothis songs",
            "public": True
        })

        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.userId)
        response = requests.post(
            query,
            data = requestBody,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotifyToken)
            }
        )

        responseJson = response.json()
        return responseJson["id"]

    def searchSong(self, songName, artist):
        query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20'.format(songName, artist)
        resonse = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotifyToken)
            }
        )

        responseJson = resonse.json
        songs = responseJson["tracks"]["items"]

        uri = songs[0]["uri"]
        return uri

    def addSongtoPlaylist(self, songs):
        
        uris = []
        for i in len(songs):
            self.songInfo = {
                "spotUri": self.searchSong(songs[i, 0], songs[i, 1])
            }
            uris.append(songInfo["spotUri"])

        playlistId = self.createPlaylist()

        requestData = json.dumps(uris)
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlistId)

        response = requests.post(
            query,
            data = requestData,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotifyToken)
            }
        )

        responseJson = response.json()
        return responseJson

