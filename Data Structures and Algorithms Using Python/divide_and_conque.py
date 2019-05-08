# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 15:37
# @Author  : Irving

# 递归求和

def recurrent_sum(arr):
    #基线条件
    if len(arr)<=1:
        return arr[0]
    else:
        return arr[0]+recurrent_sum(arr[1:])


def quick_sort(arr):
    # 基线条件
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x<pivot]
        right = [x for x in arr[1:] if x> pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)


if __name__ == '__main__':
    d = {'a':11}
    print (d.get('a','Not found!'))
    print ('d:',d)