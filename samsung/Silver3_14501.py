from collections import deque
N = int(input()) # N일 동안 상담, N+1일째 퇴사
schedule = []

for i in range(N):
    t, p = map(int, input().rstrip().split())
    schedule.append([t, p])

max_profit = 0
for i in range(N):
    q = deque()
    q.append(schedule[i - 1])
    curr_profit = 0
    time = i+1

    while q:
        t, p = q.popleft()
        time += t
        if time > N+1:
            break

        curr_profit += p
        q.append(schedule[time-1])

    max_profit = max(max_profit, curr_profit)

print(max_profit)
