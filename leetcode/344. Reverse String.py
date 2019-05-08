#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/8


# 空间复杂段o(1)，reverse数组中的元素,二分法



def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    l = len(s)
    if l < 2:
        return s
    mid = int(l / 2)
    return reverseString(s[mid:]) + reverseString(s[:mid])


input = ["h", "e", "l", "l", "o"]
print(reverseString(input))
