#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/3/4

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        len_board = 8
        [(row_r,col_r)] = [(row,col) for row in range(len_board) for col in range(len_board) if board[row][col]=='R']

        def traverse(row,col,x,y):
            if not 0<row<8 or not 0<col<8 or board[row][col]=='B':
                return 0
            if board[row][col]=='p':
                return 1
            return traverse(row+x,col+y,x,y)

        return sum([traverse(row_r,col_r,x,y) for x,y in [(1,0),(0,1),(-1,0),(0,-1)]])
