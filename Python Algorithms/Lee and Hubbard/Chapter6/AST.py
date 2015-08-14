__author__ = 'stephenosullivan'

import queue

class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"

class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"

class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

def E(q):
    if q.empty():
        raise ValueError("Invalid prefix expression")

    token = q.

    if token == "+":
        return PlusNode(E(q), E(q))

    if token == "*":
        return TimesNode(E(q), E(q))

    return NumNode(float(token))

def main():
    x = NumNode(5)
    y = NumNode(4)
    p = PlusNode(x, y)
    t = TimesNode(p, NumNode(6))
    root = PlusNode(t, NumNode(3))
    print(root.eval())

    x = input("Enter a prefix expression")

    lst = x.split()
    q = queue.Queue()

    for token in lst:
        q.put(token)

    root = E(q)

    print(root.eval())
    print(root.inorder())

if __name__ == "__main__":
    main()
