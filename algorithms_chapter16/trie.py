end = 'end'
def trie(*words):
    root = dict()
    for word in words:
        current = root
        for letter in word:
            current = current.setdefault(letter, {})
        current[end] = end
    return root
ash = trie('pokemon', 'pikachu','dido', 'mew')

def intrie(triee, word):
     current = triee
     for letter in word:
         if letter in current:
             current = current[letter]
         else:
             return False
     else:
         if end in current:
             return True
         else:
             return False

print intrie(ash, 'pokemon')
print intrie(ash, 'pikachu')
