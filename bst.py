# coding=utf-8

'''实现搜索二叉树'''

class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left=None
        self.right=None
# print tree
    def printTree(self,root):
        if root==None:
            return
        self.printTree(root.left)
        print root.val
        self.printTree(root.right)

# insert
    def insert(self,root,val):
        if root is None:
            root=TreeNode(val)
        else:
            if val>root.val:
                root.right = self.insert(root.right,val)
            elif val<root.val:
                root.left = self.insert(root.left,val)
        return root

    # qurey
    def query(self,root,val):
        if root.val==None:
            return False
        if root.val==val:
            return True
        elif root.val<val:
            return self.query(root.right,val)
        elif root.val>val:
            return self.query(root.left,val)
    #findMin
    def findMin(self,root):
        if root.left==None:
            return root
        else:
            return self.findMin(root.left)

    # findMax
    def findMax(self,root):
        if root.right==None:
            return root
        else:
            return self.findMax(root.right)

    # delete node
    def delNode(self,root,val):

        if root==None:
            return
        if val<root.val:
            root.left = self.delNode(root.left,val)
        elif val >root.val:
            root.right=self.delNode(root.right,val)
        else:
            if root.right and root.left:
                temp = self.findMin(root.right)
                root.val=temp.val
                root.right = self.delNode(root.right,temp.val)
            elif root.right==None and root.left==None:
                root=None
            elif root.right==None:
                root=root.left
            elif root.left==None:
                root = root.right
        return root

if __name__ == '__main__':
    root = TreeNode(10)
    root.insert(root,12)
    root.insert(root,11)
    root.insert(root,13)
    root.printTree(root)
    # print root.query(root,11)
    # print root.findMin(root).val
    # print root.findMax(root).val
    print 'delete tree node:',root.delNode(root,11)
    root.printTree(root)


