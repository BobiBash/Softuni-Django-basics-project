
import datetime as dt
import calendar as cal

current_month = dt.datetime.now().month - 1
current_year = dt.datetime.now().year
num_days = cal.monthrange(current_year, current_month)[1]

print(num_days)
days = [dt.date(current_year, current_month, day) for day in range(1, num_days + 1)]
print(days)