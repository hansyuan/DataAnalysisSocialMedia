#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "1360300398-fc52kSNY76KDR5yYBkeUCUfIUBMXtwL78Myp2l2"
access_token_secret = "pEUYfEiDcdZx9BxZFcaEhIrsvLbn9hHcbQSfIHakxrciJ"
consumer_key = "UOkQIz5COq9Dv3QmmmSZN06Gx"
consumer_secret = "Duts0Tq1d7YofMUhzV4uW6hlsGjlEWqoBXzcafMgVPXfbA5Mey"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = tweepy.API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    
    allTweets = tweepy.Cursor(api.search, q='Trump', geocode="34.0201,-118.6919,1000km").items(10000)

    for tweet in allTweets:
        print(tweet.text.encode('utf-8'),"\n\n")