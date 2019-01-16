# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 10:34
# @Author  : Irving

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if i%2==0:
                ans+=nums[i]
        return ans

