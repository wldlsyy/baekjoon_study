n = int(input()) # 라운드 수
chang = 100
sang = 100
for _ in range(n):
    # 창영, 상덕
    a, b = map(int, input().split())
    if a>b: # 창영이 상덕을 이기면, 상덕은 창영이 나온 수 만큼 점수 잃음
        sang -= a
    elif a<b:
        chang -= b
    else:
        continue

print(chang)
print(sang)