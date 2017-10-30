from datetime import datetime, timedelta
from icalendar import Calendar, Event

calendar = Calendar()
calendar.add('prodid', "-//Google Inc//Google Calendar 70.9054//EN")
calendar.add('version', '2.0')
calendar.add('calscale', 'GREGORIAN')
calendar.add('method', 'PUBLISH')
calendar.add('x-wr-calname', "KBTU Calendar")
calendar.add('x-wr-caldesc', "KBTU Calendar")
calendar.add('NAME', "KBTU Calendar")
calendar.add('x-wr-timezone', "Asia/Almaty")

'''
vevent = Event()

vevent.add('summary', "test summary")
vevent.add('dtstart', datetime.now())
vevent.add('dtend', datetime.now() + timedelta(hours=3))

calendar.add_component(vevent)
'''
f = open('empty_test.ics', 'wb')
f.write(calendar.to_ical())
f.close()


