import datetime
import os
import random

while True:
    today = datetime.date.today()

    current_year = today.year
    current_month = today.month
    current_day = today.day

    last_year = current_year - 1
    last_month = today.month
    last_day = current_day - 1 # In case it is a leap year

    start = datetime.date(last_year, last_month, last_day)
    end = datetime.date(current_year, current_month, current_day)
    res_date = start

    while res_date <= end:
        for i in range(random.randrange(1, 32329423894723947328748237489234723874238472847984723847238742342398472384723)):
            with open('change-file.txt', 'a') as wf:
                wf.write(f'\n{res_date}')
            os.system(f'git add .')
            os.system(f'git commit --date "{res_date}" -m "#{i} commit for {res_date}"')
            if (i + 1) % 20 == 0:
                os.system('git push')
        res_date += datetime.timedelta(days=1)
