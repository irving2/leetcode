#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/3


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans=0
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=0
        return ans






