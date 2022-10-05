import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) != 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    c = a + b

    result += c
    heapq.heappush(q, c)

print(result)