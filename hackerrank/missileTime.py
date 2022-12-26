import datetime

lt = input()
tt = input()


def timecheck(a, b):
    return (0 <= a < 24) and (0 <= b < 60)


lt_hh = int(lt[0:2])
lt_mm = int(lt[3:5])

tt_hh = int(tt[0:2])
tt_mm = int(tt[3:5])

if(timecheck(lt_hh, lt_mm) and timecheck(tt_hh, tt_mm)):
    launch = datetime.datetime(2022, 1, 1, lt_hh, lt_mm)
    travel = datetime.time(tt_hh, tt_mm)
    tdelta = datetime.timedelta(hours=tt_hh, minutes=tt_mm)
    print((launch + tdelta).strftime('%H %M'))
else:
    print("Invalid Time !!")