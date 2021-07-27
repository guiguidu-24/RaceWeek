import tweepy


def auth():
    """
    Se connecte à l'API twitter
    """
    # clés de l'application
    consumer_key = "xxxxxxxxxxx"
    consumer_secret = "xxxxxxxxxxxx"

    # le acces_token est le token de l'application twitter que nous avons créée précédement
    access_token = "xxxxxxxx"
    access_token_secret = "xxxxxxxxxxx"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api, auth