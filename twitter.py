import tweepy
import config_helpers


class Twitter:
    def auth(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
         Se connecte à l'API twitter
         """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api, auth

    def __init__(self,
                 consumer_key: str = None,
                 consumer_secret: str = None,
                 access_token: str = None,
                 access_token_secret: str = None):
        if consumer_key or consumer_secret or access_token or access_token_secret is not None:
            self._api, self._auth = self.auth(consumer_key, consumer_secret, access_token, access_token_secret)
            return
        else:
            # get the different tokens for the authentication
            tokens = config_helpers.get_json_data('twitter_tokens.json')
            consumer_tokens = tokens['consumer']
            access_tokens = tokens['access']
            self.__init__(consumer_tokens['key'],
                          consumer_tokens['secret'],
                          access_tokens['token'],
                          access_tokens['secret'])
            return

    def post(self, content):
        if isinstance(content, str):
            self._api.update_status(content)
            return
        else:
            raise NotImplementedError

