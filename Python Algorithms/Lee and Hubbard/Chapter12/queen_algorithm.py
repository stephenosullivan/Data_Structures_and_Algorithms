__author__ = 'stephenosullivan'

import sys
import copy
# front-end   back-end
#   8 --------->       # A size is specified to the back-end program
#   <----------- 0 10  # these are the row column pairs of possibly assigned queen locations
#   ...                # repeating until the search is complete
#   <----------- and   # The and is printed between the assigned and remaining locations
#   <----------- 1 2   # next comes the remaining locations
#   ...                # repeating until done
#   <----------- done  # Then done is printed after each state is completely enumerated
#   ...                # These states repeat until the search has concluded.
#   <----------- eof   # EOF is printed back to inidicate the end of the animation.


class SorterByConstraint:
    def __init__(self, remaining):
        self.remaining = remaining

    def __call__(self, item):
        # count overlaps between item and remaining positions
        cnt = 0
        i = 1
        for row in self.remaining[::-1]:
            common = {(item[0]+i, item[1]), (item[0]+i, item[1]-i), (item[0]+i, item[1]+i)} & row
            cnt += len(common)
            i += 1
        return cnt

def removeItems(item, remaining):
    i = 1
    for j, row in enumerate(remaining[::-1]):
        common = {(item[0]+i, item[1]), (item[0]+i, item[1]-i), (item[0]+i, item[1]+i)} & row
        for match in common:
            remaining[-j-1].remove(match)
        i += 1
    return remaining

def findQueenLocations(queenLocations, remaining):
    if not remaining:
        return True
    elif not all(remaining):
        return None
    else:
        nextrow = list(remaining.pop())

        # sort next row by constraint
        sorter = SorterByConstraint(remaining)
        nextrow.sort(key=sorter)

        # Iterate over intermediary row
        for item in nextrow:
            oldremaining = copy.deepcopy(remaining)

            # Choose next queen and print
            queenLocations.append(item)
            for location in queenLocations:
                print(location[0], location[1])
            print('and')

            # Remove possible queen placements from remaining an print
            remaining = removeItems(item, remaining)
            for row in remaining:
                for location in row:
                    print(location[0], location[1])
            print('done')

            # If remainder is empty then exit
            if findQueenLocations(queenLocations, remaining):
                return True

            # Remove option from queen list and restore remaining list
            queenLocations.pop()
            remaining = oldremaining
        return None



if __name__ == '__main__':
    size = int(next(sys.stdin).rstrip())
    remainingLocations = [{(i, j) for j in range(size-1, -1, -1)} for i in range(size-1, -1, -1)]
    output = findQueenLocations([], remainingLocations)
    print('eof')
    print(output)



