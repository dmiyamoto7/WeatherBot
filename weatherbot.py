import requests
import praw
import time
import re

keyphrase = '!forecast '

print("Authenticating...")
reddit = praw.Reddit(client_id=[REDACTED],
					 client_secret=[REDACTED],
					 username=[REDACTED],
					 password=[REDACTED],
					 user_agent=[REDACTED])
print("Authenticated as {}".format(reddit.user.me()))
print("Starting comment stream")

subreddit = reddit.subreddit('test')

def get_weather(city):
	cityAdjusted = city.lower()
	api_address = "http://api.openweathermap.org/data/2.5/weather?appid=4256f4707c26e6af9a69272f21a57a67&units=imperial&q={}".format(cityAdjusted)
	weatherType = requests.get(api_address).json()['weather'][0]['main']
	weatherTemp = requests.get(api_address).json()['main']['temp']
	weatherString = "In {}, the weather is currently: {}. The temperature is {} degrees F.".format(cityAdjusted.capitalize(),weatherType,weatherTemp)
	return weatherString


for comment in subreddit.stream.comments():
	if comment.saved:
		continue
	if keyphrase in comment.body:
		comment.save()
		word = comment.body.replace(keyphrase,'')
		if ' ' in word:
			word.replace(' ','+')
			comment.reply(get_weather(word))
		else:	
			comment.reply(get_weather(word))










