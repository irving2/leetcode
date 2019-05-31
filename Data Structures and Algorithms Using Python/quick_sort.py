#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/13


# 递归方法快速排序

def quick_sort(a):
    right=[]
    left=[]

    # 递归出口
    if len(a)<2:
        return a

    for e in a[1:]:
        if e>=a[0]:
            right.append(e)
        else:
            left.append(e)
    # 递归
    return quick_sort(left)+[a[0]]+quick_sort(right)

if __name__ == '__main__':
    a = [1,3,2,9,4,3,5,1]
    print(quick_sort(a))







