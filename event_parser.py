from bs4 import BeautifulSoup
from UEvent import UEvent

def get_schedule():
    html_doc = open('test.html', 'r').read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.find_all('tr')

def get_week_days(schedule_heading):
    return list(map(lambda x: x.string, schedule_heading.find_all('span')))

def get_events():
    events = []
    schedule = get_schedule()
    week_days = get_week_days(schedule[0])
    schedule = schedule[1:-1] # Remove the first and last rows. They're used only for markup.
    cur_time = [0] * len(week_days)
    time_on_schedule = 420 # 07:00

    for schedule_row in schedule:
        if (len(schedule_row.find_all('th')) == 2):
            # Met left side time marker.
            time_on_schedule += 60
            continue
        day = 0
        for time_frame in schedule_row.find_all('td'):
            while (cur_time[day] > time_on_schedule):
                day += 1
            event_duration = int(time_frame['rowspan']) * 30
            if ('class' in time_frame.attrs):
                events.append(UEvent(            \
                    time_frame.span.text,       \
                    time_on_schedule,           \
                    event_duration))
            cur_time[day] = time_on_schedule + event_duration
    return events

events = get_events()
for event in events:
    print(event.title, event.start, event.duration)

