# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 10:11
# @Author  : Irving


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def tree(self, left, right):
        node = TreeNode(0)
        node.left = left
        node.right = right
        return node

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        return [self.tree(l, r)
                for k in range(1, N-1, 2)
                for l in self.allPossibleFBT(k)
                for r in self.allPossibleFBT(N-1-k)
                ]