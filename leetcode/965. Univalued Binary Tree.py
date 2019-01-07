# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 15:28
# @Author  : Irving

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.right:
            if root.right.val!=root.val:
                return False
        if root.left:
            if root.left.val !=root.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

if __name__ == '__main__':
    a = [3,5,4,8,7]
    print sorted(a)

    print sorted(a)