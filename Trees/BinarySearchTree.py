import math
from collections import deque

class TreeNode:
    def __init__(self, key=None, value=None, left=None, right=None):
        # self.data = data
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        """
        initialises tree structure
        """
        self.root = None


    def insert(self, key, value, current_node=None):
        """
        inserts data into the binary search tree
        """
        #check if there is already data in the tree; if not make current data root node
        if self.root is None:
            self.root = TreeNode(key=key, value=value)
        
        #iterate through tree to find correct place for node
        else:
            #if current node is None we start at the roo
            if current_node is None:
                current_node = self.root
           


            if value < current_node.value:
                # check if we are at leaf node
                if current_node.left is None:
                    #insert new leaft node
                    current_node.left = TreeNode(key=key, value=value)
                else:
                    #if no leaf node keep searching
                    self.insert(key=key, value=value, current_node=current_node.left)
            elif value > current_node.value:
                #check if we are at leaf node
                if current_node.right is None:
                    #insert new leaf node
                    current_node.right = TreeNode(key=key, value=value)
                else:
                    #if no leaf node keep search
                    self.insert(key=key, value=value, current_node=current_node.right)
    

    def print_tree(self, node=None, level=0):
        """
        Simple recursive print — shows the tree structure.
        Right children appear above, left children below.
        """
        if node is None:
            node = self.root
            if node is None:
                print("(empty tree)")
                return

        if node.right:
            self.print_tree(node.right, level + 1)

        print("    " * level + f"{node.value}")

        if node.left:
            self.print_tree(node.left, level + 1)

bst = BinarySearchTree()
for idx,v in enumerate([8, 3, 10, 1, 6, 14, 4, 7, 13]):
    bst.insert(key=idx, value=v)

bst.print_tree()