# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 10:00
# @Author  : Irving

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            d = {}
            for w,p in zip(word,pattern):
                if d.setdefault(p,w)!=w:
                    return False
            return len(set(d.values()))==len(d.values())

        return filter(match,words)





if __name__ == '__main__':
    d = {}
    print d.setdefault('a',123)
    print d.setdefault('a',345)
    print d
