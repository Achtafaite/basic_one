from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
delta = last_date - first_date
print(delta.days)
