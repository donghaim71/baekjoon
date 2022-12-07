n = int(input())

array = list(map(int, input().split()))

d = [1 for _ in range(n)]
for i in range(n):
    now = array[i]
    
    for j in range(i):
        prev = array[j]
        if prev < now:
            d[i] = max(d[i], d[j] + 1)

print(max(d))