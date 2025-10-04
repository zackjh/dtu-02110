# Optimised by ChatGPT
import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
x = next(it)
prices = [next(it) for _ in range(n)]
pages = [next(it) for _ in range(n)]

dp = [0] * (x + 1)

for p, s in zip(prices, pages):
    # j goes from x down to p; no inner if needed
    for j in range(x, p - 1, -1):
        v = dp[j - p] + s
        if v > dp[j]:
            dp[j] = v

print(dp[x])  # same as max(dp), but dp[x] is fine here

# My original code - gets TLE on test cases 6-11, 13, and 15
# n, x = map(int, input().split())
# prices = list(map(int, input().split()))
# pages = list(map(int, input().split()))

# dp = [0] * (x + 1)
# for i in range(n):
#     for j in range(x, 0, -1):
#         if prices[i] <= j:
#             dp[j] = max(dp[j], pages[i] + dp[j - prices[i]])

# print(dp[-1])
