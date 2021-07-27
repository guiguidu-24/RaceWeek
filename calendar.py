from gcsa.google_calendar import GoogleCalendar
import config_helpers
from datetime import datetime

calendarId = config_helpers.get_data('google_calendar_config/calendar_id.json', 'calendar_id')
calendar = GoogleCalendar(calendarId, credentials_path='google_calendar_config/.credentials/credentials.json')
for event in calendar:
    print(event)


def get_calendar():
    calendarId = config_helpers.get_data('google_calendar_config/calendar_id.json', 'calendar_id')
    calendar = GoogleCalendar(calendarId, credentials_path='google_calendar_config/.credentials/credentials.json')
    schedule = []
    names = sessions_type = []

    for event in calendar.get_events(order_by="startTime", single_events=True):
        event_detail = str(event).split(str=' - ')
        schedule.append(datetime.fromisoformat(event_detail[0]))
        names.append(event_detail[1])
        sessions_type.append(event_detail[2])

    return schedule, names, sessions_type
