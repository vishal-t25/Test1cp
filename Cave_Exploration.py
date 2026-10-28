import sys
from collections import deque
input = sys.stdin.readline

def main():

    grid_size = int(input())

    N = grid_size - 1

    grid = [[0 for _ in range(grid_size)]for _ in range(grid_size)]

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def bfs(h):
        if h <= grid[N][N]:
            return False
        x = 0
        y = 0

        q = deque()

        q.append([x,y])
        seen = [[0 for _ in range(grid_size)]for _ in range(grid_size)]
        while q:
            x,y = q.popleft()

            if x == N and y == N:
                return True
            
            for dr,dc in directions:
                new_x = x + dr
                new_y = y + dc

                if 0<=new_x <= N and 0<=new_y<= N and grid[new_x][new_y] < h and not seen[new_x][new_y]:
                    q.append([new_x,new_y])
                    seen[new_x][new_y] = 1

        return False 



    for i in range(grid_size):
        line = list(map(int,input().split()))

        for j in range(grid_size):
            grid[i][j] = line[j]

    curr_water_height = grid[N][N] + 1
    while not bfs(curr_water_height):
        curr_water_height += 1

    print(curr_water_height-1)
    
main()
    








'''
def main():
    grid_size = int(input())

    grid = [[0 for _ in range(grid_size)]for _ in range(grid_size)]
    visited = [[0 for _ in range(grid_size)]for _ in range(grid_size)]



    for i in range(grid_size):
        line = list(map(int,input().split()))

        for j in range(grid_size):
            grid[i][j] = line[j]


    visited[0][0] = 1

    print(visited)


    flooded = set()
    flooded.add((0,0))


    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    def flood(h,x,y):

        for dr,dc in directions:
            new_x = x + dr
            new_y = y + dc

            if 0<=new_x < grid_size and 0<=new_y< grid_size and visited[new_x][new_y] != 1 and grid[new_x][new_y] < h:
                visited[new_x][new_y] = 1
                flooded.add((new_x,new_y))
                if new_x == grid_size - 1 and new_y == grid_size - 1:
                    print(h-1)
                    return
                flood(h,new_x,new_y)
        
        return


    curr_water_height = 1
    while visited[grid_size-1][grid_size-1] != 1:
        copy_flooded = flooded
        for x,y in copy_flooded:
            flood(curr_water_height, x, y)

main()
'''
