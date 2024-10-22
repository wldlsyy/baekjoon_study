N, L = map(int, input().split()) # 과일 개수, 초기 길이
fruits = list(map(int, input().split()))
fruits.sort()

for f in fruits:
    if f <= L:
        # 먹을 수 있음
        L += 1 # 과일 먹고 길이 증가

print(L)