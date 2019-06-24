#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/31


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # n = len(A)
        # if n<=2:
        #     return True
        is_great=False
        is_less = False
        for i  in range(1,len(A)):
            if A[i-1]<A[i]:
                is_great=True
            if A[i-1]>A[i]:
                is_less=True
            if is_great and is_less:
                return False
        return True









