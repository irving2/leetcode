#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/13


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack=[root]
        # DFS
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right=node.right,node.left
                stack.append(node.left)
                stack.append(node.right)
        return root









