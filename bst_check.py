import collections
import sys
# Collections module has already been imported.
class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    
    def validate_BST_Itr(self,root):
        class TreeBoundryNode:
            def __init__(self, tree_node = None, left_boundry = None, right_boundry = None):
                self.tree_node = tree_node
                self.left_boundry = left_boundry
                self.right_boundry = right_boundry

        # base case
        if root == None or (root.left_child == None and root.right_child == None):
            return True
        
        queue = collections.deque()
        queue.append(TreeBoundryNode(root,-sys.maxsize-1, sys.maxsize))
        while queue:
            # pop off a tree boundry node
            tree_binary_node = queue.popleft()
            tree_node = tree_binary_node.tree_node
            if (tree_node.data <= tree_binary_node.left_boundry) or (tree_node.data >= tree_binary_node.right_boundry):
                return False

            if tree_node.left_child != None:
                queue.append(TreeBoundryNode(tree_node.left_child, tree_binary_node.left_boundry, tree_node.data))

            if tree_node.right_child != None:
                queue.append(TreeBoundryNode(tree_node.right_child, tree_node.data, tree_binary_node.right_boundry))

            return True