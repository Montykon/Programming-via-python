#3_1
gen_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = gen_dna[0:63:1]
exon2 = gen_dna[91::1]
intron = gen_dna[63:91:1]

print("Coding part: ", exon1 + exon2)
print("Intron is: ", intron) 
#3_2
countintron = len(intron)
codingcoun = len(exon1 + exon2)
unserresult = (countintron / codingcoun)*100


print(unserresult, '%')
#3_3
exon12 = exon1.lower()
exon22 = exon2.lower()
print(exon12 + intron + exon22)