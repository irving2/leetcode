#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/11


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        ret=[]
        if not isinstance(root,list):
            curr_level = [root]
        else:
            curr_level=root

        curr_sum = 0
        next_level = []
        for node in curr_level:
            curr_sum+=node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        return ret+[float(curr_sum/len(curr_level))]+self.averageOfLevels(next_level)




if __name__ == '__main__':
    a = [1]
    print(isinstance(a,list))

