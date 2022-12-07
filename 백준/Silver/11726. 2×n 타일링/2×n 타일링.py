def get_cnt(n):
    if n == 1:
        print(1)
        return

    if n == 2:
        print(2)
        return

    INF = int(1e9)
    d = [INF] * (n+1)
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = d[i - 2] + d[i - 1]

    print(d[n]%10007)


n = int(input())
get_cnt(n)