
# The 20 valid AA characters and their masses are as follows:

# mass(A) = 71.03711360
# mass(C) = 103.0091854
# mass(D) = 115.0269428
# mass(E) = 129.0425928
# mass(F) = 147.0684136
# mass(G) = 57.02146360
# mass(H) = 137.0589116
# mass(I) = 113.0840636
# mass(K) = 128.0949626
# mass(L) = 113.0840636
# mass(M) = 131.0404854
# mass(N) = 114.0429272
# mass(P) = 97.05276360
# mass(Q) = 128.0585772
# mass(R) = 156.1011106
# mass(S) = 87.03202820
# mass(T) = 101.0476782
# mass(V) = 99.06841360
# mass(W) = 186.0793126
# mass(Y) = 163.0633282

# mass(h2o) = 18.010564684  --> mass of water

# Examples of valid protein sequences: ACDEFPMNQR, acdefpmnqr
# Example of invalid protein sequence: ACZEFP ('Z' is not a valid AA)
# mass(ACDEFPMNQR) = mass(h2o) + (sum of masses of all AA characters in ACDEFPMNQR)
# m/z of ACDEFPMNQR can be calculated as: mass(ACDEFPMNQR)/ch(ACDEFPMNQR); ch is provided for each sequence


list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2}, 
                         {'seq': 'ELEMYRATNE', 'ch': 1}, 
                         {'seq': 'wapwop', 'ch': 3}, 
                         {'seq': 'zeittsieg', 'ch': 2}, 
                         {'seq': 'DESFBIRC', 'ch': 1}, 
                         {'seq': 'altaatsiv', 'ch': 3}, 
                         {'seq': 'MEINWOHC', 'ch': 2}]