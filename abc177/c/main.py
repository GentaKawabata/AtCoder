# answer = ((a0 + ... + aN)^2 - (a0^2 + ... + aN^2)) // 2
# answer = answer % MOD

MOD = int(1e9) + 7

N = int(input())
A = list(map(int, input().split()))


S_A = sum(A)
S2 = sum(map(lambda x: x * x, A))
ans = ((S_A * S_A - S2) // 2) % MOD

print(ans)
