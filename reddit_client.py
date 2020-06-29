import praw

clientId = 'cGmfkXximckDKg'
clientSecret = 'ht8lTNQewNRvJaiF52IrDsn4T5g'
userAgent = 'ListenToThisAgent'
lim = 100

reddit = praw.Reddit(client_id = clientId, 
                     client_secret = clientSecret, 
                     user_agent = userAgent)

subreddit = reddit.subreddit('listentothis')
submissions = []
songs = []

for submission in subreddit.hot(limit = lim):
    if not submission.stickied:
        submissions.append(submission.title) 

for x in range(len(submissions)):
    if 'Indie' in submissions[x]:
        songs.append(submissions[x])

print(songs[0].split(' - '))
