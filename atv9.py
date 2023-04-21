res = 0

while True:
    n, m = [int(v) for v in input('').splt(' ')]
    
    if n == 0 and m == 0:
        break
    
    matriz = []
    
    for i in range(n):
        line = [int(v) for v in input('').split(' ')]
        matriz.append(line)
    
    rule_1 = rule_2 = rule_3 = rule_4 = 0
    
    for i in n:
        for j in m:
            if 