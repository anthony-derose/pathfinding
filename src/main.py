class Grid:
    def __init__(self, grid, visited):
        self.grid = grid 
        self.visited = visited
    
    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end=' ')
            print()
    
    def get_grid(self):
        return self.grid
            
def dfs(g, current, start, end, visited, order):
    grid1 = g.get_grid()
    startx, starty = start[0], start[1]
    visited[startx][starty] = True 
    
    x = current[0]
    y = current[1]
    grid1[x][y] = order
    
    if x == end[0] and y == end[1]:
        grid1[start[0]][start[1]] = 'S'
        grid1[x][y] = 'E'
        visited[x][y] = True
        g.print_grid()
        return 
    
    neighbors = get_valid_neighbors(grid1, x, y, visited)
    for n in neighbors:
        if visited[n[0]][n[1]] == False:
            visited[n[0]][n[1]] = True
            dfs(g, n, start, end, visited, order+1)

def bfs(g, start, end, visited):
    grid1 = g.get_grid()
    queue = []
    order = 0
    
    queue.append(start)
    startx, starty = start[0], start[1]
    endx, endy = end[0], end[1]
    
    while queue:
        temp = queue.pop(0)
        x = temp[0]
        y = temp[1]
        
        if x == endx and y == endy:
            grid1[startx][starty] = 'S'
            grid1[x][y] = 'E'
            visited[x][y] = True
            g.print_grid()
        
        if visited[x][y] is True:
            continue
        visited[x][y] = True
        grid1[x][y] = order
        order+=1
        neighbors = get_valid_neighbors(grid1, x, y, visited)
        
        for n in neighbors:
            queue.append(n)
    
def get_valid_neighbors(grid, x, y, visited):
    neighbors = []
    
    if x > 0 and not visited[x-1][y]:
        neighbors.append([x-1,y])
    if y > 0 and not visited[x][y-1]:
        neighbors.append([x,y-1])
    if x < len(grid) - 1 and visited[x+1][y] is False:
        neighbors.append([x+1,y])
    if y < len(grid[0]) - 1 and visited[x][y+1] is False:
        neighbors.append([x,y+1])
    return neighbors

def main():
    grid1 = [
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['-','-','-','-','-'],
    ]

    start = [0,0]
    end = [0,3]
    visited = [[False for _ in range(len(grid1))] for _ in range(len(grid1[0]))]
    g = Grid(grid1, visited)
    dfs(g, start, start, end, visited, 0)

    #bfs(g, start, end, visited)

if __name__ == "__main__":
    main()