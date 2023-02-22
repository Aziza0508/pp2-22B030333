from datetime import timedelta, datetime
import time

today = datetime.today()


# Substract days

def printDaysAgo(days: int) -> None:
    days_ago = today - timedelta(days = days)

    print(days_ago)

printDaysAgo(5)
