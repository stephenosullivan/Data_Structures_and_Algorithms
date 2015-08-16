__author__ = 'stephenosullivan'


class ToDictMixin(object):
    def todict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.todict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        # elif isinstance(value, list):
        #     return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinarySearchTree(ToDictMixin):
    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right


        def getValue(self):
            return self.value

        def setValue(self, value):
            self.value = value

        def getLeft(self):
            return self.left

        def setLeft(self, node):
            self.left = node

        def getRight(self):
            return self.right

        def setRight(self, node):
            self.right = node

        def __iter__(self):
            if self.left:
                for elem in self.left:
                    yield elem

            yield self.value

            if self.right:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            if root is None:
                return BinarySearchTree.__Node(val)

            if val < root.getValue():
                root.setLeft(__insert(root.getLeft(), val))

            else:
                root.setRight(__insert(root.getRight(), val))

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def exists(self, value):
        def __exists(root, value):
            if root is None:
                return False
            elif value < root.getValue():
                return __exists(root.left, value)
            elif value > root.getValue():
                return __exists(root.right, value)
            else:
                return True

        return __exists(self.root, value)

    def delete(self, value):
        def __delete(root, value):
            if root is None:
                return root
            elif root.getValue() == value:
                if root.getLeft() is None and root.getRight() is None:
                    return None
                elif root.getLeft() and root.getRight():
                    node = root.getRight()
                    if node.left:
                        while node.left and node.left.left:
                            node = node.left
                        root.value = node.left.getValue()
                        node.left = node.left.right
                        return root
                    else:
                        node.left = root.left
                        return node
                else:
                    return root.getLeft() or root.getRight()

            elif value < root.getValue():
                root.setLeft(__delete(root.left, value))
            else:
                root.setRight(__delete(root.right, value))
            return root

        self.root = __delete(self.root, value)

    def __str__(self):
        s = "["
        for item in self:
            s += "%d, " % item
        s += "]"
        return s


def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()

    tree = BinarySearchTree()

    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)


def main2():
    print("""
    Binary Search Tree Program
    --------------------------
    """)
    tree = BinarySearchTree()
    while True:
        s = input("Make a choice: \n"
                  "1. Insert into a tree \n"
                  "2. Delete from tree \n"
                  "3. Lookup value \n"
                  "4. Print tree \n"
                  "5. Print dict tree \n"
                  "Choice? ")

        if s == '1':
            # Insertion
            while True:
                value = input("insert? ")
                try:
                    val_int = int(value)
                except ValueError:
                    break

                tree.insert(val_int)
            print("\n")

        elif s == '2':
            # Deletion
            value = input("Value? ")
            try:
                val_int = int(value)
            except ValueError:
                print("Need to enter an int")
                break
            if tree.exists(val_int):
                tree.delete(val_int)
                print("%d deleted" % val_int)
            else:
                print("%d not in tree" % val_int)

        elif s == '3':
            # Check existence
            value = input("Value? ")

            try:
                val_int = int(value)
            except ValueError:
                print("Need to enter an int")
                break
            if tree.exists(val_int):
                print("Yes, %s is in the tree" % value)
            else:
                print("No, %s is not in the tree" % value)

        elif s == '4':
            print(tree)

        elif s == '5':
            print(tree.todict())
        else:
            print("Try again")


if __name__ == '__main__':
    # main()
    main2()
