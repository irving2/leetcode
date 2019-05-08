#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/8


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# BFS 搜索

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root.children==None:
            return 0

        depth=1
        stack = [root]
        while stack:
            next_level = []
            while stack:
                node = stack.pop()   #
                if node.children:
                    next_level+=node.children
            stack=next_level
            depth+=1
        return depth






