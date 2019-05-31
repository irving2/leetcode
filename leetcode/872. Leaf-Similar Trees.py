#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def findleaf(root):
            if root==None:
                return []
            sq = []
            if not root.left and not root.right:
                return [root.val]
            return sq+findleaf(root.left)+findleaf(root.right)

        sq_1 = findleaf(root1)
        sq_2 = findleaf(root2)
        return sq_1==sq_2