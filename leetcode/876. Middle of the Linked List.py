#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = [head]
        arr=[]
        while stack:
            ln = stack.pop()
            arr.append(ln)
            if  ln.next:
                stack+=ln.next

        index = int(len(arr)/2)
        return arr[index]




