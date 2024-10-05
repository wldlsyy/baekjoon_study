def cal_score(str):
    # 이전에 연속된 O의 개수
    count_o = 0
    # 전체 점수
    total = 0

    for i in range(len(str)):
        if str[i] == "X":
            count_o = 0
            continue
        else:
            count_o += 1
            total += count_o

    print(total)

# 입력받기
T = int(input())
strings = []
for i in range(T):
    str = input()
    strings.append(str)

for i in range(T):
    cal_score(strings[i])