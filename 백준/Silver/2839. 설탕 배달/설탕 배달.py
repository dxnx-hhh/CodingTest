N = int(input())
suger = 0

while N % 5 != 0:

    if N > 0:
        N -= 3
        suger += 1
    elif N < 0:
        N = -1
        break

if N == -1: print(-1)
else: print(suger + int(N / 5))