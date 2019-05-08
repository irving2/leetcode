#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/8

# 先用二叉树中序遍历，保存所有节点到一个数组，然后连接起来即可

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if not root:
                return []
            array = []
            array.extend(inorder(root.left))
            array.append(root.val)
            array.extend(inorder(root.right))
            return array

        arr = inorder(root)
        if not arr:
            return None

        new_root = TreeNode(arr[0])
        cur_node = new_root

        for i in range(1,len(arr)):
            cur_node.right=TreeNode(arr[i])
            cur_node=cur_node.right
        return new_root
