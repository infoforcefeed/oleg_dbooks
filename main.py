#!/usr/bin/env python2
from local_settings import consumer_key, consumer_secret, access_token_key,\
        access_token_secret
import twitter

def main():
    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    #status = api.PostUpdate('Beware I live.')

if __name__ == '__main__':
    main()
