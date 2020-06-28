import tweepy

consumer_key = "your-consumer-key-here"
consumer_secret = "your-consumer-secret-here"
access_token = "your-access-token-here"
access_token_secret = "your-access-token-secret-here"

# config twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for page in tweepy.Cursor(api.search, q="indonesia", count=10, result_type="recent").pages(100):
    for d in page:
        print("{}: {}\ncreated: {}".format(d.user.screen_name, d.text, d.created_at))
        print("-" * 50)
