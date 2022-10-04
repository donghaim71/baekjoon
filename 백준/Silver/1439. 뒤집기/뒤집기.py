graph = list(input())

zero = 0
one = 0

temp = ''
for i in graph:
    if temp != i:
        temp = i
        if i == '0':
            zero += 1
        elif i == '1':
            one += 1

print(min(zero, one))