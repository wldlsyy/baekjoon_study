from collections import deque
# 입력 받기
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 북, 동, 남, 서 -> d로 들어오는 값이 인덱스가 됨!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rear(x, y, d):
    # 바라보는 방향 기준, 뒤쪽으로 이동된 좌표 반환
    if d == 0: # 북 -> 남
        nx = x + dx[2]
        ny = y + dy[2]
    elif d == 1: # 동 -> 서
        nx = x + dx[3]
        ny = y + dy[3]
    elif d == 2: # 남 -> 북
        nx = x + dx[0]
        ny = y + dy[0]
    else: # 서 -> 동
        nx = x + dx[1]
        ny = y + dy[1]
    return nx, ny

def change_dir(d):
    # 반시계 방향 90도 회전
    dir = {0: 3, 3: 2, 2: 1, 1: 0}

    return dir[d]

def find_next_cleanable(x, y, d, visited):
    #print(f'현재 방향: {d}')
    for i in range(4):
        d = change_dir(d) # 반시계 방향으로 회전
        nx = x + dx[d]
        ny = y + dy[d]

        # 청소 가능한 칸
        if not visited[nx][ny] and room[nx][ny] != 1:
            #print(f'({nx, ny})로 전진 가능. 방향: {d}')
            return nx, ny, d

    return None

def bfs(r, c, d):
    q = deque([(r, c, d)])
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0 # 청소하는 칸 카운트
    while q:
        x, y, d = q.popleft()
        #print(f'현재 위치와 방향: ({x, y}), {d}')

        # 동작 1: 현재 칸 청소 가능하면 청소
        if room[x][y] == 0 and not visited[x][y]: # 현재 위치가 청소되지 않은 칸이면
            #print(f'({x, y}) 청소 가능')
            visited[x][y] = True # 현재 칸 청소
            cnt += 1
            #print(f'--청소 완료-- 청소한 칸 개수: {cnt}')

        # 현재 칸 주변 4칸이 어떤 상태인지 파악
        # 동작 2: 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 있는지 확인
        next_cleanable = find_next_cleanable(x, y, d, visited)

        if next_cleanable:
            # 청소 가능한 칸이 있으면 전진
            nx, ny, nd = next_cleanable
            q.append((nx, ny, nd))
        else:
            # 4방향 모두 청소할 수 없을 때 후진
            rx, ry = rear(x, y, d)
            #print(f'({rx, ry})로 후진 가능한지 확인')

            if room[rx][ry] == 1:
                #print(f'({rx, ry})로 후진 불가능 -> 작동 종료')
                return cnt
            else:
                #print(f'({rx, ry})로 후진')
                q.append((rx, ry, d))

    return cnt

result = bfs(r, c, d)
print(result)