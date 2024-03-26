class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
# 외적 계산
def cross_product(p1, p2):
    return (p1.x * p2.y) - (p1.y * p2.x)
def main():
    K = int(input())  # 참외 개수
    start = Point(0, 0)  # 시작 좌표
    points = [start]  # 첫 좌표 넣고 시작

    for _ in range(6):  # 육각형이니까
        dir, len = map(int, input().split())

        next_point = Point(start.x, start.y)
        if dir == 1:  # 동쪽
            next_point.x += len
        elif dir == 2:  # 서쪽
            next_point.x -= len
        elif dir == 3:  # 남쪽
            next_point.y -= len
        elif dir == 4:  # 북쪽
            next_point.y += len
        points.append(next_point)
        start = next_point  # 다음 시작점 설정

    # CCW 구하고
    ccw = 0
    for i in range(6):
        j = (i + 1) % 6
        ccw += cross_product(points[i], points[j])

    # 면적 구하기 -> CCW / 2
    area = abs(ccw) / 2
    print(int(area * K))


if __name__ == "__main__":
    main()
