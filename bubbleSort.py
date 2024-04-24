# -*- coding: utf-8 -*-
"""
@File    : bubbleSort.py
@Date    : 2024/4/23 16:13
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


# 冒泡排序(普通版) 时间复杂度为O(n²)

def bubbleSort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


def bubbleSortNew(li2):
    for i in range(len(li2) - 1):
        exchange = False
        for j in range(len(li2) - i - 1):
            if li2[j] > li2[j + 1]:
                li2[j], li2[j + 1] = li2[j + 1], li2[j]
                exchange = True
        print(li2)
        if not exchange:
            return


# li = [2, 4, 5, 1, 3, 6, 7, 9, 8]
# bubbleSort(li)
# print(li)

li2 = [1, 2, 3, 4, 5, 6, 8, 7, 9]
bubbleSortNew(li2)
# print(li2)
