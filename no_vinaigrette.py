from datetime import timedelta
from random import randrange
from datetime import datetime


def random_date(start, end):
    delta = end - start
    int_delta = delta.days
    random_day = randrange(int_delta)
    return (start + timedelta(days=random_day)).date()


def get_date_day(d):
    if 2 == d.weekday():
        return "אין לי ויניגרט"
    return d


if __name__ == '__main__':
    minDate = input("Enter the minimum date: ")
    maxDate = input("Enter the maximum date: ")
    d1 = datetime.strptime(minDate, '%Y-%m-%d')
    d2 = datetime.strptime(maxDate, '%Y-%m-%d')
    print(get_date_day(random_date(d1, d2)))

