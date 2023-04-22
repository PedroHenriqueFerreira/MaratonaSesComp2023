n, m = [int(v) for v in input('').split(' ')]

matrix = []

for i in range(n):
    line = [int(v) for v in input('').split(' ')]
    
    matrix.append(line)

res = []

for i in range(n):
    if i == 0 or i == n - 1:
        continue
    
    for j in range(m):
        if j == 0 or j == m - 1:
            continue
        
        if matrix[i][j] != 42:
            continue
        
        prev_line = matrix[i - 1]
        
        if prev_line[j - 1] != 7 or prev_line[j] != 7 or prev_line[j + 1] != 7:
            continue
        
        next_line = matrix[i + 1]
        
        if next_line[j - 1] != 7 or next_line[j] != 7 or next_line[j + 1] != 7:
            continue
        
        if matrix[i][j - 1] != 7 or matrix[i][j + 1] != 7:
            continue
        
        res.append(i + 1)
        res.append(j + 1)

if len(res) == 0:
    res.append(0)
    res.append(0)

print('')    

print(' '.join([str(v) for v in res]))