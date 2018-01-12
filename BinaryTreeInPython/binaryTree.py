class TreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None


class BST(object):
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, root, value):
        if root is None:
            return TreeNode(value)

        elif root.data >= value:
            root.left_child = self.insert(root.left_child, value)
            return root

        else:
            root.right_child = self.insert(root.right_child, value)
            return root

    def print_preorder(self, root):
        if root is None:
            return
        print(root.data, end='    ')
        self.print_preorder(root.left_child)
        self.print_preorder(root.right_child)

    def print_inorder(self, root):
        if root is None:
            return
        self.print_inorder(root.left_child)
        print(root.data, end='    ')
        self.print_inorder(root.right_child)

    def print_postorder(self, root):
        if root is None:
            return
        self.print_postorder(root.left_child)
        self.print_postorder(root.right_child)
        print(root.data, end='    ')
