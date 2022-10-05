import sys
import heapq

input = sys.stdin.readline

n = int(input())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def check(parent, a, b):
    if find_parent(parent, a) != find_parent(parent, b):
        return True
    else:
        return False


def check(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return False
    else:
        return True



parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i


x = []
y = []
z = []
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

edges = []
for i in range(n - 1):
    heapq.heappush(edges, (x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    heapq.heappush(edges, (y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    heapq.heappush(edges, (z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

total = 0
while edges:
    dist, a, b = heapq.heappop(edges)
    if check(parent, a, b):
        total += dist
        union_parent(parent, a, b)
print(total)