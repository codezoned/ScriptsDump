class Node:
    """
    Class Node
    """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def create_node(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        # if tree is empty , return a root node
        if node is None:
            return self.create_node(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def delete_node(self, node, data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:  # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp

        return node

    def traverse_inorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)

    def traverse_preorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data)


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)

    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverse_inorder(root)

    print("Traverse Preorder")
    tree.traverse_preorder(root)

    print("Traverse Postorder")
    tree.traverse_postorder(root)


if __name__ == "__main__":
    main()
