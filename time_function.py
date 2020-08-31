import datetime 
from datetime import timedelta


def time_delta(time1, time2):
	datetimeFormat = '%H%M'
	diff = datetime.datetime.strptime(time1,datetimeFormat)\
	-datetime.datetime.strptime(time2,datetimeFormat)
	return round(diff.seconds//60/60,2)

	