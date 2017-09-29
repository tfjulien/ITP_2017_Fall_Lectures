reference_sequence = 'ATG*A***CC*A*T*C**C*'
sequences = [
    'ATG*A***CC*A*T*C**C*',
    'ATG*T***CC*A*T*C**C*',
    'ATG*A***CC*A*T*C**C*',
    'ATG*A***CC*A*T*C****']

# 1. create function to locate '*' characters in reference

# 2. function to remove characters at indices provided in list

# 3. function to add missing characters


def locate_special_characters(reference_seq):
    list_of_positions = []
    for index, character in enumerate(reference_seq):
        if character == '*':
            list_of_positions.append(index)
    return list_of_positions

position_list = locate_special_characters(reference_sequence)


def remove_characters_at_positions(sequence, pos_list):
    result_sequence = ''
    current_position = 0
    for position in pos_list:
        result_sequence += sequence[current_position:position]
        current_position = position + 1
    return result_sequence


def fill_missing_character(sequence, reference):
    result_string = ''
    for index, character in enumerate(sequence):
        if character == '*':
            result_string += reference[index]
        else:
            result_string += character
    return  result_string

updated_reference_sequence = remove_characters_at_positions(reference_sequence, position_list)

sequences_removed_characters = []
for sequence in sequences:
    sequences_removed_characters.append(
        remove_characters_at_positions(
            sequence,
            position_list
        )
    )

final_sequences = []
for sequence in sequences_removed_characters:
    final_sequences.append(
        fill_missing_character(
            sequence, updated_reference_sequence)
    )

print(final_sequences)
