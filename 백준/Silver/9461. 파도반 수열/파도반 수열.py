t = int(input())

array = []
for _ in range(t):
    n = int(input())
    array.append(n)


d = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(100):
    if i < 10:
        continue
    d.append(d[i-1] + d[i-5])

for seq in array:
    print(d[seq -1])