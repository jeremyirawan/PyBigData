__author__ = 'ADMIN'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

consumer_key = 'yZTcDgv4wbRFEdfsC4Wh8IY6C'
consumer_secret = 'JBV5C2pVcghMrd9D1wlP9EqERhZmu1lv9MAcRTuITYxNdGooB4'
atoken = '25921543-FtURCQBXj1cHtLiJUjIgQL3RdcEnvWamNbHkCv0Ef'
asecret = '9GuYGsddfH37m9cAqC4R4c2qxPC0SxYfJgIkeoGAoTfx7'

class listener(StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status_code):
        print status_code

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(atoken, asecret)

print "Showing all new tweets from Jakarta, Bekasi, Depok, Bogor, Tangerang and Bandung with the keywords ahok"
twitterStream = Stream(auth, listener())

# Get tweets based on boundary box
#twitterStream.filter(locations=[106.06, -7.29, 108.49, -5.74])

# Get tweets based on a specific word within a tweet
twitterStream.filter(track=["foto menara bca"])