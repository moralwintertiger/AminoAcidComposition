from Bio import Entrez, SeqIO
import pylab
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt

from AAlibraries import *

class Glycan:

    def __init__(self, name):
        self.name = name
    def positions(self):

        """returns a list of incidences of n-glycan motifs for self"""

        input = self.name
        position_list = []
        for residue in range(len(input)-2):
            if input[residue] == "N" and input[residue+1] != "P" \
                and input[residue+2] in ["S", "T"]:
                position_list.append(residue + 1)
        return position_list

    def num_motifs(self):

        """returns counts of n-glycan motifs for self"""

        input = self.positions()
        return len(input)
        print('changed')

    def hydrophobicity(self):
        """generates hydrophobicity plot using kD library"""
        input = self.name
        output_list = []
        for residue in input:
            output_list.append(kD[residue])
        return output_list

    
