from collections import deque

n = int(input())

graph = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1
graph[0][0] = 2

dir_rotate = [0] * 10001
l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    c = -1 if c == 'D' else 1
    dir_rotate[x] = c

# 북, 서, 남, 동
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
# 'L' 이면 +1, 'D'이면 -1

dir = 3
time = 0
head_y, head_x = 0, 0

snake = deque()
snake.append((head_y, head_x))
while True:    
    time += 1
    ny = head_y + dy[dir]
    nx = head_x + dx[dir]
    snake.append((ny, nx))
    # 뱀의 몸에 닿거나, 공간 밖이면 게임 아웃
    if ny >= n or ny < 0 or nx >= n or nx < 0 or graph[ny][nx] == 2:
        print(time)
        break
    # 사과가 있으면 길이 늘어남
    elif graph[ny][nx] == 1:
        None
    # 사과 없으면 꼬리 줄이기
    elif graph[ny][nx] == 0:
        y, x = snake.popleft()
        graph[y][x] = 0

    graph[ny][nx] = 2
    head_y, head_x = ny, nx

    # 방향 회전 하기
    if dir_rotate[time] != 0:
        dir = (dir + dir_rotate[time]) % 4