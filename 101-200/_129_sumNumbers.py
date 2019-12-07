# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def path_number(node, pre_path, res):
            if not node:
                return

            cur_path = pre_path + str(node.val)
            if not node.left and not node.right:
                res.append(cur_path)
                return

            path_number(node.left, cur_path, res)
            path_number(node.right, cur_path, res)

        res = []
        path_number(root, "", res)

        res = [int(i) for i in res]
        print(res)

        return sum(res)





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)

    res = Solution().sumNumbers(root)
    print(res)

