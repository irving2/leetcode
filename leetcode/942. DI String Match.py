# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 14:58
# @Author  : Irving

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        min_cur, max_cur = 0,len(S)
        for i in S:
            if i=='I':
               res.append(min_cur)
               min_cur+=1
            else:
                res.append(max_cur)
                max_cur-=1
        return res+min_cur

