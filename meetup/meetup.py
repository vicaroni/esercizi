from calendar import Calendar, isleap


def meetup_day(y, m, w, q):
	calendar = Calendar()
	g = {
		'Monday': 0,
		'Tuesday': 1,
		'Wednesday': 2,
		'Thursday': 3,
		'Friday': 4,
		'Saturday': 5,
		'Sunday': 6
	}
	l = [31, 29 if isleap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	c = 1
	for d in calendar.itermonthdates(y, m):
		if d.month == m and d.weekday() == g[w]:
			if q == 'teenth' and d.day in range(13, 20):
				return d
			if q == 'last' and l[m-1] - d.day < 7:
				return d
			if q != 'teenth' and q != 'last':
				if c == int(q[0]):
					return d
				else:
					c += 1
	raise Exception