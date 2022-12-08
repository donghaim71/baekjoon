'''
증가하거나
감소하는
연속합
'''

n = int(input())
array = list(map(int, input().split()))

# [증가합, 감소합]
d = [0 for _ in range(n)]


for i in range(n):
    # d[i-1] + array[i]가 array[i]보다 작다면 d[i]는 array[i]
    d[i] = max(d[i-1] + array[i], array[i])

print(max(d))