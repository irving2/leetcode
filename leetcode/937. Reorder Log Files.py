#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/13


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l=[]
        d =[]
        for log in logs:
            if log.split()[1].isdigit():
                d.append(log)
            else:
                l.append(log)
        l = sorted(l,key=lambda x:x.split()[1:])
        return l+d





