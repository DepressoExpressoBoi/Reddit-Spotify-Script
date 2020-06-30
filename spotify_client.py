import json
import requests

userId = 'mr.redderson'
spotifyToken = 'BQBflb_3f4DmS5eaYBWRD3KU3hd9aW5Mk0KYNWUTAvUOsXjt3b73njlD5jq0gTo4atZ8M_HdKDopLQfA-TlyvDzPUCmY9IyfL3yfywjwnyhS5E5X6dA8getMa_c08CCAZ9PpeA_nrZ1GFaLAi3q2bcYk54fxvUDSrLO1NTZ-IXLRgp7R7vX_TbcQLDjkJ-hest0tNsg5GZPRAEvwrhs'
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
        query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=5'.format(songName, artist)
        response = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotifyToken)
            }
        )

        responseJson = response.json()
        print(responseJson)
        track = responseJson["tracks"]["items"]
        

        if len(track) > 0:
            uri = track[0]["uri"]
            return uri
        

    def addSongtoPlaylist(self, songs):
        
        uris = []
        for x in range(len(songs)):
            self.songInfo = {
                "spotUri": self.searchSong(songs[x][0], songs[x][1])
            }
            uris.append(self.songInfo["spotUri"])

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

