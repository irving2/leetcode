# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 10:13
# @Author  : Irving

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left,right+1):
            flag = 1
            for d in str(num):
               if d=='0' or num%int(d)!=0:
                    flag=0
                    break
            if flag==1:
                ans.append(num)
        return ans
