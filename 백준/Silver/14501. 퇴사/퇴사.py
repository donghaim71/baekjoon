n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


d = [0 for _ in range(n)]

for i in range(n):
    t, p = array[i][0], array[i][1]

    # 이전 상담일 중에서 해당일과 상담 소요일이 현재 상담일을 넘지 않아야 함
    ex = [0]
    for j in range(i):
        if j + array[j][0] > i:
            continue
        ex.append(d[j])
    max_ = max(ex)
    
    # 만약 상담일과 상담 소요일의 합이 퇴사 당일 포함 이후라면 해당 일의 상담은 못함, 이전 상담일의 수익을 저장
    if i + t > n:
        d[i] = max_
    else:
        d[i] = max_ + p

print(max(d))