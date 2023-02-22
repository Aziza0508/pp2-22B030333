from datetime import timedelta, datetime
import time

today = datetime.today()

# microseconds to zero

def dropMicroseconds(dt) -> None:
    print(dt.replace(microsecond = 0))


dropMicroseconds(today)