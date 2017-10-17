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


def search(grid, init, goal, cost, debug = False):
    def getTriplet(extension, position):
        return [extension, position[0], position[1]]

    def unpack(triplet):
        return triplet[0], [triplet[1], triplet[2]]

    def popNextValue(open):
        open.sort()
        open.reverse()
        return open.pop()

    def getNeighbours(pos):
        neighbours = []
        for d in delta:
            neighbours.append([pos[0] + d[0], pos[1] + d[1]])
        return neighbours

    def isSamePosition(pos1, pos2):
        return pos1[0] == pos2[0] and pos1[1] == pos2[1]

    def isInGrid(pos, grid):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

    def isOpen(pos, closed):
        return closed[pos[0]][pos[1]] == 0

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    closed = [[grid[row][col] for col in range(len(grid[0]))] for row in range(len(grid))]
    open = [getTriplet(0, init)]

    iteration = 0

    if debug:
        print 'Initial open list:'
        for o in open:
            print '    ', o
        print '---'

    while True:

        # If open nodes are empty, it is impossible to find a solution
        if len(open) == 0:
            print 'fail'
            return expand

        next = popNextValue(open)
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
            return expand

        neighbours = getNeighbours(pos)
        for pos2 in neighbours:
            if debug:
                print 'Searching ', pos2

            if isInGrid(pos2, grid) and isOpen(pos2, closed):
                g2 = g+cost
                new = getTriplet(g2, pos2)
                if debug:
                    print 'Append list item:'
                    print new
                open.append(new)

                # Close position
                closed[pos2[0]][pos2[1]] = 1

        if debug:
            print 'New open list:'
            for o in open:
                print '    ', o
            print '---'

expand = search(grid, init, goal, cost, debug=True)

print 'Expansion:'
print expand