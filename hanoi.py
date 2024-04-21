# -*- coding: utf-8 -*-
"""
@Author  : ♡ uwutara ⸝⋆
@Contact : tara0523@outlook.com
"""


def hanoi(n, a, b, c):
    # 定义结束条件
    if n > 0:
        # 调用自身
        hanoi(n - 1, a, c, b)
        # 打印数据
        print("moving from %s to %s" % (a, c))
        # 调用自身
        hanoi(n - 1, b, a, c)


hanoi(5, 'A', 'B', "C")
