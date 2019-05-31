#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/14


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkList(object):
    def __init__(self):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next=self.tail
        self.tail.prev=self.head

    def print(self):
        first = self.head.next
        while first.next:
            print(first.value)
            first=first.next


    def add(self, value):
        pre = self.tail.prev
        new = Node(value)
        pre.next=new
        new.prev = pre

        new.next=self.tail
        self.tail.prev=new

    def remove(self, value):
        p = self.head
        while p.next:
            if p.value == value:
                temp = p.prev
                xyz = p.next
                temp.next = xyz
                xyz.prev = temp
                break
            else:
                p = p.next

    def find(self, value):
        #根据指定的值找出位置
        p = self.head
        i = -1
        while p.next:
            if p.value == value:
                return i
            else:
                p = p.next
                i += 1

        raise AttributeError(u"can\'t find this element")

    def index(self, index):
        #根据指定的位置找出相应的值
        i = -1
        p = self.head
        while p.next:
            if i == index:
                return p.value
            else:
                i += 1
                p = p.next
        raise IndexError(u'index out of range')

    def findprev(self, value):
        """根据指定节点的值找出前面的一个节点的值"""
        p = self.head
        while p.next:
            if p.value == value:
                return p.prev.value
            else:
                p = p.next
        raise AttributeError(u"can\'t find this element")

    def findnext(self, value):
        """根据指定节点的值找出后面的一个节点的值"""
        p = self.head
        while 1:
            if p.value == value:
                return p.next.value
            else:
                p = p.next
                if not p.next:
                    return None
        raise AttributeError(u"can\'t find this element")

    def insert(self, index, value):
        """index必须大于等于1
        """
        i = -1
        p = self.head
        new = Node(value)
        while p.next:
            if i == index:
                temp = p.prev
                temp.next = new
                new.prev = temp
                new.next = p
                p.prev = new
                break
            else:
                p = p.next
                i += 1
        #上面循环自然结束,就直接插入到元素的末尾
        else:
            prev = self.tail.prev
            prev.next=new
            new.prev = prev

            new.next = self.tail
            self.tail.prev=new

    @property
    def length(self):
        p = self.head
        i = 0
        while p.next !=self.tail:
            p = p.next
            i += 1

        return i

    def output(self):
        p = self.head
        while 1:
            print (p.value)
            p = p.next
            if not p.next:
                print (p.value)
                break

    def reverse(self):
        """反转链表"""
        length = self.length
        i = 0
        last = self.tail.prev
        first = self.head.next
        while i < length:
            first.value, last.value = last.value, first.value
            first = first.next
            last = last.prev
            i += 1
            length -= 1


if __name__ == '__main__':
    ll = LinkList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    print('print'.center(20,'*'))
    ll.reverse()
    ll.print()