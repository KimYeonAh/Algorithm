def isSafe( maze, x, y, mark ) :
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y >= 0 and y < H :
        if maze[y][x] != 0 and mark[y][x] == 0 :
            return True
    
    return False

def solve_maze( maze, x, y ) :
    W, H = len(maze[0]), len(maze)
    sol = [[0 for j in range(W)] for i in range(H)]
    mark = [[0 for j in range(W)] for i in range(H)]

    if DFS_maze(maze, x, y, sol, mark) == False :
        print("출구를 찾을 수 없음")
    else :
        for i in sol : print(i)

maze = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solve_maze(maze, 3, 0)