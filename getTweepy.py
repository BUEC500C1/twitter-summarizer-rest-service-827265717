import tweepy
import re
import os
import os.path
import configparser

def tweepy_get(keyword):
	config = configparser.ConfigParser()
	config.read('keys')
	auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
	auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())  
	
	# get author API
	api = tweepy.API(auth)

	search_results = api.user_timeline(keyword)
	num = 0
	highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
	for tweet in search_results:
		gap = '\n'
		tweet_list = list(tweet.text)
		list_num = 0
		for i in range(len(tweet_list)):
			if (i % 50) == 0:
				tweet_list.insert(i,gap)
		tweet.text = ''.join(tweet_list)
		print(tweet.text)

		num += 1
		text_noem = highpoints.sub('--emoji--', tweet.text)
		text_noem = text_noem.encode('utf8')

		fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
		image = Image.open('origin.png')
		draw = ImageDraw.Draw(image)
		draw.text((100,200), tweet.text, font=fnt, fill= "white")
		filename = "img/" + keyword + str(num) + ".png"
		image.save(filename)
