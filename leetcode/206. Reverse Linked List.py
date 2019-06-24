#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        next_node = head.next
        next_node.next=head




