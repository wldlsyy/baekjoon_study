N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def print_visited():
    for i in range(N):
        for j in range(M):
            print(visited[i][j], end=" ")
        print()
class Robot():
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.cnt = 0

    # 현재 칸 청소 가능하면 청소
    def cleanRoom(self):
        if not visited[self.r][self.c] and room[self.r][self.c] == 0:
            # print(f'{(self.r, self.c)} 청소 가능')
            visited[self.r][self.c] = 1
            self.cnt += 1
            # print(f'--청소 완료-- 청소한 칸 개수: {self.cnt}')
            # print_visited()

    # 현재 칸 주변 4칸 중 청소 가능한 구역이 있는지 확인
    def isCleanable(self):
        for i in range(4):
            self.changeDir()
            nr = self.r + dx[self.d]
            nc = self.c + dy[self.d]

            # 청소 가능한 칸 찾기
            if not visited[nr][nc] and room[nr][nc] == 0:
                # print(f'({nr, nc})로 전진 가능. 방향: {self.d}')
                return True
        return False

    def canMoveBackwards(self):
        nr = self.r - dx[self.d]
        nc = self.c - dy[self.d]

        if room[nr][nc] != 1:
            return True
        else:
            # print('Cannot Move')
            return False

    # 방향 유지한 채 한칸 후진
    def moveBack(self):
        self.r = self.r - dx[self.d]
        self.c = self.c - dy[self.d]

    # 방향 유지한 채 한칸 전진
    def moveForward(self):
        self.r = self.r + dx[self.d]
        self.c = self.c + dy[self.d]

    # 반시계 회전
    def changeDir(self):
        self.d = (self.d + 3) % 4
        # print(f'회전된 방향: {self.d}')

    # 로봇의 현재 좌표와 방향 출력
    def printStatus(self):
        print(f'현재 위치: {(self.r, self.c)}, 현재 방향: {self.d}')

robot = Robot(r, c, d)

while True:
    # 동작 1: 현재 칸 청소 가능하면 청소
    robot.cleanRoom()

    # 현재 칸 주변 4칸이 어떤 상태인지 파악
    if robot.isCleanable():
        # 동작 2: 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
        # 반시계 회전해 청소 가능한 위치 찾기
        # 청소 가능한 칸이 있으면 그 방향으로 전진 -> 다시 동작 1로
        robot.moveForward()
        continue

    # 동작 3: 현재 칸 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    else:
        # 4 방향 모두 청소할 수 없을 때 후진 시도
        if robot.canMoveBackwards():
            # 후진 가능하면 후진하고 다시 동작 1로
            robot.moveBack()
            continue
        else:
            # 후진 못하면 작동 종료
            print(robot.cnt)
            break