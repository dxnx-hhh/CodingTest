N = int(input())
move = list(map(str, input().split()))

walk = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

now = [1, 1]

for i in move:
    if i in walk:
        dx, dy = walk[i]
        x = now[0] + dx
        y = now[1] + dy

        if 0 < x <= N and 0 < y <= N:
            now = [x, y]

print(now[0], now[1])