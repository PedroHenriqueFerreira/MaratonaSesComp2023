n = int(input(''))
values = [int(v) for v in input('').split(' ')]

index = 0
atacks = []

while True: 
    current_value = values[index]
    
    if current_value > 0:
        values[index] -= 1
        
        if atacks.count(index) == 0:
            atacks.append(index)
    
    if current_value % 2 == 0:
        index -= 1
    else:
        index += 1
        
    if index < 0 or index + 1 > len(values):
        break

print('')

print(f'{len(atacks)} {sum(values)}')