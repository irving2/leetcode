# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 22:01
# @Author  : Irving

# 二分查找算法,时间复杂度O(logn)
def binary_search(item,num_list):
    low = 0
    high = len(num_list)-1
    while low<=high:
        mid = (low + high) / 2
        guess = num_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid+1
        else:
            high = mid-1
    return None

if __name__ == '__main__':
    L = [1,3,5,7,9,22]
    print (binary_search(7,L))