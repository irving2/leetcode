#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/9

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row_num = len(matrix)
        col_num  = len(matrix[0])
        for i in range(row_num-1):
            for j in range(col_num-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True









