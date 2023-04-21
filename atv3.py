intervals = []

while True:
    values = [int(n) for n in input('').split(' ')]
    values.sort()
    
    if values[0] == 0:
        break

    intervals.append(values)

print('')    

for interval in intervals:
    int_range = list(range(interval[0], interval[1] + 1))
    string_range = [str(v) for v in int_range]
    
    print(f'{" ".join(string_range)} Sum={sum(int_range)}')