exec(open('util.py').read())
def twitter(inp):
	
import tweepy

	# Twitter API credentials
	consumer_key = 'YOUR_CONSUMER_KEY'
	consumer_secret = 'YOUR_CONSUMER_SECRET'
	access_token = 'YOUR_ACCESS_TOKEN'
	access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

	# Authenticate with Twitter
	auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
	api = tweepy.API(auth)

	# Upload media (image)
	media = api.media_upload("path_to_your_media_file.jpg")

	# Compose tweet with media attached
	tweet_text = "Check out this awesome picture!"
	tweet = api.update_status(status=tweet_text, media_ids=[media.media_id])

	print("Tweet posted successfully!")
	
	
inp = []
twitter(inp)