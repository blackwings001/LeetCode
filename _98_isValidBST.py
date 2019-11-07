# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif (not root.left or root.left.val < root.val) and (not root.right or root.right.val > root.val):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
