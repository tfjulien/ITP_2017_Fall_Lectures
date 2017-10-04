# dictionary used for reverse complementing
reverse_comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

# Prompt user for the number of sequences to be processed
n_seqs = int(input('Enter the number of sequences: '))

# list to hold unique sequences
list_of_sequences = []
for input_number in range(n_seqs):
    # get input from the user
    input_sequence = input('Enter DNA sequence: ')

    # check that all the characters are valid
    reversed_seq = ''
    for char in input_sequence[::-1]:
        # I create a variable for the upper case character as I use the upper case multiple times
        upper_char = char.upper()
        # if a character is invalid then break
        if upper_char not in ['A', 'C', 'G', 'T']:
            print('{} is an invalid character'.format(char))
            break
        comp_upper_char = reverse_comp[upper_char]
        # an 'inline if' - these are if statements for assigning variables
        # it will use the uppercase char if the original is uppercase otherwise it will use lowercase
        reversed_seq += comp_upper_char if char.isupper() else comp_upper_char.lower()
    # this will only execute if the the break was not called, which means the sequence was valid
    else:
        if reversed_seq not in list_of_sequences:
            print('{} has been added to the list'.format(reversed_seq))
            list_of_sequences.append(reversed_seq)
        else:
            print('{} is already in list'.format(reversed_seq))

# --PRE COMPUTE VALUES NEEDED FOR OUTPUT--
# Dictionary which keeps count of each nucleotide
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
number_of_sequences = len(list_of_sequences)
# variable to count the total number of nucleotides
length_of_all_sequences = 0
# iterate over each sequence and add its length to length_of_all_sequences
for sequence in list_of_sequences:
    length_of_all_sequences += len(sequence)
    # Update the counts for each nucleotide for each sequence
    for key in counts:
        counts[key] += sequence.upper().count(key)

# --OUTPUT CALCULATED VALUES--
print('Sequences')
print('\t' + ', '.join(list_of_sequences))
print('--* Statistics *--')
print('\tfrequencies:')
for key, value in counts.items():
    print('\t\t {}/{}\t: {}/{}'.format(key, key.lower(), value, length_of_all_sequences))
print('\tnumber of sequences:')
print('\t\t', number_of_sequences)
print('\taverage number of characters per sequence:')
print('\t\t{:.3f}'.format(length_of_all_sequences / number_of_sequences))
