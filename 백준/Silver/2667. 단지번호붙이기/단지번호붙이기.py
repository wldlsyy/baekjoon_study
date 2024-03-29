n = int(input())
graph=[]
result=[]
for _ in range(n):
    graph.append(list(map(int, input())))

# L, R, D, U
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count=0
def dfs(x, y):
    global count
    if x<0 or x>=n or y<0 or y>=n:
        return

    if graph[x][y] == 1: # 집을 찾으면 개수 증가시키고, 집 없앰
        count+=1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 그래프의 원소가 1인 경우만 dfs로 집 방문
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for r in result:
    print(r)