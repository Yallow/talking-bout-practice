class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node
    
    # Required collection modules have already been imported. 
    def number_of_full_nodes(self,root):
        node_counter = 0
        if root is None:
            # base case
            return 0
        # work down the tree, only adding to the counter when a left and right child exist
        if root.left_child!=None:
           node_counter+=self.number_of_full_nodes(root.left_child)
        if root.right_child!=None:
            node_counter+=self.number_of_full_nodes(root.right_child)
        if root.right_child and root.left_child:
            node_counter+=1
        return node_counter