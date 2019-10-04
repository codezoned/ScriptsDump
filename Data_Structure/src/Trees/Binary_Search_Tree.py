"""
A binary search tree is a rooted binary tree, whose internal nodes each
store a key (and optionally, an associated value) and each have two
distinguished sub-trees, commonly denoted left and right.

The tree additionally satisfies the binary search property, which states that
the key in each node must be greater than or equal to any key stored in the
left sub-tree, and less than or equal to any key stored in the right sub-tree.

https://en.wikipedia.org/wiki/Binary_search_tree

"""

from random import randint

class Node:         # class to create nodes
    def __init__(self, Parent = None, Value = None, Left = None, Right = None):
        self.parent = Parent        # points to parent of Node
        self.value = Value          # value in Node
        self.left = Left            # points to left child
        self.right = Right          # points to right child

    def __str__(self):
        return str(self.value)

class BST:

    def __init__(self):
        self.__root = None      # initially root = None

    def is_empty(self):
        return self.__root == None

    def insert(self, val):
        if( self.is_empty() ):          # if root = None (no nodes added to tree)
            self.__root = Node(Value = val)     # create new node & assign to root
        else:
            current = self.__root           # current node = root (initially)
            while( current != None ):
                parent = current
                current = current.left if( val <= current.value ) else current.right    # if val < current.value, goto left child, else goto right child

            if( val <= parent.value ):          # if val < parent.value
                parent.left = Node(parent, val)     # assign new node as Left child
            else:
                parent.right = Node(parent, val)    # assign new node as Right child

    def preorder(self, current = -1):
        if (current == -1 ): current = self.__root      # if current == -1 (no argument passed), current = root

        # Pre-Order = (Root, Left, Right)
        Ret = []
        if(current != None):
            Ret.append(current.value)   # Root (value)
            Ret.extend(self.preorder(current.left))     # Left (subtree)
            Ret.extend(self.preorder(current.right))    # Right (subtree)
        return Ret

    def inorder(self, current = -1):
        if (current == -1 ): current = self.__root      # if current == -1 (no argument passed), set current = root

        # In-Order = (Left, Root, Right)
        Ret = []
        if(current != None):
            Ret.extend(self.inorder(current.left))     # Left (subtree)
            Ret.append(current.value)   # Root (value)
            Ret.extend(self.inorder(current.right))    # Right (subtree)
        return Ret

    def postorder(self, current = -1):
        if (current == -1 ): current = self.__root      # if current == -1 (no argument passed), set current = root

        # Post-Order = (Left, Right, Root)
        Ret = []
        if(current != None):
            Ret.extend(self.postorder(current.left))     # Left (subtree)
            Ret.extend(self.postorder(current.right))    # Right (subtree)
            Ret.append(current.value)   # Root (value)
        return Ret

    def levelorder(self, current = -1):

        Ret = []

        if( self.is_empty() ): return Ret       # if tree is empty, return empty list

        if( current == -1 ):
            current = [self.__root]      # if current == -1 (no argument passed), set current = [root]
            Ret.append(self.__root.value)       # append root.value to Ret

        next_level = []     # list of all nodes on Next Level

        for each in current:    # current -> list of all nodes on any particular level

            if( each.left != None ):    # if node on current level has left child
                Ret.append(each.left.value)     # insert its value to Ret
                next_level.append(each.left)    # add left child to next_level

            if( each.right != None ):   # if node on current level has right child
                Ret.append(each.right.value)    # insert its value to Ret
                next_level.append(each.right)   # add right child to next_level

        if( next_level ):       # if there are any nodes in the next_level
            Ret.extend(self.levelorder(next_level))     # process nodes in next_level

        return Ret

    def search(self, find):
        current = self.__root

        while current and current.value != find :       # while current (current != None) and value is not found
            current = current.right if(current.value < find) else current.left      # if "find" is larger than current.value, traverse Right sub-tree, else left sub-tree

        return current      # return Node (None if value not found)

    def maximum(self, current = -1):
        if current == -1:           # find maximum of current sub tree, if argument is not passed, use root
            current = self.__root

        while current and current.right != None :       # while current != None & current has a right child
            current = current.right
        return current

    def minimum(self, current = -1):
        if current == -1:           # find minimum of current sub tree, if argument is not passed, use root
            current = self.__root

        while current and current.left != None :       # while current != None & current has a left child
            current = current.left
        return current

    def successor(self, node):

        if node.right == None:          # if node does not have right child
            while node.parent != None and node.parent.right == node :   # traverse to parent while Parent != None & node is right child of parent
                node = node.parent
            return node.parent
        else:
            return self.minimum(node.right)     # return Minimum from right subtree

    def predecessor(self, node):

        if node.left == None:
            while node.parent != None and node.parent.left == node :
                node = node.parent
            return node.parent
        else:
            return self.maximum(node.left)      # return Maximum from left subtree

if __name__ == "__main__":

    T1 = BST()

    # insert random 10 numbers in the tree
    for i in range(10):
        T1.insert(randint(1, 50))

    print("Level-Order = ", T1.levelorder())
    print("  Pre-Order = ", T1.preorder())
    print(" Post-Order = ", T1.postorder())
    print("   In-Order = ", T1.inorder())

    find = 10
    Found_Node = T1.search(find)
    if(Found_Node):
        print("Successor of", find, " = ", T1.successor(Found_Node))
        print("Predecessor of", find, " = ", T1.predecessor(Found_Node))
        print("\nValue Found, Parent = ", Found_Node.parent, "left = ", Found_Node.left, "right = ", Found_Node.right)
    else:
        print("\n", find, "not found in tree")

    print("\nMaximum = ", T1.maximum())
    print("Minimum = ", T1.minimum())
