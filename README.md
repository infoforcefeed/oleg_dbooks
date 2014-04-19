Twitter markov thing for OlegDB.

Running
-------

You'll need to put your sick twitter creds in `local_settings.py`. Then you can
just run `main.py` and it'll tweet for you. If you just want to see some example
output, set `debug=True` in `main.py` and it'll print what it wants to tweet.

What is it?
-----------

This is a twitter bot designed to market OlegDB in the best way we know how: By
generating markov text from the tweets of other database projects! You can see
the corpus in `redone_final.txt`.
