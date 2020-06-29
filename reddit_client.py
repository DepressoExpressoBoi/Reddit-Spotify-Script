import praw
    
clientId = 'cGmfkXximckDKg'
clientSecret = 'ht8lTNQewNRvJaiF52IrDsn4T5g'
userAgent = 'ListenToThisAgent'

reddit = praw.Reddit(clientId, clientSecret, userAgent)
subreddit = reddit.subreddit('listentothis')

for submission in subreddit.hot(limit = 1):
    print(submission.title) 
