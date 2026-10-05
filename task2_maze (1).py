maze = [
    "##########",
    "#A   #   #",
    "# ## # # #",
    "# #    # #",
    "# # #### #",
    "#   #  # #",
    "### # ## #",
    "#   #   B#",
    "##########",
]

grid = []
for row in maze:
    grid.append(list(row))

start = None
goal = None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "A":
            start = (r, c)
        if grid[r][c] == "B":
            goal = (r, c)

frontier = [start]          
seen = [start]                
parent = {start: None}     
explored = 0              
found = False

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while len(frontier) > 0:
    cell = frontier.pop(0) 
    explored = explored + 1

    if cell == goal:          
        found = True
        break

    row, col = cell
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        new_cell = (new_row, new_col)

        inside = 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
        if inside and grid[new_row][new_col] != "#" and new_cell not in seen:
            seen.append(new_cell)
            parent[new_cell] = cell
            frontier.append(new_cell)

if not found:
    print("No path from A to B")
else:
    path = []
    cell = goal
    while cell is not None:
        path.append(cell)
        cell = parent[cell]
    path.reverse()


    for r, c in path[1:-1]:
        grid[r][c] = "*"

    print("Maze with path:")
    for row in grid:
        print("".join(row))
    print()
    print("Explored cells:", explored)
    print("Path length:", len(path) - 1, "steps")
    print("Final path:", path)
