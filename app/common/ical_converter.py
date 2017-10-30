from datetime import datetime, timedelta
from icalendar import Calendar, Event
from .event_parser import get_events
from .UEvent import UEvent

def events_to_ical(events):
    calendar = Calendar()
    calendar.add('prodid', "-//NurlashKO Inc.//KBTU to Calendar//EN")
    calendar.add('version', '2.0')
    calendar.add('calscale', 'GREGORIAN')
    calendar.add('method', 'PUBLISH')
    calendar.add('x-wr-calname', "KBTU Calendar")
    calendar.add('NAME', "KBTU Calendar")
    calendar.add('x-wr-timezone', "Asia/Almaty")

    for event in events:
        vevent = Event()
        vevent.add('summary', event.title)
        vevent.add('dtstart', event.start)
        vevent.add('dtend', event.end)
        vevent.add('rrule', {'freq': 'weekly'})

        calendar.add_component(vevent)

    return calendar.to_ical()
