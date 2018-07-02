from Bio import Entrez, SeqIO
import pylab
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt

Entrez.email="moralwintertiger@gmail.com"
#attach an IdList to handle:
handle = Entrez.esearch(db="protein", term="Tas2*[gene] NOT partial AND mus[ORGN]", retmax='500')
record = Entrez.read(handle)
#handle.close()
id_list =record['IdList']

handle2 = Entrez.efetch(db="protein", id=id_list,rettype="gb", retmode="text")

#make a list of the sequences in the handle2:
input_sequence_list = []
for seq_record in SeqIO.parse(handle2,"gb"):
    input_sequence_list.append(str(seq_record.seq))

def motif_finder_set(input_sequences):
    position_list = []
    for seq in input_sequences:
        for residue in range(len(seq)-2):
            if seq[residue] == "N" and seq[residue+1] != "P" and seq[residue+2] in ["S", "T"]:
                position_list.append(residue + 1)
    return position_list

output_vals = motif_finder_set(input_sequence_list)

yvals = [output_vals.count(i) for i in range(max(output_vals)+1)]

plt.plot(yvals, 'r', linewidth=2)

plt.xlabel("amino acid position")
plt.ylabel("N-glycosylation motifs")
plt.title("N-glycosylation of Type 2 Taste Receptors")
plt.show()
plt.savefig("Tas2RGlycans.png")
