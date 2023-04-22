res = []

while True:
    n, m = [int(v) for v in input('').split(' ')]
    
    if n == 0 and m == 0:
        break
    
    matrix = []
    
    for i in range(n):
        line = [bool(int(v)) for v in input('').split(' ')]
        matrix.append(line)
    
    rule_1 = True
    rule_4 = True
    
    for i in range(n):
        if matrix[i].count(True) == m:
            rule_1 = False
            
        if matrix[i].count(True) == 0:
            rule_4 = False
    
    rule_2 = True
    rule_3 = True
    
    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        
        if col.count(True) == 0:
            rule_2 = False
        
        if col.count(True) == n:
            rule_3 = False
            
    res.append([rule_1, rule_2, rule_3, rule_4].count(True))

print('')
    
for value in res:
    print(value)