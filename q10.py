res = []

while True:
    try:
        w, h, n = [int(v) for v in input('').split(' ')]

        for i in range(n):
            dimentions = [int(v) for v in input('').split(' ')]

            dimentions.sort()

            wi, hi = dimentions

            if wi > w or hi > h:
                res.append('Nao')
            else:
                res.append('Sim')
    except EOFError:
        break

print('')

for value in res:
    print(value)
