from collections import deque

def allclusters(model):
    return model.cluster_count

def clusterssize(model):
    try:
        return model.count_type(model, "Fine") + model.count_type(model, "Protected") + model.count_type(model, "Sprinkler") / model.cluster_count
    except:
        return 0

def statefine(model):
    return model.count_type(model, "Fine")

def stateprotected(model):
    return model.count_type(model, "Protected") + model.count_type(model, "Sprinkler")

def statefire(model):
    return model.count_type(model, "On Fire")

def stateburned(model):
    return model.count_type(model, "Burned Out")


def newMatrix (size):
    line = []
    for i in range(0,size):
        line.append(0)
    lines = []
    for i in range(0,size):
        lines.append(line.copy())
    return lines


row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
def isSafe(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed[0])) and \
           mat[x][y] == 1 and not processed[x][y]
 
def BFS(mat, processed, i, j):
 
    q = deque()
    q.append((i, j))
    processed[i][j] = True
 
    while q:
        x, y = q.popleft()
 
        for k in range(len(row)):
            if isSafe(mat, x + row[k], y + col[k], processed):
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))
 
def countIslands(mat):
    if not mat or not len(mat):
        return 0
 
    (M, N) = (len(mat), len(mat[0]))
    processed = [[False for x in range(N)] for y in range(M)]
 
    island = 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                island = island + 1
 
    return island


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