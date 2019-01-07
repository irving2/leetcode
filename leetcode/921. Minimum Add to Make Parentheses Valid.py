# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 10:25
# @Author  : Irving

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left=0
        right=0
        for p in S:
            if p=='(':
                left+=1
            elif p==')' and left<=0:
                right+=1
            else:
                left-=1
        return left+right