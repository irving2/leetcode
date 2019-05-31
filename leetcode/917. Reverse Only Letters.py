#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/31


# use stack pop()


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letter = [alpha for alpha in S if alpha.isalpha()]
        return ''.join(x if not x.isalpha() else letter.pop() for x in S )










