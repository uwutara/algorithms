# -*- coding: utf-8 -*-
"""
@File    : quickSort.py
@Date    : 2024/4/24 19:00
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


# 快排


# 定义partition函数
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


def quickSort(li, left, right):
    if left < right:  # 至少列表里面有两个元素
        mid = partition(li, left, right)
        quickSort(li, left, mid - 1)
        quickSort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# partition(li, 0, len(li) - 1)
quickSort(li, 0, len(li) - 1)
print(li)
