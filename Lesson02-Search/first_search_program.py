# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost, debug=False):
    def getTriplet(extension, position):
        return [extension, position[0], position[1]]

    def unpack(triplet):
        return triplet[0], [triplet[1], triplet[2]]

    def getNeighbours(pos):
        neighbours = []
        arrows = []
        for d, arrow in zip(delta, delta_name):
            neighbours.append([pos[0] + d[0], pos[1] + d[1]])
            arrows.append(arrow)
        return neighbours, arrows

    def isSamePosition(pos1, pos2):
        return pos1[0] == pos2[0] and pos1[1] == pos2[1]

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    closed = [[grid[row][col] for col in range(len(grid[0]))] for row in range(len(grid))]
    open = [getTriplet(0, init)]

    previous = [[[] for row in range(len(grid[0]))] for col in range(len(grid))]
    all_arrows = [['X' for row in range(len(grid[0]))] for col in range(len(grid))]

    def popNextValue():
        open.sort()
        open.reverse()
        return open.pop()

    def isInGrid(pos):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    def isOpen(pos):
        return closed[pos[0]][pos[1]] == 0

    def appendNeigbours(g, pos):
        neighbours, arrows = getNeighbours(pos)
        for pos2, arrow in zip(neighbours, arrows):
            if debug:
                print 'Searching ', pos2

            if isInGrid(pos2) and isOpen(pos2):
                g2 = g + cost
                new = getTriplet(g2, pos2)
                if debug:
                    print 'Append list item:'
                    print new
                open.append(new)

                # Close position
                closed[pos2[0]][pos2[1]] = 1

                # Fill helpers
                all_arrows[pos2[0]][pos2[1]] = arrow
                previous[pos2[0]][pos2[1]] = pos
        if debug:
            print 'New open list:'
            for o in open:
                print '    ', o
            print '---'

    iteration = 0

    if debug:
        print 'Initial open list:'
        for o in open:
            print '    ', o
        print '---'

    fail = False
    found = False

    while not fail and not found:

        # If open nodes are empty, it is impossible to find a solution
        if len(open) == 0:
            print 'fail'
            fail = True

        else:
            next = popNextValue()
            g, pos = unpack(next)

            # Close position
            closed[pos[0]][pos[1]] = 1

            # Write expansion
            expand[pos[0]][pos[1]] = iteration
            iteration += 1

            if debug:
                print 'Next item:'
                print '    ', next

            if isSamePosition(pos, goal):
                if debug:
                    print 'Search successful!'
                found = True

            else:
                appendNeigbours(g, pos)

    if debug:
        print 'Expansion:'
        print expand
        print 'Arrows:'
        print all_arrows

    if found:
        path=[[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
        current = goal
        path[goal[0]][goal[1]]='*'

        while not isSamePosition(current, init):
            p=previous[current[0]][current[1]]
            path[p[0]][p[1]]=all_arrows[current[0]][current[1]]
            current=p

        return path


path = search(grid, init, goal, cost, debug=True)

print 'Path:'
print path