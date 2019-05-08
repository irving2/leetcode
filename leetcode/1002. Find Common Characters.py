#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/3/5


class Solution(object):
    def commonChars(self, A):
        import collections
        """
        :type A: List[str]
        :rtype: List[str]
        """
        count = collections.Counter(A[0])
        for x in A[1:]:
            c = collections.Counter(x)
            count = count&c
        return list(count.elements())

if __name__ == '__main__':

    from collections import Counter

    a = 'sssbbc'
    b = 'sssssssc'

    counter = Counter(a)
    print('*')











