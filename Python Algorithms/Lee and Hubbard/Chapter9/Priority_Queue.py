__author__ = 'stephenosullivan'

# Min Heap
class PriorityQueue():
    # Each item in the queue is a tuple (priority, *data)
    def __init__(self, items=None):
        if items:
            self.size = len(items)
            self.storage = items
            self.allocation = len(items)

            for i in range((self.size-2)//2, -1, -1):
                #print(self, 'loading', self.storage[i][0])
                if self.storage[self.minChildIndex(i)][0] < self.storage[i][0]:
                    min_index = self.minChildIndex(i)
                    self.storage[min_index], self.storage[i] = self.storage[i], self.storage[min_index]
                    #print(i , self.minChildIndex(i),self.storage[self.minChildIndex(i)], self.storage[i])
                    self.siftDownFrom(min_index)

        else:
            self.storage = [None]
            self.size = 0
            self.allocation = 1

    def extend_allocation(self):
        self.storage = self.storage + [None]*(self.allocation + 1)
        self.allocation = self.allocation * 2 + 1

    def shrink_allocation(self):
        self.storage = self.storage[:self.allocation//2 + 1]

    def parentFromChild(self, childIndex):
        return (childIndex - 1)//2

    def leftChildIndexFromParent(self, parentIndex):
        return 2 * parentIndex + 1

    def rightChildIndexFromParent(self, parentIndex):
        return 2 * parentIndex + 2

    def minChildIndex(self, index):
        #print('inside min child', index)
        left_index = self.leftChildIndexFromParent(index)
        right_index = self.rightChildIndexFromParent(index)

        if left_index > self.size - 1:
            return None
        leftChild = self.storage[left_index][0]

        if right_index > self.size - 1:
            return left_index
        rightChild = self.storage[right_index][0]

        if leftChild <= rightChild:
            return self.leftChildIndexFromParent(index)
        else:
            return self.rightChildIndexFromParent(index)

    # class Node(priority, data):
    #     def __init__(self):
    #         self.priority = priority
    #         self.data = data

    def enqueue(self, item):
        if self.size == self.allocation:
            self.extend_allocation()
        self.storage[self.size] = item
        self.siftUp(self.size)
        self.size += 1

    def dequeue(self):
        # Take the min node off the top
        index = 0
        output = self.storage[index]
        self.storage[index], self.storage[self.size-1] = self.storage[self.size-1], None
        self.size -= 1
        self.siftDownFrom(index)
        if self.size < self.allocation//2:
            self.shrink_allocation()
        return output

    def siftUp(self, index):
        if self.storage[self.parentFromChild(index)][0] > self.storage[index][0]:
            self.storage[self.parentFromChild(index)], self.storage[index] = self.storage[index], self.storage[self.parentFromChild(index)]
            if self.parentFromChild(index) > 0:
                self.siftUp(self.parentFromChild(index))

    def siftDownFrom(self, index):
        #print('sift', index, self.size, self.minChildIndex(index), self.storage)
        if index < self.size:

            if self.minChildIndex(index) and self.storage[index][0] > self.storage[self.minChildIndex(index)][0]:
                #print(self.storage[index][0], self.storage[self.minChildIndex(index)][0])
                tmp = self.storage[index]
                self.storage[index] = self.storage[self.minChildIndex(index)]
                self.storage[self.minChildIndex(index)] = tmp
                self.siftDownFrom(self.minChildIndex(index))

    def __repr__(self):
        return str([i[0] for i in self.storage[:self.size]])

    def __bool__(self):
        return bool(self.size)

if __name__ == '__main__':
    firstList = [(4, 71), (3, 57), (2, 36), (1, 15), (5, 101)]
    #firstList = [(4, 0), (3, 0), (2, 0), (1, 0), (5, 0)]
    firstHeap = PriorityQueue(firstList)
    print(firstHeap)
    firstHeap.enqueue((1,100))
    ordered = []
    while firstHeap:
        ordered.append(firstHeap.dequeue())
        print(firstHeap)
    print(ordered)

    secondHeap = PriorityQueue()
    secondHeap.enqueue((4, 71))
    secondHeap.enqueue((3, 57))
    secondHeap.enqueue((2, 36))
    secondHeap.enqueue((1, 15))
    secondHeap.enqueue((5, 101))
    print(secondHeap)
