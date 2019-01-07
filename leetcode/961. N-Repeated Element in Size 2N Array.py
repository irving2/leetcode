# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 14:57
# @Author  : Irving

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set([])
        for i in A:
            if i in s:
                return i
            else:
                s.add(i)


if __name__ == '__main__':
    s = set([])
    s.update('boy')