import collections

# Mert Doğru
# 160302016

# Maze2
# Map Info
map_information = {
    (1, 1): "W",
    (2, 3): "W",
    (0, 5): "W",
    (4, 3): "W",
    (2, 7): "W",
    (5, 7): "W",
    (5, 6): "W",
    "information": {
        "rows": 6,
        "columns": 8,
        "start": (2, 1),
        "end": (0, 7)
    }
}


def createDefault2DMatrix(rows, columns):
    doubleMatrix = []
    for rowIndex in range(0, rows):
        rowMatrix = []
        for column in range(0, columns):
            rowMatrix.append(" ")
        doubleMatrix.append(rowMatrix)
        del rowMatrix
    return doubleMatrix


def createMatrix():
    # Create two dimension array with spaces.
    map = createDefault2DMatrix(map_information["information"]["rows"], map_information["information"]["columns"])
    for cordinants in map_information.keys():
        # Get just cordinants looking with type of data on the dictionary.
        if type(cordinants) == tuple:
            map[cordinants[0]][cordinants[1]] = map_information[cordinants]

    # Add Start location
    map[map_information["information"]["start"][0]][map_information["information"]["start"][1]] = "S"
    # Add End Location
    map[map_information["information"]["end"][0]][map_information["information"]["end"][1]] = "E"
    # Return created matrix
    return map


def bfs(grid, start):
    # Breadth First Search Algorithm
    # Control Keys
    wall, clear, end = "W", ' ', "E"
    # Limits of matrix
    width, height = map_information["information"]["columns"], map_information["information"]["rows"]
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == end:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= y2 < width and 0 <= x2 < height and grid[x2][y2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def printMaze(Maze):
    # For printing Maze
    for i in Maze:
        print(i)


# Create Maze
myMap = createMatrix()
# Print Maze
printMaze(myMap)
# Find Path
path = bfs(myMap, map_information["information"]["start"])
print("----------------------------------------")
# Print Path
print(path)
