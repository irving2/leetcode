#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/3/7

import copy
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        col_num = len(A[0])
        result = []
        for i in range(col_num):
            new_row = []
            for row in A:
                new_row.append(row[i])
            result.append(new_row)




if __name__ == '__main__':
    s = Solution()
    A = [[1,2,3],[4,5,6],[7,8,9]]
    res = s.transpose(A)
    print(res)


