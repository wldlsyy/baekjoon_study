def cal_score(str):
    score = [0]*len(str)

    for i in range(len(str)):
        if str[i] == "X":
            score[i] = 0
        if str[i] == "O":
            if i-1 < 0:
                score[i] = 1
                continue
            if str[i-1] == "O":
                score[i] = score[i-1]+1
            else:
                score[i] = 1

    print(sum(score))

# 입력받기
T = int(input())
strings = []
for i in range(T):
    str = input()
    strings.append(str)

for i in range(T):
    cal_score(strings[i])