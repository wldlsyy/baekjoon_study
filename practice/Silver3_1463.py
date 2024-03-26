n=int(input())
dp=[0]*(n+1) # 앞에서 계산한 결과 담을 리스트

for i in range(2, n+1): # bottom-up 방식
    dp[i] =dp[i-1] + 1 # 현재 수에서 1을 빼는 경우
    # 1을 뺐을 경우와 2 또는 3으로 나누었을 경우 중 최소
    if i % 2 == 0: # 현재 수가 2로 나눠지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 현재 수가 3으로 나눠지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])