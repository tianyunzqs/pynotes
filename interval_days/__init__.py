# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 16:50
# @Author      : tianyunzqs
# @Description : 计算两个日期之间间隔的天数

import datetime


def is_leap(year):
    if (year % 4 == 0 and year % 100) or year % 400 == 0:
        return 1
    else:
        return 0


def get_dates(year, month, day):
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_day[1] = 29
    days = 0
    for y in range(1, year):
        days += 365 + is_leap(y)
    for m in range(month):
        days += month_day[m]
    days += day
    return days


def interval_days(year1, month1, day1, year2, month2, day2):
    d1 = get_dates(year1, month1, day1)
    d2 = get_dates(year2, month2, day2)
    return d1 - d2


if __name__ == '__main__':
    year1, month1, day1 = 2018, 4, 4
    year2, month2, day2 = 2018, 4, 13
    d1 = datetime.date(year1, month1, day1)
    d2 = datetime.date(year2, month2, day2)
    print((d1 - d2).days)
    print(interval_days(year1, month1, day1, year2, month2, day2))
