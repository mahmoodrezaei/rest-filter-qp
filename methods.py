from datetime import datetime, timedelta
import jdatetime



jtoday = jdatetime.date.today()
today = datetime.today()
def this_week():
		start_week = jtoday - jdatetime.timedelta(jtoday.weekday())
		end_week = jtoday + jdatetime.timedelta(jtoday.weekday())
		print([start_week,end_week])
		return [start_week,end_week]


def this_month():
	return [today.year,today.month]


def this_day():
	return [today.year,today.month,today.day]