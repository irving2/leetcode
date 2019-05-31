#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/9


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS 宽度优先搜索
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return None

        stack = [root]
        depth=0
        while stack:
            next_level = []
            depth+=1
            while stack:
                node = stack.pop()
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            stack=next_level
        return depth