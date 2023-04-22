n = int(input(''))

even = []
odd = []

for i in range(n):
    v = int(input(''))
    
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
        
even.sort()
odd.sort(reverse=True)

print('')

for v in [*even, *odd]:
    print(v)