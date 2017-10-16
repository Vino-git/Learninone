import datetime
import time


def cron_time(minu, hour, day_of_month, month_of_year, day_of_week, year):
    try:
        localtime = time.localtime()
        now=datetime.datetime.now()

        if (localtime.tm_min >= minu and localtime.tm_min <= minu+15) or minu == '*':
            if localtime.tm_hour == hour or hour == '*':
                if localtime.tm_mday == day_of_month or day_of_month == '*':
                    if localtime.tm_mon == month_of_year or month_of_year == '*':
                        if localtime.tm_wday == day_of_week or day_of_week == '*':
                            if localtime.tm_year == year or year == '*':
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False
