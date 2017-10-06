import os
from pprint import pprint

pardir = 'data'

files = []
for fname in os.listdir(pardir):
    if os.path.splitext(fname)[1] == '.txt':
        files.append(os.path.join(pardir, fname))
# files = [os.path.join(pardir, fname)
#          for fname in os.listdir(pardir)
#          if os.path.splitext(fname)[1] == '.txt']

counts = {}
for file_ in files:

    with open(file_, 'r') as fh:
        for line in fh:

            for word in line.split():

                counts[word] = counts.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        print('old' ,big_word, big_count)
        print('new', word, count)
        big_word = word
        big_count = count
#
# print(big_word, big_count)


# files = []
# for fname in os.listdir(pardir):
#     if os.path.splitext(fname)[1] == '.txt':
#         files.append(os.path.join(pardir, fname))