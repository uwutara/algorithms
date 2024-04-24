# -*- coding: utf-8 -*-
"""
@File    : selectSort.py
@Date    : 2024/4/23 17:01
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


# 选择排序 时间复杂度为O(n²)
# 不推荐使用 ： 1. 生成了两个列表，占用空间大

def selectSort(li):
    # 定义新列表
    newList = []
    # 遍历，每次找到一个最小的数放到新列表里面
    for i in range(len(li)):
        # 找到且定义最小值
        minNum = min(li)
        # 把最小的值添加到新列表中
        newList.append(minNum)
        # 删除旧列表中的值
        li.remove(minNum)
        # 返回新列表
    return newList


# 优化后的选择排序 时间复杂度为O(n²)
def betterSelectSort(li):
    for i in range(len(li) - 1):
        # 假定最小的数的位置
        min_loc = i
        for j in range(i+1, len(li)):
            # 如果 min_loc 小于之后的数，那么进行交换
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [2, 1, 4, 3, 6, 5, 8, 7, 9]
# selectSort(li)
betterSelectSort(li)
print(li)
