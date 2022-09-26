import datetime

def add(moment):
    gigasecond = 1000000000
    td = datetime.timedelta((gigasecond // 86400), (gigasecond - (86400 * (gigasecond // 86400))))
    return moment + td
