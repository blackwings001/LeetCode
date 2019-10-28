# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n == 0:
            return res

        def level(root):
            res = []
            stack = []

            stack.append(root)
            while stack:
                ele = stack.pop(0)
                if ele:
                    res.append(ele.val)
                    stack.append(ele.left)
                    stack.append(ele.right)

            print(res)

        def tree(nodes):
            if not nodes:
                return [None]
            elif len(nodes) == 1:
                return nodes

            tmp = []
            for i in range(len(nodes)):
                root = nodes[i]
                left = tree(nodes[:i])
                right = tree(nodes[i+1:])
                for l in left:
                    for r in right:
                        root.left = l
                        root.right = r
                        tmp.append(root)
            for i in tmp:
                level(i)
            return tmp


        nodes = [TreeNode(i + 1) for i in range(n)]
        res = tree(nodes)

        return res


if __name__ == '__main__':
    n = 3
    res = Solution().generateTrees(n)

    def level(root):
        res = []
        stack = []

        stack.append(root)
        while stack:
            ele = stack.pop(0)
            if ele:
                res.append(ele.val)
                stack.append(ele.left)
                stack.append(ele.right)

        print(res)

    for root in res:
        level(root)
