# -*- coding: utf-8 -*-
# @Time        : 2019/11/29 17:20
# @Author      : tianyunzqs
# @Description : 利用装饰器，计算函数运行时间

import time


def cal_run_time(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("%s cost %d ms" % (f.__name__, execution_time))
        return res
    return wrapper


@cal_run_time
def fun():
    time.sleep(5)


if __name__ == '__main__':
    fun()
