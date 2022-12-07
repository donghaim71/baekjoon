'''
i 계단의 점수 

= [
    i 계단의 점수 + max(i-2 계단의 연속하는 점수, i-2 계단의 연속하지 않는 점수),
    i 계단의 점수 + i-1 계단의 연속하지 않은 점수
    ]

= [
    i 계단의 연속하지 않은 점수,
    i 계단의 연속하는 점수
    ]
'''

t = int(input())

stairs = []
for _ in range(t):
    stairs.append(int(input()))



d = [[0, 0] for _ in range(t)]
d[0][0], d[0][1] = stairs[0], stairs[0]


for i in range(t):
    if i == 1:
        # [연속하지 않는 점수, 연속하는 점수]
        d[i][0] = stairs[i]
        d[i][1] = stairs[i] + stairs[i-1]
    
    elif i > 1:
        # [연속하지 않는 점수, 연속하는 점수]
        d[i][0] = stairs[i] + max(d[i-2][1], d[i-2][0])
        d[i][1] = stairs[i] + d[i-1][0]
    
        
print(max(d[t - 1]))