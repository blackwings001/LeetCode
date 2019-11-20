# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        queue = [(root, 0, "right")]  # "right"记录的是下一层的遍历方向
        while queue:
            ele = queue.pop(0)
            node = ele[0]
            level = ele[1]
            direction = ele[2]

            if len(res) == level + 1:
                res[level].append(node.val)
            else:
                res.append([node.val])
            if direction == "right":
                if node.right:
                    queue.append((node.right, level + 1, "left"))
                if node.left:
                    queue.append((node.left, level + 1, "left"))
            elif direction == "left":
                if node.left:
                    queue.append((node.left, level + 1, "right"))
                if node.right:
                    queue.append((node.right, level + 1, "right"))
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().zigzagLevelOrder(root)
    print(result)