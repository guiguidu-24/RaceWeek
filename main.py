from twitter import Twitter
import json


def get_json_data(path):
    with open(path, 'r') as stream_file:
        data = stream_file.read()
    return json.loads(data)


# get the different tokens for the authentication
tokens = get_json_data('twitter_tokens.json')
consumer_tokens = tokens['consumer']
access_tokens = tokens['access']

twitter = Twitter(consumer_tokens['key'], consumer_tokens['secret'], access_tokens['token'], access_tokens['secret'])

twitter.post("Hello from python")
