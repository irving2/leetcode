# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 10:08
# @Author  : Irving


from collections import deque

def BSF(graph,start_node):
    '''
    广度优先搜索算法，找到图中两点之间最短的路径
    :param graph:
    :param start_node:
    :return:
    '''
    q = deque(graph[start_node])
    searched = []   # 避免双向图节点造成无限循环
    while q:
        name = q.popleft()
        if name not in searched:
            if is_needed(name):
                return True
            else:
                q.extend(graph[name])
                searched.append(name)
    return False

def is_needed(name):
    pass


if __name__ == '__main__':
    pass

