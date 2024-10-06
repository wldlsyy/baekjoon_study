n, k = map(int, input().split())

room = [] # (s, y, count)
for i in range(n):
    s, y = map(int, input().split())
    if i == 0: # 첫 친구 방 하나에 배정
        room.append([s, y, 1])
    else:
        found = False
        for j in range(0, len(room)):
            if s == room[j][0] and y == room[j][1] and room[j][2] < k:
                room[j][2] += 1
                found = True
                break

        if found == False:
            room.append([s, y, 1])

print(len(room))