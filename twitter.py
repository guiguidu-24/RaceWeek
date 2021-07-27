import tweepy


class Twitter:
    def auth(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """
         Se connecte à l'API twitter
         """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api, auth

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self._api, self._auth = self.auth(consumer_key, consumer_secret, access_token, access_token_secret)
        return

    def post(self, content):
        if isinstance(content, str):
            self._api.update_status(content)
            return
        else:
            raise NotImplementedError

