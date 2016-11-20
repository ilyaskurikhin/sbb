import datetime

def datetime_from_text(text_date):
    try:
        day = int(text_date[0:2])
        month = int(text_date[3:5])
        year = int(text_date[6:10])
        hour = int(text_date[11:13])
        minute = int(text_date[14:16])
        date = datetime.datetime(year,month,day,hour,minute)
    except ValueError:
        date = datetime.datetime(2000,1,1)
    return date

def date_from_text(text_date):
    try:
        day = int(text_date[0:2])
        month = int(text_date[3:5])
        year = int(text_date[6:10])
        date = datetime.date(year,month,day)
    except ValueError:
        date = datetime.date(2000,1,1)
    return date

def print_time(date_time):
    hour = ""
    minute = ""
    
    if (date_time.hour < 10):
        hour = "0"
    hour += str(date_time.hour)
    
    if (date_time.minute < 10):
        minute = "0"
    minute += str(date_time.minute)
    
    return hour + ":" + minute
