import datetime

from pytz import timezone, utc

tz_germany = timezone("Europe/Berlin")


class Task:

    # Creates a Task
    def __init__(self, number, description, started, finished=None):
        self.number = number
        self.description = description
        self.started = utc.localize(started).astimezone(tz_germany)
        self.finished = utc.localize(finished).astimezone(tz_germany) if finished else None

    def is_finished(self):
        return False if not self.finished else True

    def date_from_timestamp(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp, tz_germany) if timestamp else None
