# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 10:06
# @Author  : Irving


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left,root.right = self.pruneTree(root.left),self.pruneTree(root.right)

        if not root.left and not root.right and not root.val:
            return None
        else:
            return root