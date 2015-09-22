__author__ = 'stephenosullivan'

class AVLTree:
    class AVLNode:
        def __init__(self, item, balance=0, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def __repr__(self):
            return "AVLTree.AVLNode(" + repr(self.item) + ",balance=" + \
                repr(self.balance) + ",left=" + repr(self.left) + \
                ",right=" + repr(self.right) + ")"

    def __init__(self, root=None):
        self.root = root

    def insert(self, item):
        def __insert(root,item):
            return root

        self.pivotFound = False
        self.root = __insert(self.root,item)

    def __repr__(self):
        return "AVLTree(" + repr(self.root) + ")"

    def __iter__(self):
        return iter(self.root)