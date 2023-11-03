Vowel_words = []
Vowels = ['a', 'e', 'i', 'o', 'u']
words = input('Words: ')
for word in words.split():
    if word[0] in Vowels:
        Vowel_words.append(word)
Vowel_words.sort()
print(' '.join(Vowel_words))
