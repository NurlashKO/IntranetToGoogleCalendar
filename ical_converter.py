from datetime import datetime, timedelta
from icalendar import Calendar, Event
from event_parser import get_events
from UEvent import UEvent


calendar = Calendar()
calendar.add('prodid', "-//Google Inc//Google Calendar 70.9054//EN")
calendar.add('version', '2.0')
calendar.add('calscale', 'GREGORIAN')
calendar.add('method', 'PUBLISH')
calendar.add('x-wr-calname', "KBTU Calendar")
calendar.add('NAME', "KBTU Calendar")
calendar.add('x-wr-timezone', "Asia/Almaty")

events = get_events()
for event in events:
    vevent = Event()
    vevent.add('summary', event.title)
    vevent.add('dtstart', event.start)
    vevent.add('dtend', event.end)
    vevent.add('rrule', {'freq': 'weekly'})

    calendar.add_component(vevent)

f = open('events_req.ics', 'wb')
f.write(calendar.to_ical())
f.close()


