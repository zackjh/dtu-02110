n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0] * (x + 1)
for i in range(n):
    for j in range(x, 0, -1):
        if prices[i] <= j:
            dp[j] = max(dp[j], pages[i] + dp[j - prices[i]])

print(dp[-1])
