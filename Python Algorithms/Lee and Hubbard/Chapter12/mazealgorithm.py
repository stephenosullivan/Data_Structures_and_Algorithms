__author__ = 'stephenosullivan'

import sys
from heapq import heappush, heappop
# output piped to mazeanimate
# Use stderr for diagnostics
# sys.stderr.write('Your text goes here.\n')

# front-end    back-end
#   dfs --------->     # A search type is selected, the back-end program must read
#   maze.txt ---->     # The filename is passed to the back-end program
#   <----------- 0 10  # these are the row column pairs of visited locations
#   ...                # repeating until the search is complete
#   <----------- done  # Then done is printed by the back-end
#   <----------- 31 22 # Finally the path is printed in reverse order
#   ...                # All locations are printed
#   <----------- eof   # EOF is printed back to be sent back to this application.


def neighbors(maze, x, y):
    s = {(x+1, y), (x, y-1), (x-1, y), (x, y+1)}
    neighbors_within_bounds = {(i, j) for i, j in s if 0 <= i < len(maze) and 0 <= j < len(maze[0])}
    return neighbors_within_bounds

def dfs(maze, start, end):
    stack = [[start]]
    visited = set()
    cnt = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            print(node[0], node[1], cnt, flush=True)
            for neighbor in neighbors(maze, node[0], node[1]) - visited:
                if neighbor == end:
                    print(neighbor[0], neighbor[1], cnt + 1, flush=True)
                    return path[:-1] + [(node, cnt)] + [(neighbor, cnt+1)]
                elif maze[neighbor[0]][neighbor[1]] == ' ':
                    stack.append(path[:-1] + [(node, cnt)]+ [neighbor])
            cnt += 1
    return [[]]

from queue import deque
def bfs(maze, start, stop):
    visited = set()
    nodequeue = deque()
    nodequeue.append([start])
    cnt = 0
    while nodequeue:
        path = nodequeue.popleft()
        current = path[-1]
        if current not in visited:
            visited.add(current)
            print(current[0], current[1], cnt)
            for neighbor in neighbors(maze, current[0], current[1]) - visited:
                if neighbor == stop:
                    print(neighbor[0], neighbor[1], cnt+1)
                    return path[:-1] + [(current, cnt)] + [(neighbor, cnt)]
                elif maze[neighbor[0]][neighbor[1]] == ' ':
                    nodequeue.append(path[:-1] + [(current, cnt)] + [neighbor])
            cnt += 1

    return [[]]

def hill(maze, start, stop):
    visited = set()
    stack = [[start]]
    cnt = 0
    while stack:
        path = stack.pop()
        current = path[-1]
        if current not in visited:
            visited.add(current)
            print(current[0], current[1], cnt)
            for neighbor in sorted(neighbors(maze, current[0], current[1]), key=lambda node: manhattan(node, stop), reverse=True):
                if neighbor == stop:
                    print(neighbor[0], neighbor[1], cnt+1)
                    return path[:-1] + [(current, cnt)] + [(neighbor, cnt+1)]
                elif maze[neighbor[0]][neighbor[1]] == ' ':
                    stack.append(path[:-1] + [(current, cnt)] + [neighbor])
        cnt += 1

    return [[]]

def best(maze, start, end):
    visited = set()
    node_queue = []
    cnt = 0
    heappush(node_queue, (manhattan(start, end), cnt, [start]))
    while node_queue:
        _, _, path = heappop(node_queue)
        current = path[-1]
        if current not in visited:
            print(current[0], current[1], cnt)
            visited.add(current)
            if current == end:
                return path[:-1] + [(current, cnt)]
            for neighbor in neighbors(maze, current[0], current[1]):
                if maze[neighbor[0]][neighbor[1]] == ' ':
                    heappush(node_queue, (manhattan(neighbor, end), cnt, path[:-1] + [(current, cnt)] + [neighbor]))
            cnt += 1
    return [[]]

def astar(maze, start, end):
    visited = set()
    node_queue = []
    cnt = 0
    heappush(node_queue, (totaldist(0, start, end), cnt, [start]))
    while node_queue:
        _, _, path = heappop(node_queue)
        current = path[-1]
        if current not in visited:
            print(current[0], current[1], cnt)
            visited.add(current)
            if current == end:
                return path[:-1] + [(current, cnt)]
            for neighbor in neighbors(maze, current[0], current[1]):
                if maze[neighbor[0]][neighbor[1]] == ' ':
                    heappush(node_queue, (totaldist(len(path), neighbor, end), cnt, path[:-1] + [(current, cnt)] + [neighbor]))
            cnt += 1
    return [[]]



def manhattan(start, end):
    return abs(end[1] - start[1]) + abs(end[0] - start[0])

def totaldist(length, current, end):
    return length + manhattan(current, end)


def findMazeEntry(maze):
    for i, elem in enumerate(maze[0]):
        if elem == ' ':
            return 0, i

def findMazeExit(maze):
    for i, elem in enumerate(maze[-1]):
        if elem == ' ':
            return len(maze)-1, i



if __name__ == '__main__':
    a = []
    # for line in sys.stdin:
    #     a.append(line)
    #     sys.stderr.write(line + '\n')
    #
    search = next(sys.stdin).rstrip()
    mazefile = next(sys.stdin).rstrip()

    with open(mazefile) as f:
        firstLine = f.readline()
        rows = int(firstLine)
        secondLine = f.readline()
        cols = int(secondLine)
        maze = []
        for i in range(rows):
            line = f.readline()
            maze.append(line)

        mazeentry = findMazeEntry(maze)
        mazeexit = findMazeExit(maze)
        sys.stderr.write(str((mazeentry, mazeexit)))

    sys.stderr.write(search)
    searchfunc = eval(search)


    path = searchfunc(maze, mazeentry, mazeexit)

    print('done', flush=True)
    sys.stderr.write('done\n')

    length = len(path) - 1
    for node in path[::-1]:
        sys.stderr.write(str((node, length)) + '\n')
        print(node[0][0], node[0][1], node[1], flush=True)
        length -= 1


    sys.stderr.write('done\n')
    print('eof', flush=True)


    # if s == 'dfs':
    #     pass
