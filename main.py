import tweepy
import sys
import os
from webbrowser import open as site  # For the auth token
import settings

keysPath = "keys.txt"
if len(sys.argv) == 1:
    print("Arguments required!")
    sys.exit()



query = input("enter the test")

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)

auth.secure = True
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

# 
# Construct the API instance
api = tweepy.API(auth)

tweetID = api.update_status("Can you help me out with this query " + str(query)).id


class ReplyListener(tweepy.StreamListener):

    def on_status(self, status):
        # There is a status tweeted tagging the user

        if status.in_reply_to_status_id == tweetID:
            # There was a reply to the  tweet
            parsedAnswer = "".join(status.text.split(" ")[1:])

          
            print(parsedAnswer)  
            api.update_status(
                "@" + status.author.screen_name + " Awesome! Thanks!",
                in_reply_to_status_id=status.id)
            return False
            
        else:
            # They did not reply to the tweet
            return True

    def on_error(self, statusCode):
        # There was a listener error

        print("There was a listener error with the code", statusCode)
        return True

    def on_timeout(self):
        # There was a listener timeout

        print("There was a listener timeout")
        return True

listener = tweepy.streaming.Stream(auth, ReplyListener())
# Listen for a response to the user
listener.filter(track=["@" + api.me().screen_name])
