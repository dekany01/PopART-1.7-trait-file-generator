# PopART-1.7-trait-file-generator
The python script generates a PopART 1.7 trait file. It needs 2 input files: one is a haplotype file generated in DNASP v6, the other is a txt file containing the accession numbers of the sequences and the corresponding metadata (such as geographic locations, populations etc.).

The required format of the input files:
--
"Hap" file:
-- 
From DNASP v6, you first need to export the .nex file. From the .nex file you need to extract the part from the second "[Hap# Freq. Sequences]" line (the mentioned line included) with the accession numbers listed into a .txt file by simply copy-paste.\
for example:\
[Hap#  Freq. Sequences]\
[Hap_7:  1    AF132823.1]


"ID" file:
--
ID file is a .txt file which contains the accession number in one column and the chosen metada in the second column.\
for example:\
Accession[space]number[tab]Country\
AF132823[tab]Zimbabwe
