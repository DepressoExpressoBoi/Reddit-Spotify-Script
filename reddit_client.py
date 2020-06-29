import praw

clientId = 'cGmfkXximckDKg'
clientSecret = 'ht8lTNQewNRvJaiF52IrDsn4T5g'
userAgent = 'ListenToThisAgent'

reddit = praw.Reddit(clientId, clientSecret, userAgent)

class redditClient(object):
    def __init__(self):
        pass

    def getSubbreddit(self):
        self.subreddit = reddit.subreddit('listentothis')

    def getGenres(self):
        pass

    def getSongs(self):
        pass

    def getArtists(self):
        pass