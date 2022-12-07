t = int(input())

array = []
for _ in range(t):
    array.append(int(input()))
    

d = [0, 1, 2, 4]


for i in range(4,11):
    d.append(d[i-1] + d[i-2] + d[i-3])


for i in array:
    print(d[i])