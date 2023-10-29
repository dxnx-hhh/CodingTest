N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

result = 0

for i in range(len(A)):
    bigB = max(B)
    result += A[i] * bigB

    B.remove(bigB)

print(result)
