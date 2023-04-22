res = []

while True:
    values = [v for v in input('').split(' ')]
    values.sort()
    
    if values[0] == '0' and values[1] == '0':
        break
    
    values[0] = values[0].zfill(len(values[1]))
    
    values = [v[::-1] for v in values]
    
    carrys = []
    
    for i in range(len(values[1])):
        int_values = [int(v[i]) for v in values]
        
        carry = 1 if carrys.count(i) != 0 else 0
        
        if sum(int_values) + carry >= 10:
            carrys.append(i + 1)
        
    res.append(len(carrys))

print('')
    
for value in res:
    value_formated = 'No' if value == 0 else value
    plural_formated = 's' if value > 1 else ''
    
    print(f'{value_formated} carry operation{plural_formated}.')