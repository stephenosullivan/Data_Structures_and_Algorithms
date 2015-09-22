__author__ = 'stephenosullivan'

"""Write an AVL tree implementation that maintains balances
in each node and implements insert iteratively. Write a test
program to thoroughly test your program on some randomly
 generated data."""

import random

class AVLTree:
    """AVLTree with iterative insert"""
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

        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem
            yield self.item

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, item):
        stack = []
        node = self.root
        while node:
            if item <= node:
                node.balance -= 1
                stack.append(node.left)
                node = node.left
            else:
                node.balance += 1
                stack.append(node.right)
                node = node.right

        node = self.AVLNode(item)

        pivot = None
        while stack and not pivot:
            trackback = stack.pop()
            if trackback.balance != 0:
                pivot = trackback
            else:
                trackback.balance = self.calc_balance(trackback.left) - self.calc_balance(trackback.right)

        if pivot:
            #Case 2:
            if ~(item > pivot.value ^ pivot.value > 0):
                pivot.balance = self.calc_balance(pivot.left) - self.calc_balance(pivot.right)

            #Case 3:
            else:


    def calc_balance(self, node):
        return self.height(node.right) - self.height(node.left)

    def height(self, node):
        if node:
            return max(self.height(node.left), self.height(node.right)) + 1
        return 0

    def __iter__(self):
        if self.root:
            yield self.root
            # return self.root.__iter__()
        else:
            return [].__iter__()

if __name__ == '__main__':
    random.seed(0)
    Tree1 = AVLTree()
    for _ in range(100):
        Tree1.insert(random.randint(0, 100))
    for item in Tree1:
        print(item)