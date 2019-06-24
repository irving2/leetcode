#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/3


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if not total%3==0:
            partial = total/3
            i = 0
            j = len(A)-1
            left_sum = 0
            right_sum = 0
            while i<j:
                left_sum+=A[i]
                right_sum+=A[j]
                if left_sum!=partial:
                    i+=1
                if right_sum!=partial:
                    j-=1
                if right_sum==partial and right_sum==partial:
                    return True
            return False
        else:
            return False




if __name__ == '__main__':
    s = 20
    targets = [2*s,s]
    print(targets)






