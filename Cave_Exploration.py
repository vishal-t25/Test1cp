grid_size = int(input())

grid = [[[0] for _ in range(grid_size)]for _ in range(grid_size)]
flood = [[[0] for _ in range(grid_size)]for _ in range(grid_size)]



for i in range(grid_size):
    line = list(map(int,input().split()))

    for j in range(grid_size):
        grid[i][j] = line[j]


flood[0][0] = 1

flooded = set()
flooded.add((0,0))


directions = [(0,1),(0,-1),(1,0),(-1,0)]
def flood1(h,x,y):

    for dr,dc in directions:
        new_x = x + dr
        new_y = y + dc

        if 0<=new_x< grid_size and 0<=new_y< grid_size and flood[new_x][new_y] != 1 and grid[new_x][new_y] < h:
            flood[new_x][new_y] = 1
            flooded.add((new_x,new_y))
            if new_x == grid_size - 1 and new_y == grid_size - 1:
                print(h-1)
                return
            flood1(h,new_x,new_y)


curr_water_height = 1
while flood[grid_size-1][grid_size-1] != 1:
    copy_flooded = flooded
    for x,y in copy_flooded:
        flood1(curr_water_height, x, y)