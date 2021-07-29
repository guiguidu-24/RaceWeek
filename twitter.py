from tweepy import OAuthHandler, API, error
import config_helpers as config
import logging


class Twitter:

    def auth(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        """
         Se connecte à l'API twitter
         """

        self.logger.debug('Set the authentication tokens')

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = API(auth)
        return api, auth

    def __init__(self,
                 path: str = 'twitter_tokens.json'):
        """
        Default constructor
        :param path: The relative path of the file that store the twitter credentials
        """

        self.logger = logging.getLogger('twitter')
        self.logger.debug('Read the authentication twitter file')

        # get the different tokens for the authentication
        tokens = config.get_dict_data(path)
        consumer_tokens = tokens['consumer']
        access_tokens = tokens['access']
        self._api, self._auth = self.auth(consumer_tokens['key'],
                                          consumer_tokens['secret'],
                                          access_tokens['token'],
                                          access_tokens['secret'])
        return

    def post(self, content):

        """
        Post a status on Twitter
        :param content: The content to post
        """

        if isinstance(content, str):
            try:
                self._api.update_status(content)
            except error.TweepError as e:
                self.logger.warning(e.reason)
            return
        else:
            raise NotImplementedError
