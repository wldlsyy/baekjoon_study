h, m = map(int, input().split())
cooking_time = int(input())

time = cooking_time + m
new_h = h + time//60 # 시
new_m = time%60 # 분
if new_h>23:
    new_h = new_h%24
    print(new_h, new_m)
else:
    print(new_h, new_m)