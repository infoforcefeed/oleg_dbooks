#!/usr/bin/env python2
from local_settings import consumer_key, consumer_secret, access_token_key,\
        access_token_secret
import twitter

debug = True

def main():
    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    markov_text = None

    if debug is False:
        status = api.PostUpdate('Beware I live.')
    else:
        print "Want to post: {}".format(markov_text)

if __name__ == '__main__':
    main()
