words = []
for row in range(5):
    words.append(input().rstrip())

for col in range(15):
    for row in range(5):
        try:
            print(words[row][col], end='')
        except:
            continue