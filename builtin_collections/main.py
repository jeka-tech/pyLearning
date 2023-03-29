from collections import Counter

text = ['new', 'text', 'with', 'any', 'symbols', 'and', 'words']
with open('gogol.txt', encoding='utf-8') as book:
    words = book.read().split(' ')

top_five = Counter(words).most_common(5)
print(top_five)
