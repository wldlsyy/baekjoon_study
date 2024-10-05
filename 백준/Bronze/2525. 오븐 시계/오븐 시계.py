curr_h, curr_m = map(int, input().split())
time = int(input())

h = time//60 # 걸리는 시간
m = time%60 # 걸리는 분

t_h = curr_h + h
t_m = curr_m + m

if t_m>=60:
    t_h+=t_m//60
    t_m = t_m%60
if t_h>=24:
    t_h = t_h-24

print(t_h, t_m)