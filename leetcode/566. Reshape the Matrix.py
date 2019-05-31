#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/10

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0])!=r*c:
            return nums

        row_new=[]
        ret = []
        while nums:
            row = nums.pop(0)
            for x in row:
                row_new.append(x)
                if len(row_new)==c:
                    ret.append(row_new)
                    row_new=[]
        return ret


def foo(*args,**kwargs):
    print(args[0:3])
    print(kwargs)
foo(1,2,3,4,5,a=100)