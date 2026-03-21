short_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
short_dna1 = short_dna.replace('A','*')
short_dna2 = short_dna1.replace('T','A')
short_dna3 = short_dna2.replace('*','T')
short_dna4 = short_dna3.replace('C','*')
short_dna5 = short_dna4.replace('G','C')
comp_dna = short_dna5.replace('*','G')
print(comp_dna)