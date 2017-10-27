from datetime import date
from icalendar import Calendar, Event

calendar = Calendar()
calendar.add('prodid', "KBTU Calendar")
calendar.add('version', '2.0')
calendar.add('method', 'publish')

vevent = Event()

vevent.add('summary', "test summary")
vevent.add('dtstart', date.today())

calendar.add_component(vevent)

f = open('example.ics', 'wb')
f.write(calendar.to_ical())
f.close()


