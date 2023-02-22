from datetime import timedelta, datetime
import time

today = datetime.today()


# Calculate difference in seconds

def printDiffInSeconds(first: datetime, second: datetime) -> None:
    firstSeconds = time.mktime(first.timetuple())
    secondSeconds = time.mktime(second.timetuple())
    print(secondSeconds - firstSeconds)


printDiffInSeconds(today, today + timedelta(days = 2))