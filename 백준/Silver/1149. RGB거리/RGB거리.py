n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))



INF = int(1e9)
costs = [[INF, INF, INF] for _ in range(n)]

for i in range(n):
    for j in range(3):
        if i == 0:
            costs[i][j] = array[i][j]
        else:
            min_cost = INF
            if j == 0:
                min_cost = min(costs[i-1][1], costs[i-1][2])
            elif j == 1:
                min_cost = min(costs[i-1][0], costs[i-1][2])
            elif j == 2:
                min_cost = min(costs[i-1][0], costs[i-1][1])
            costs[i][j] = array[i][j] + min_cost

print(min(costs[n-1]))