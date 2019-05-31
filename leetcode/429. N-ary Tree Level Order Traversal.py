#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/10


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# BFS
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Node
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []
#
#         result = []
#         stack = [root]
#         while stack:
#             if stack:
#                 result.append([node.val for node in stack])
#             next_level = []
#             while stack:
#                 node = stack.pop(0)
#                 if node.children:
#                     next_level+=node.children
#             stack=next_level
#         return result

# more neat and understandable
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue,result = [root],[]
        while any(queue):
            result.append([node.val for node in queue])
            queue=[child for node in queue for child in node.children if child ]
        return result