# -*- coding: utf-8 -*-
"""
@File    : linearSearch.py
@Date    : 2024/4/21 16:31
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


# 线性查找 时间复杂度为O(n)

def linearSearch(x, ele):
    # For循环
    for i, el in enumerate(x):
        # 在列表里面依次查找
        if el == ele:
            # 返回找到的元素
            return i
        else:
            # 若没有找到相关的元素，返回None
            return None

# linearSearch([1, 2, 3], 0) 调用&测试
