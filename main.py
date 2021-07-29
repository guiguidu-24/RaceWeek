from google_calendar import get_calendar
from twitter import Twitter
from datetime import datetime
from pytz import timezone
import logging

logging.basicConfig(level=logging.INFO, filename='info.log', format='%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger('main')

logger.info('Start the app')
logger.info('send calendar request')
schedule, names, sessions, locations = get_calendar()
now = datetime.now(tz=timezone('Europe/Paris'))
delta_time = schedule[0] - now

if delta_time.days <= 7:
    logger.debug('Found a race in the week')
    tweet = 'C\'est une semaine de Grand Prix !\n' + names[0] + "\n" + locations[0] + "\n"

    for i in range(len(schedule)):
        if names[i] == names[0]:
            tweet += f"{sessions[i]} : {schedule[i].strftime('%H:%M')}\n"
            continue
        logger.info('Send the tweet')
        Twitter().post(tweet)
        break

logger.info('Close the app\n')
