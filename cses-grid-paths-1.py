def solve():
    MOD = 10**9 + 7
    N = int(input())
    dp = [0] * N
    for i in range(N):
        row = input()
        for j in range(N):
            if row[j] == "*":
                dp[j] = 0
            else:
                if i == 0 and j == 0:
                    dp[0] = 1
                elif j > 0:
                    dp[j] = (dp[j - 1] + dp[j]) % MOD
    print(dp[-1] % MOD)


solve()
