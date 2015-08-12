__author__ = 'stephenosullivan'

import random

class Sort:
    def selSort0(self, seq, start):
        for i in range(len(seq)):
            minimum = seq[i]
            for j in range(i + 1, len(seq)):
                if seq[j] < minimum:
                    minimum = seq[j]
                    index = j

            seq[index] = seq[i]
            seq[i] = minimum

    def select(self, seq, start):
        minIndex = start

        for j in range(start + 1, len(seq)):
            if seq[minIndex] > seq[j]:
                minIndex = j

        return minIndex

    def selSort(self, seq):
        for i in range(len(seq) - 1):
            minIndex = self.select(seq, i)
            tmp = seq[i]
            seq[i] = seq[minIndex]
            seq[minIndex] = tmp

    def mergeSortRecursive(self, seq):
        length = len(seq)
        if length > 1:
            mid = length // 2
            left = seq[:mid]
            right = seq[mid:]
            left = self.mergeSortRecursive(left)
            right = self.mergeSortRecursive(right)
            i, j = 0, 0
            output = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1

            if i < len(left):
                output.append(left[i:])

            elif j < len(right):
                output.append(right[j:])

            return output

        elif length == 1:
            return seq

    def mergeSort(self, seq):
        return self.mergeSortRecursive(seq)

    def partition(self, seq, start, stop):
        pivotIndex = start
        pivot = seq[pivotIndex]
        i = start + 1
        j = stop - 1

        while i <= j:
            while i <= j and not pivot < seq[i]:
                i += 1
            while i <= j and pivot < seq[j]:
                j -= 1

            if i < j:
                seq[i], seq[j] = seq[j], seq[i]
                i += 1
                j -= 1

        seq[pivotIndex], seq[j] = seq[j], pivot

        return j

    def quicksort(self, seq):
        # for i in range(len(seq)):
        #     j = random.randint(0,len(seq)-1)
        #     tmp = seq[i]
        #     seq[i] = seq[j]
        #     seq[j] = tmp
        self.quicksortRecursively(seq, 0, len(seq))

    def quicksortRecursively(self, seq, start, stop):
        if start >= stop - 1:
            return

        pivotIndex = self.partition(seq, start, stop)

        self.quicksortRecursively(seq, start, pivotIndex)
        self.quicksortRecursively(seq, pivotIndex + 1, stop)


if __name__ == '__main__':
    a = [3, 6, 9, 3, 6, 4, 1, 4, 2, 7, 5, 8, 1, 2]
    b = [5, 8, 2, 6, 9, 1, 0, 7]
    c = [7, 6, 8]
    sort1 = Sort()
    print(sort1.quicksort(a))
    print(a)
    #print(sort1.quicksort(b))
    print(sort1.selSort(c))
    print(c)
