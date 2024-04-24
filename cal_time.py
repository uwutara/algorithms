# -*- coding: utf-8 -*-
"""
@File    : cal_time.py
@Date    : 2024/4/24 19:41
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""
import time


# 计时器

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper
