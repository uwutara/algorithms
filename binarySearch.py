# -*- coding: utf-8 -*-
"""
@File    : binarySearch.py
@Date    : 2024/4/21 17:43
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


# 二分查找 时间复杂度为O(logn)

# 定义要找的元素，中间值元素
def binarySearch(n, x):
    left = 0  # 定义Left的初始值
    right = len(n) - 1  # 定义Right的初始值
    while left <= right:  # 进行循环，设置结束条件 left <= right
        mid = (left + right) // 2  # 定义中间值
        if n[mid] == x:  # 如果第一次查找就找到了X 直接返回mid 此时mid即为X
            return mid
        elif n[mid] > x:  # 如果mid大于X，那么让Right-1
            right = mid - 1
        else:  # n[mid] < x | 如果mid小于X，让left+1
            left = mid + 1
    else:
        return None  # 在列表内没找到相应的元素 返回None


n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(n, 3))
