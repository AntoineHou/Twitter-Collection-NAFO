import tweepy 
import json
import time

# Twitter API credentials
API_KEY = [""]
API_KEY_SECRET = [""]
BEARER_TOKEN = [""]
ACCESSEN_TOKEN = [""]
TOKEN_SECRET = [""]
HASHTAG = "#NAFO"

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.file = open('NAFO_{}.json'.format(str(time.strftime("%Y%m%d-%H%M%S"))), 'w', encoding='utf-16')

    def on_data(self, data):
        self.counter += 1
        if self.counter > 1000:
            self.file.close()
            self.file = open('NAFO_{}.json'.format(time.strftime("%Y%m%d-%H%M%S")), 'w', encoding='utf-16')
            self.counter = 0 
        else:
            self.file.write(data + '\n')
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
        else : 
            print('Encountered error with status code:', status_code)
        return True  

    def on_timeout(self):
        print('Timeout...')
        return True  

def main():
    CREDENTIALS_COUNTER = 0
    while True:
        try:
            auth = tweepy.OAuthHandler(API_KEY[CREDENTIALS_COUNTER], API_KEY_SECRET[CREDENTIALS_COUNTER])
            auth.set_access_token(ACCESSEN_TOKEN[CREDENTIALS_COUNTER], TOKEN_SECRET[CREDENTIALS_COUNTER])
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
            myStream.filter(track=[HASHTAG])
        except:
            CREDENTIALS_COUNTER += 1
            if CREDENTIALS_COUNTER == len(API_KEY):
                CREDENTIALS_COUNTER = 0
            continue

if __name__ == '__main__':
    main()
