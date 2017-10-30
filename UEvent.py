from datetime import datetime, date, timedelta
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
class UEvent:
    def __init__(self, title, week_delta, start_time_delta, duration):
        today = date.today()
        week_start = today - timedelta(days=-today.weekday(), weeks = 1)
        self.title = title.strip()
        self.weekday = week_days.index(week_delta)
        self.start =                                        \
              week_start                                    \
            + timedelta(days=week_days.index(week_delta))   \
            + timedelta(minutes=start_time_delta)
        self.end = self.start + timedelta(minutes=duration)

