t = int(input())

array = []
for i in range(t):
    k = int(input())
    n = int(input())
    array.append([k, n])


d = [[] for _ in range(15)]


for i in range(14):
    d[0].append(i + 1)

def get_tenants(d, i, j):
    stair = d[i - 1]
    
    tenants = 0
    for k in range(j + 1):
        tenants = tenants + stair[k]
    
    return tenants
    
    
    
for i in range(1, 15):
    for j in range(14):
        tenants = get_tenants(d, i, j)
        d[i].append(tenants)


for k, n in array:
    print(d[k][n-1])