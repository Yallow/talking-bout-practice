# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree_list = []
        queue, level = [], []
        # check for empyty tree
        if root is None:
            return
        
        # put the root on first then start adding its children
        queue.append(root)
        while len(queue) > 0:
            for _ in range(len(queue)):
                level.append(queue[0].val)
                node = queue.pop(0)
                # put the right and left child on the queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            tree_list.append(level)
            level = []
        return tree_list