import pprint
gen_code = {'uuu': 'Phe', 'uuc': 'Phe', 'uua': 'Leu', 'uug': 'Leu',
          'ucu': 'Ser', 'ucc': 'Ser', 'uca': 'Ser', 'ucg': 'Ser',
          'uau': 'Tyr', 'uac': 'Tyr', 'uaa': 'Stop', 'uag': 'Stop',
          'ugu': 'Cys', 'ugc': 'Cys', 'uga': 'Stop', 'ugg': 'Trp',
          'cuu': 'Leu', 'cuc': 'Leu', 'cua': 'Leu', 'cug': 'Leu',
          'ccu': 'Pro', 'ccc': 'Pro', 'cca': 'Pro', 'ccg': 'Pro',
          'cau': 'His', 'cac': 'His', 'caa': 'Gln', 'cag': 'Gln',
          'cgu': 'Arg', 'cgc': 'Arg', 'cga': 'Arg', 'cgg': 'Arg'}

aa_codon_map = {}
for key, value in gen_code.items():
    aa_codon_map[value] = aa_codon_map.get(value, []) + [key]
    ## alternate solution (google and try to understand what's happening)
    # aa_codon_map.setdefault(value, []).append(key)

pprint.pprint(aa_codon_map)
