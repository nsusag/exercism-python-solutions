from datetime import date
from leap import leap_year

class MeetupDayException(Exception): pass

def meetup(year, month, week, day_of_week):
    if day_of_week == "Monday":
        num_day = 1
    elif day_of_week == "Tuesday":
        num_day = 2
    elif day_of_week == "Wednesday":
        num_day = 3
    elif day_of_week == "Thursday":
        num_day = 4
    elif day_of_week == "Friday":
        num_day = 5
    elif day_of_week == "Saturday":
        num_day = 6
    elif day_of_week == "Sunday":
        num_day = 7
    if week == "1st":
        for i in range(1, 8):
            if date(year, month, i).isoweekday() == num_day:
                return date(year, month, i)
    elif week == "2nd":
        for i in range(8, 15):
            if date(year, month, i).isoweekday() == num_day:
                return date(year, month, i)
    elif week == "3rd":
        for i in range(15, 22):
            if date(year, month, i).isoweekday() == num_day:
                return date(year, month, i)
    elif week == "4th":
        for i in range(22, 29):
            if date(year, month, i).isoweekday() == num_day:
                return date(year, month, i)
    elif week == "5th":
        if month in [1, 3, 5, 7, 8, 10, 12]:  
            for i in range(29, 32):
                if date(year, month, i).isoweekday() == num_day:
                    return date(year, month, i)
        elif month in [4, 6, 9, 11]:  
            for i in range(29, 31):
                if date(year, month, i).isoweekday() == num_day:
                    return date(year, month, i)
        elif month == 2:
            if leap_year(year):
                if date(year, month, 29).isoweekday() == num_day:
                    return date(year, month, 29)
    elif week == "teenth":
        for i in range(13, 20):
            if date(year, month, i).isoweekday() == num_day:
                return date(year, month, i)
    elif week == "last":
        if month in [1, 3, 5, 7, 8, 10, 12]:  
            for i in range(25, 32):
                if date(year, month, i).isoweekday() == num_day:
                    return date(year, month, i)
        elif month in [4, 6, 9, 11]:  
            for i in range(24, 31):
                if date(year, month, i).isoweekday() == num_day:
                    return date(year, month, i)
        elif month == 2:
            if leap_year(year):
                for i in range(23, 30):
                    if date(year, month, i).isoweekday() == num_day:
                        return date(year, month, i)
            else:
                for i in range(22, 29):
                    if date(year, month, i).isoweekday() == num_day:
                        return date(year, month, i)
    raise MeetupDayException("That day does not exist.") 


