from datetime import timedelta, datetime
import time

today = datetime.today()


# Yesterday, today, tomorrow

def printThreeDays() -> None:
    yesterday, tomorrow = today - timedelta(days = 1), today + timedelta(days = 1)

    print(f"Yesterday: {yesterday}\n Today: {today}\n Tomorrow: {tomorrow}")

printThreeDays()