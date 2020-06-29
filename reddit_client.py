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
        pass

    def getSongs():
        for submission in subreddit.hot(limit = lim):
            if not submission.stickied:
                submissions.append(submission.title) 

        for x in range(len(submissions)):
            if 'Indie' in submissions[x]:
                if ' - ' in submissions[x]:
                    song = submissions[x].split(' - ')
                elif ' -- ' in submissions[x]:
                    song = submissions[x].split(' -- ')
                artist = song[0]
                song = song[1].split(' [')
                songs.append([song[0], artist])

        return songs



print(redditClient.getSongs())
        


