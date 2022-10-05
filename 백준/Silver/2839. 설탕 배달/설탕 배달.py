n = int(input()) + 1

d = [-1] * 5001
d[3] = 1
d[5] = 1
for x in range(3,n):
    if d[x -3] != -1 and d[x-5] == -1:
        d[x] = d[x-3]+1
    if d[x-3] == -1 and d[x-5] != -1:
        d[x] = d[x-5] + 1
    if d[x-3] != -1 and d[x-5] != -1:
        d[x] = min(d[x-3]+1, d[x-5]+1)

print(d[x])