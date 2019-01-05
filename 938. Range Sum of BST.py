class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root.val == None:
            return 0
        l = self.rangeSumBST(root.left,L,R)
        r = self.rangeSumBST(root.right,L,R)
        return l+r+(L<=root.val<=R)*root.val
