# 입력받기
T = int(input())
result = [0] * T

for i in range(T):
    ys = 0
    ks = 0
    for j in range(9):
        y, k = map(int, input().split())
        ys += y
        ks += k

    if ys > ks:
        result[i] = 1
    elif ys < ks:
        result[i] = 2
    else:
        result[i] = 0

for r in result:
    if r == 1:
        print("Yonsei")
    elif r == 2:
        print("Korea")
    else:
        print("Draw")