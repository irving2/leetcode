#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/11


class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def binary( x):
            if x < 2:
                return str(x)
            return binary(x//2) + str(x % 2)

        def int_10(s):
            ret = 0
            for i in range(len(s)):
                ret += pow(2, i) * int(s.pop())
            return ret

        bin_N = binary(N)
        s = ['1' if e=='0' else '0' for e in bin_N]
        return int_10(s)

if __name__ == '__main__':

    def binary(x):
        if x < 2:
            return str(x)
        return binary(x // 2) + str(x % 2)

    print(binary(4))












