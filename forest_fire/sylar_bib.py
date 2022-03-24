def newMatrix (size):
    line = []
    for i in range(0,size):
        line.append(0)
    lines = []
    for i in range(0,size):
        lines.append(line.copy())
    return lines


class SuperGraph: 

    def __init__(self, row, col, g): 
        self.ROW = row 
        self.COL = col 
        self.graph = g 

# to check validity of cell
    def isSafe(self, i, j, visited): 
        return (i >= 0 and i < self.ROW and 
                j >= 0 and j < self.COL and 
                not visited[i][j] and self.graph[i][j]) 


    def DFS(self, i, j, visited):

        row = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        col = [-1,  0,  1, -1, 1, -1, 0, 1]; 


        visited[i][j] = True

        # check all 8 neighbours and mark them visited
        # as they will be part of group
        for k in range(8): 
            if self.isSafe(i + row[k], j + col[k], visited): 
                self.DFS(i + row[k], j + col[k], visited) 


    def group(self): 

        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 

        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                # traverse not visited cell
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    self.DFS(i, j, visited) 
                    count += 1

        return count


def addStrength(model, x, y):
    model.st98.append((x+1,y-1))
    model.st98.append((x+1,y))
    model.st98.append((x+1,y+1))
    model.st98.append((x+2,y-2))
    model.st98.append((x+2,y-1))
    model.st98.append((x+2,y))
    model.st98.append((x+2,y+1))
    model.st98.append((x+2,y+2))
    model.st94.append((x+3,y-3))
    model.st94.append((x+3,y-2))
    model.st94.append((x+3,y-1))
    model.st94.append((x+3,y))
    model.st94.append((x+3,y+1))
    model.st94.append((x+3,y+2))
    model.st94.append((x+3,y+3))
    model.st94.append((x+4,y-4))
    model.st94.append((x+4,y-3))
    model.st94.append((x+4,y-2))
    model.st94.append((x+4,y-1))
    model.st94.append((x+4,y))
    model.st94.append((x+4,y+1))
    model.st94.append((x+4,y+2))
    model.st94.append((x+4,y+3))
    model.st94.append((x+4,y+4))
    model.st86.append((x+5,y-5))
    model.st86.append((x+5,y-4))
    model.st86.append((x+5,y-3))
    model.st86.append((x+5,y-2))
    model.st86.append((x+5,y-1))
    model.st86.append((x+5,y))
    model.st86.append((x+5,y+1))
    model.st86.append((x+5,y+2))
    model.st86.append((x+5,y+3))
    model.st86.append((x+5,y+5))
    model.st86.append((x+6,y-6))
    model.st86.append((x+6,y-5))
    model.st86.append((x+6,y-4))
    model.st86.append((x+6,y-3))
    model.st86.append((x+6,y-2))
    model.st86.append((x+6,y-1))
    model.st86.append((x+6,y))
    model.st86.append((x+6,y+1))
    model.st86.append((x+6,y+2))
    model.st86.append((x+6,y+3))
    model.st86.append((x+6,y+5))
    model.st86.append((x+6,y+6))
    model.st70.append((x+7,y-7))
    model.st70.append((x+7,y-6))
    model.st70.append((x+7,y-5))
    model.st70.append((x+7,y-4))
    model.st70.append((x+7,y-3))
    model.st70.append((x+7,y-2))
    model.st70.append((x+7,y-1))
    model.st70.append((x+7,y))
    model.st70.append((x+7,y+1))
    model.st70.append((x+7,y+2))
    model.st70.append((x+7,y+3))
    model.st70.append((x+7,y+5))
    model.st70.append((x+7,y+6))
    model.st70.append((x+7,y+7))
    model.st40.append((x+8,y-6))
    model.st40.append((x+8,y-5))
    model.st40.append((x+8,y-4))
    model.st40.append((x+8,y-3))
    model.st40.append((x+8,y-2))
    model.st40.append((x+8,y-1))
    model.st40.append((x+8,y))
    model.st40.append((x+8,y+1))
    model.st40.append((x+8,y+2))
    model.st40.append((x+8,y+3))
    model.st40.append((x+8,y+5))
    model.st40.append((x+8,y+6))