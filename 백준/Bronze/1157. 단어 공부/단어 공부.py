str = input().lower()
word = list(set(str))
cnt = []

for w in word:
    count = str.count(w)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word[(cnt.index(max(cnt)))].upper())