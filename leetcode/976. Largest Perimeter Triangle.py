#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/13


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # def quick_sort(a):
        #     right=[]
        #     left=[]
        #     if len(a)<2:
        #         return a
        #     for e in a[1:]:
        #         if e>=a[0]:
        #             right.append(e)
        #         if e<a[0]:
        #             left.append(e)
        #     return quick_sort(left)+[a[0]]+quick_sort(right)
        # A = quick_sort(A)
        #
        # curr_d = []
        # while True:
        #     if len(curr_d)<3:
        #         if len(A)==0:
        #             break
        #         curr_d.append(A.pop())
        #         continue
        #     if curr_d[0]<curr_d[1]+curr_d[2]:
        #         return sum(curr_d)
        #     else:
        #         curr_d.pop(0)
        # return 0

        A=sorted(A,reverse=True)
        for i,x in enumerate(A[:-2]):
            if x<A[i]+A[i+1]:
                return sum(A[i:i+2])
        return 0






if __name__ == '__main__':
    def quick_sort(a):
        right = []
        left = []
        if len(a)<2:
            return a

        for e in a[1:]:
            if e >= a[0]:
                right.append(e)
            if e < a[0]:
                left.append(e)
        return quick_sort(left) + [a[0]] + quick_sort(right)

    print(quick_sort([3,2,5,7,1]))
