# tweet-search
==========

Twitter Search is a simple utility that takes advantage of the Twitter API. You pass the script whatever query you have and it'll broadcast the tweet.
When someone replies, it will print the answer to the console and also send out a thank you tweet in return.

Setup
-----
Ensure you have the `tweepy` module installed:

    pip install tweepy

Fill the API_KEY and API_SECRET with your own key in settings.py.

Example
-------

```shell
$ python main.py 
Best place to have frankie in andheri east?
```
