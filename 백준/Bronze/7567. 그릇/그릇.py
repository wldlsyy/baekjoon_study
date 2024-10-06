# 그릇 문자열 입력받기
s = input()
prev = s[0]
total = 10 # 처음 놓는 그릇은 10으로 시작

for i in range(1, len(s)):
    if prev == s[i]:
        total += 5
    else:
        total += 10
    prev = s[i]

print(total)