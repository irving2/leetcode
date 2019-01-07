# coding=utf-8

# 535. Encode and Decode TinyURL
import random
import string
'''
class Codec:
    def __init__(self):
        self.url_pair = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        # Get a set of characters that will make up the suffix
        suffix_set = string.ascii_letters + string.digits

        # Make a tinyurl template
        tiny_url = "http://tinyurl.com/".join(random.choice(suffix_set) for _ in range(6))

        # Store the pair in the dictionary
        self.url_pair[tiny_url] = longUrl

        return tiny_url

    def decode(self, shortUrl):
        """Decodes the shortened URL to its original URL."""
        # Return the value from a given key from the dictionary
        return self.url_pair.get(shortUrl)

def encode(self, longUrl):
    """Encodes a URL to a shortened URL.

    :type longUrl: str
    :rtype: str
    """
    self.hash = {}
    if longUrl not in self.hash:
        idx = hash(longUrl)
        self.hash[idx] = longUrl
    final_string = 'https://tinyurl.com/' + str(idx)
    return (final_string)

def decode(self, shortUrl):
    """Decodes a shortened URL to its original URL.
    :type shortUrl: str
    :rtype: str
    """
    v = shortUrl[20:len(shortUrl)]
    return (self.hash[int(v)])
'''
#
# class Solution(object):
#     def minDeletionSize(self, A):
#         """
#         :type A: List[str]
#         :rtype: int
#         """
#         num=0
#         for j in range(len(A[0])):
#             for i in range(len(A)-1):
#                 if ord(A[i][j]) > ord(A[i + 1][j]):
#                     num+=1
#                     break
#         return num

# class Solution:
#     def numJewelsInStones(self, J, S):
#         """
#         :type J: str
#         :type S: str
#         :rtype: int
#         """
#         for i

class Solution(object):
    def findAndReplacePattern(self, words, p):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]

        return [w for w in words if F(w) == F(p)]



if __name__ == '__main__':
    # words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    # pattern = "abb"
    # s= Solution()
    # print s.findAndReplacePattern(words,pattern)
    # # print ord('a')
    b = {1:'2',2:'2'}
    print len(b)



    # solution = Solution.findAndReplacePattern()
    # print solution.minDeletionSize( input)