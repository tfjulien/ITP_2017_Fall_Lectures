
fh = open('data/data.txt', 'r')
counts = {}

for line in fh:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
