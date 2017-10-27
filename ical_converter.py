from datetime import datetime, timedelta
from icalendar import Calendar, Event

calendar = Calendar()
calendar.add('prodid', "KBTU Calendar")
calendar.add('version', '2.0')
calendar.add('summary', 'Test calendar name. Kind a long, test test.')
calendar.add('x-wr-timezone', "Asia/Kazakhstan")
calendar.add('method', 'publish')

vevent = Event()

vevent.add('summary', "test summary")
vevent.add('dtstart', datetime.now())
vevent.add('dtend', datetime.now() + timedelta(hours=3))

calendar.add_component(vevent)

f = open('example.ics', 'wb')
f.write(calendar.to_ical())
f.close()


