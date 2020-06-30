import praw

clientId = 'cGmfkXximckDKg'
clientSecret = 'ht8lTNQewNRvJaiF52IrDsn4T5g'
userAgent = 'ListenToThisAgent'
lim = 100

reddit = praw.Reddit(client_id = clientId, client_secret = clientSecret, user_agent = userAgent)

subreddit = reddit.subreddit('listentothis')
submissions = []
songs = []

class redditClient():
    def __init__(self):
        self.subreddit = subreddit
        self.submissions = submissions
        self.songs = songs

    def getSongs(self):
        for submission in self.subreddit.hot(limit = lim):
            if not submission.stickied:
                self.submissions.append(submission.title) 

        for x in range(len(self.submissions)):
            if 'Indie' in self.submissions[x]:
                if ' - ' in self.submissions[x]:
                    song = self.submissions[x].split(' - ')
                elif ' -- ' in self.submissions[x]:
                    song = self.submissions[x].split(' -- ')
                artist = song[0]
                song = song[1].split(' [')
                self.songs.append([song[0].replace(" ", ""), artist])

        return songs

        


