from collections import deque
def bfs():
    q = deque([start])
    visited[start[0]][start[1]] = 1 # 시작 지점 방문 표시

    while q:
        curr = q.popleft()

        for i in range(4):
            next_x = curr[0] + dx[i]
            next_y = curr[1] + dy[i]

            # 경계 검사: 맵 벗어나는지
            if next_x < 1 or next_y < 1 or next_x > n or next_y > m:
                continue
            # 종료 조건: 목적지에 도착한 경우
            if next_x == n and next_y == m:
                #print("Found Path")
                print(visited[curr[0]][curr[1]] + 1)  # 현재 위치에서 1을 더한 값을 출력
                return

            # 갈 수 없는 경로
            if map[next_x][next_y] == 0 or visited[next_x][next_y] != 0:
                #print("cannot pass: ", next_x, next_y)
                continue
            #print("next path: ", next_x, next_y)
            # 갈 수 있는 경로는 스택에 넣고 방문 표시
            q.append([next_x, next_y])
            # 칸 수 세기 위해, 그 이전에 방문 표시 했던 값에 1 더해줌
            visited[next_x][next_y] = visited[curr[0]][curr[1]] + 1

# 입력받기
n, m = map(int, input().split())
# map: (n x m) 배열
map = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    s = input()
    for j in range(1, m+1):
        map[i][j] = int(s[j-1])

# 방향 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start = [1, 1]
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
bfs()