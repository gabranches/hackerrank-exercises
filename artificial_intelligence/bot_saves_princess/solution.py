#!/usr/bin/python

def get_pos(grid, x):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == x:
                return (row, col)

def find_path(x, y, grid):
    x_pos = (get_pos(grid, x))
    y_pos = (get_pos(grid, y))
    return [x_pos[0] - y_pos[0], x_pos[1] - y_pos[1]]
    
def displayPathtoPrincess(n,grid):
    path = find_path('p', 'm', grid)
    
    while path[0] != 0 and path[1] != 0:
        if path[0] < 0:
            print("UP")
            path[0] += 1
        if path[0] > 0:
            print("DOWN")
            path[0] -= 1
        if path[1] < 0:
            print("LEFT")
            path[1] += 1
        if path[1] > 0:
            print("RIGHT")
            path[1] -= 1  
     
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
    
displayPathtoPrincess(m,grid)
