#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/9


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = self.binary(N)
        distance=0
        pre=0
        for i,c in enumerate(N):
            if c=='1':
                distance = max(distance,i-pre)    # distance和pre记录中间状态，for循环处理所有元素
                pre=i
        return distance

    def binary(self,x):   # 递归将一个整数转成二进制，str.
        if x==0:
            return ''
        return self.binary(int(x/2))+str(x%2)
