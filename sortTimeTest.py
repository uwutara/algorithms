# -*- coding: utf-8 -*-
"""
@File    : sortTimeTest.py
@Date    : 2024/4/24 19:35
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""
import random
from cal_time import *
import copy


# 排序运行时间对比
@cal_time
def bubbleSort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


@cal_time
def betterSelectSort(li):
    for i in range(len(li) - 1):
        # 假定最小的数的位置
        min_loc = i
        for j in range(i + 1, len(li)):
            # 如果 min_loc 小于之后的数，那么进行交换
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


def partition(li, left, right):
    # 定义一个临时变量
    temp = li[left]
    while left < right:

        # 从右边开始找比temp小的数
        while left < right and li[right] >= temp:
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值赋给左边的空位上

        # 从左边开始找比temp大的数
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]  # 把左边的值赋给右边的空位上

    li[left] = temp  # 把temp归位
    return left


def _quickSort(li, left, right):
    if left < right:  # 至少列表里面有两个元素
        mid = partition(li, left, right)
        _quickSort(li, left, mid - 1)
        _quickSort(li, mid + 1, right)


@cal_time
def quickSort(li):
    _quickSort(li, 0, len(li) - 1)


@cal_time
def insertSort(li):
    # i表示摸到的牌的下标
    for i in range(1, len(li)):
        temp = li[i]
        # j表示手里的牌
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


li = list(range(1000000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)
li4 = copy.deepcopy(li)

quickSort(li1)
# betterSelectSort(li2)
# insertSort(li3)
# bubbleSort(li4)
