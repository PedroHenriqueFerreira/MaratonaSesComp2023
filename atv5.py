n = int(input(''))

phrases = []
phrases_size = []

for i in range(n):
    words = input('').split(' ')
    words.sort(key=lambda word: len(word), reverse=True)
    
    size = len(words)
    
    phrases.append(' '.join(words))
    phrases_size.append(size)
        
repeated_indexes = []
res = []

for i, phrase_size in enumerate(phrases_size):
    if phrases_size.count(phrase_size) > 1:
        repeated_indexes.append(i)
    else:
        res.append(phrases[i])
        
res.sort(key=lambda phrase: len(phrase))

for repeated_index in repeated_indexes:
    res.insert(repeated_index, phrases[repeated_index])

print('')

for phrase in res:
    print(phrase)