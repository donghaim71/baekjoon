'''
연속으로 마시는 경우:
d[i] = d[i-1]의 비연속 + i번째 포도주의 양

비연속으로 마시는 경우:
d[i] = d[i-2]부터 d[0]까지의 최대값 + i번째 포도주의 양
'''

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))


continuous_d = []
discontinuous_d = []

for i in range(n):
    if i == 0:
        continuous_d.append(array[i])
        discontinuous_d.append(array[i])
        continue
    
    if i == 1:   
        ct = discontinuous_d[i - 1] + array[i]
        dct = array[i]
        
        continuous_d.append(ct)
        discontinuous_d.append(dct)
        continue
    
    ct = discontinuous_d[i - 1] + array[i]
    continuous_d.append(ct)
            
    dct = 0
    for j in range(i - 1):
        dct = max(dct, continuous_d[j], discontinuous_d[j])
    discontinuous_d.append(dct + array[i])
    
print(max(continuous_d + discontinuous_d))