__author__ = 'stephenosullivan'


class Heapv1:
    def __init__(self):
        self.storage = []
        self.allocation = 0
        self.size = 0

    def buildfrom(self, aSequence):
        """aSequence is an instance of a sequence collection
         which understands the comparison operators. The
          elements of aSequence are copied into the heap and
          ordered to build a heap."""
        for item in aSequence:
            self.addToHeap(item)

    def fastbuildfrom(self, aSequence):
        self.allocation = len(aSequence)
        self.size = self.allocation
        self.storage = aSequence
        startIndex = (self.size - 2)//2
        print(startIndex)
        while startIndex > -1:
            bigChild = self.biggerChild(startIndex, self.size-1)
            if bigChild:
                if self.storage[startIndex] < self.storage[bigChild]:
                    self.storage[startIndex], self.storage[bigChild] = self.storage[bigChild], self.storage[startIndex]
            startIndex -= 1

    def biggerChild(self, parentIndex, lastIndex):
        """return the index of the larger child"""
        leftIndex = self.leftChildFromParent(parentIndex)
        rightIndex = self.rightChildFromParent(parentIndex)
        if leftIndex <= lastIndex:
            leftvalue = self.storage[leftIndex]
        else:
            leftvalue = None

        if rightIndex <= lastIndex:
            rightvalue = self.storage[rightIndex]
        else:
            rightvalue = None

        if leftvalue and rightvalue:
            if max(leftvalue, rightvalue) == leftvalue:
                return leftIndex
            else:
                return rightIndex
        elif leftvalue:
            return leftIndex
        else:
            return None


    def __siftUpFrom(self, child_index):
        """childIndex is the index of a node in the heap.
        This method sifts that node up as far as necessary
        to ensure that the path to the root satisfies the
        heap condition. """
        if child_index > 0:
            if self.storage[self.parentFromChild(child_index)] < self.storage[child_index]:
                self.storage[self.parentFromChild(child_index)], self.storage[child_index] = self.storage[child_index], self.storage[self.parentFromChild(child_index)]
                self.__siftUpFrom(self.parentFromChild(child_index))

    def addToHeap(self, newObject):
        """If the heap is full, double its current capacity.
       Add the newObject to the heap, maintaining it as a
       heap of the same type.  Answer newObject."""
        # if self.size > 0:
        #     assert type(self.storage[-1]) == type(newObject)
        if self.size == self.allocation:
            self.storage.extend([None]*(self.allocation+1))
            self.allocation = 2*self.allocation + 1
        self.storage[self.size] = newObject
        if self.size > 0:
            self.__siftUpFrom(self.size)
        self.size += 1

    def siftDownFromTo(self, fromIndex, lastIndex):
        """fromIndex is the index of an element in the heap.
        Pre: data[fromIndex..lastIndex] satisfies the heap condition, except perhaps for the element data[fromIndex].
        Post: That element is sifted down as far as neccessary to maintain the heap structure for data[fromIndex..lastIndex]."""
        bigChild = self.biggerChild(fromIndex, self.size-1)
        if bigChild:
                if self.storage[fromIndex] < self.storage[bigChild]:
                    self.storage[fromIndex], self.storage[bigChild] = self.storage[bigChild], self.storage[fromIndex]
                self.siftDownFromTo(bigChild, lastIndex)

    def leftChildFromParent(self, parent_index):
        """return left child index given parent"""
        return 2*parent_index + 1

    def rightChildFromParent(self, parent_index):
        """return right child index given parent"""
        return 2*parent_index + 2

    def parentFromChild(self, child_index):
        return (child_index - 1)//2

    def __repr__(self):
        output = "Hashv1(["
        for index, item in enumerate(self.storage):
            if index < self.size:
                output += str(item)
                if index < self.size - 1:
                    output += ', '
        output += "])"
        return output

    def removeFromHeap(self, index):
        if self.size > index:
            top = self.storage[0]
            self.storage[0], self.storage[self.size-1] = self.storage[self.size-1], None
            self.size -= 1
            self.siftDownFromTo(index, self.size-1)
            return top
        else:
            print("IndexError")
            return None

    def sort(self):
        output = [None]*self.size
        cnt = 1
        while output[0] is None:
            output[-cnt] = self.removeFromHeap(0)
            cnt += 1
        return output

def test1():
    firstHeap = Heapv1()
    firstList = [71, 57, 36, 15, 101]
    firstHeap.buildfrom(firstList)
    print(firstHeap)
    print(firstHeap.sort())

def test2():
    secondHeap = Heapv1()
    secondList = [110, 58, 85, 34, 17, 27, 78, 12, 98]
    secondHeap.buildfrom(secondList)
    print(secondHeap)
    print(secondHeap.sort())

def test3():
    thirdHeap = Heapv1()
    firstList = [71, 57, 36, 15, 101]
    thirdHeap.fastbuildfrom(firstList)
    print(thirdHeap)
    print(thirdHeap.sort())


if __name__ == "__main__":
    from timeit import Timer

    t = Timer("test1()", "from __main__ import test1")
    print(t.timeit(number=1))

    t = Timer("test2()", "from __main__ import test2")
    print(t.timeit(number=1))

    t = Timer("test3()", "from __main__ import test3")
    print(t.timeit(number=1))


