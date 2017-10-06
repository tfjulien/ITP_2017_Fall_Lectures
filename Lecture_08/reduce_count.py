# step 1 - read file
# step 2 - split file into words
# step 3 - reduce list of words into dictionary of counts
# step 4 - use max(key=lambda) to find the largest count
from functools import reduce

fh = open('data/data.txt', 'r')
text = fh.read()
words = text.split()


def reduce_to_counts(dict_of_counts, word):
    dict_of_counts[word] = dict_of_counts.get(word, 0) + 1
    return dict_of_counts

counts_dict = reduce(reduce_to_counts, words, {})


print(max(counts_dict.items(), key=lambda x: x[1]))