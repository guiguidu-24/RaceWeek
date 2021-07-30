from google_calendar import get_calendar
from twitter import Twitter
from datetime import datetime
from pytz import timezone
import logging


def run():
    logging.basicConfig(level=logging.INFO, filename='info.log', format='%(levelname)s - %(asctime)s - %(message)s')
    logger = logging.getLogger('main')

    logger.info('Start the app')
    logger.info('send calendar request')
    schedule, names, sessions, locations = get_calendar()
    now = datetime.now(tz=timezone('Europe/Paris'))
    delta_time = schedule[0] - now

    if delta_time.days <= 7:
        logger.debug('Found a race in the week')
        last_tweet_name = ""
        with open("tweet_history.txt", 'r', encoding='utf-8') as history:
            last_tweet_name = history.read().split('\n')[-2]

        if last_tweet_name != names[0]:
            logger.debug('Found a race to share')
            tweet = 'C\'est une semaine de Grand Prix !\n' + names[0] + "\n" + locations[0] + "\n"
            for i in range(len(schedule)):
                if names[i] == names[0]:
                    tweet += f"{sessions[i]} : {schedule[i].strftime('%H:%M')}\n"
                    continue
                logger.info('Send the tweet')
                Twitter().post(tweet)
                with open('tweet_history.txt', 'a', encoding='utf-8') as tweet_history:
                    tweet_history.write(f"{names[0]}\n")
                break
        else:
            logger.warning('The race have already been posted')

    logger.info('Close the app\n')


if __name__ == '__main__':
    run()
aw