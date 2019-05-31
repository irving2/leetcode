# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:28
# @Author  : Irving

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def find_two_smallest(arr):
    # 一次for循环，找到数组中最小的两个值
    m1 = float('inf')       # 最小值
    m2 = float('inf')       # 次小值
    for i in range(len(arr)):
        if arr[i]<m1:
            m2=m1
            m1=arr[i]
        if arr[i]<m2:
            m2=arr[i]
        return m1,m2

def find_largest_in_section(arr,i,j):
        arr = arr[i:j]
        max=-float('inf')
        for num in arr:
            if num>max:
                max=num
        return max




if __name__ == '__main__':
    # print (selectionSort([5,73,1,9,12,2]))
    a = [1,0,3,4,6,8,1,1]
    print(find_two_smallest(a))