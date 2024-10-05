# 입력받기
T = int(input())
s = dict()
s['Y'] = [[0 for _ in range(9)] for _ in range(T)]
s['K'] = [[0 for _ in range(9)] for _ in range(T)]

for i in range(T):
    for j in range(9):
        y, k = map(int, input().split())
        s['Y'][i][j] = y
        s['K'][i][j] = k

for i in range(T):
    ys = sum(s['Y'][i])
    ks = sum(s['K'][i])

    if ys > ks:
        print("Yonsei")
    elif ys < ks:
        print("Korea")
    else:
        print("Draw")