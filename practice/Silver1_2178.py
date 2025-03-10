n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    info = input().rstrip()
    for char in info:
        graph[i].append(int(char))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_path = float('inf')
def dfs(start, count):
    global min_path
    x, y = start

    if x==n-1 and y==m-1: # (N, M) 위치에 도착
        min_path = min(min_path, count)
        return

    if count>=min_path: # 이미 최단 경로 찾음
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if visited[nx][ny] == 1 or graph[nx][ny] == 0:
            continue
        visited[nx][ny] = 1
        dfs((nx, ny), count+1)
        visited[nx][ny] = 0

start = (0, 0)
visited[0][0] = 1
dfs(start, 1)
print(min_path)
