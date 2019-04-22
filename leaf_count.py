class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root):
        counter = 0
        if root==None:
            # base check to make sure there is a tree at all
            return 0
        if root.left_child!=None:
            # recursive call down the left side
            counter += self.number_of_leaves(root.left_child)
        if root.right_child!=None:
            # recursive call down the right side
            counter += self.number_of_leaves(root.right_child)
        if root.right_child==None and root.left_child==None:
            # only add to the counter if this is a "leaf"
            return counter+1
        else:
            # otherwise don't add to the counter
            return counter