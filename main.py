#!/usr/bin/env python2
from local_settings import consumer_key, consumer_secret, access_token_key,\
        access_token_secret
from markov import MarkovDict
from bs4 import BeautifulSoup
import twitter

debug = False

def main():
    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    text = open("redone_final.txt")
    filetext = text.read()
    text.close()

    mdict = MarkovDict(filetext, int(2), 122)
    mdict.read_text()
    markov_text = mdict.output_text()
    for x in ["redis", "mariadb", "mysql", "postgresql", "couchdb"]:
        markov_text = markov_text.lower().replace(x, "olegdb")

    if debug is False:
        status = api.PostUpdate(markov_text)
    else:
        print "{}".format(markov_text)

if __name__ == '__main__':
    main()
