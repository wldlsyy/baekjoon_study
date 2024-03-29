alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
answer = [-1 for i in range(26)]
str = input()

for i in range(len(str)):
    for j in range(len(alphabet)):
        if answer[j] != -1:
            continue
        if str[i] == alphabet[j]:
            answer[j] = i

for v in answer:
    print(v, end=" ")