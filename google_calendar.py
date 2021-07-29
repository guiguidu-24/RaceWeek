from gcsa.google_calendar import GoogleCalendar
import config_helpers as config
import logging
import gcsa


def get_calendar():
    """
    Get data from the google calendar
    :return: schedule, names, session_types, places
    """

    calendar_id = config.get_data('google_calendar_config/calendar_id.json', 'calendar_id')
    calendar = GoogleCalendar(calendar_id, credentials_path='google_calendar_config/.credentials/credentials.json')
    schedule = []
    names = []
    sessions_type = []
    places = []

    logger = logging.getLogger('google_calendar')

    try:
        events = calendar.get_events(order_by="startTime", single_events=True)
        for event in events:
            schedule.append(event.start)
            places.append(event.location)
            event_detail = event.summary.split(' - ')
            names.append(event_detail[0])
            sessions_type.append(event_detail[1])
    except gcsa:
        logger.error('Cannot reach the Google calendar')
    finally:
        return schedule, names, sessions_type, places



