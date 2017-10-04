import masses	# good practice to keep constants in a separate module


list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]

# Iterative Solution
for protein_dict in list_of_protein_dicts:
    valid = True	# assume valid, unless you find evidence when iterating
    running_mass = masses.mass_h2o
    for char in protein_dict['seq'].upper():
        if char in masses.aa_masses:
            running_mass += masses.aa_masses[char]
        else:
            valid = False
            print(protein_dict['seq'], ' is invalid')
            break
    if valid:	# an alternate way would be to use for-else structure (see solution for ques 1)
        mz = running_mass/protein_dict['ch']
        print('m/z of ', protein_dict['seq'], ': ', mz)
