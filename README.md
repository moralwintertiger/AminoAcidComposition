# AminoAcidComposition
scripts to analyze amino acid composition, features by position, regions of interest.

GlycosylationSites.py pulls amino acid records from Entrez using biopython and a keyword (in this case, "Tas2", which will pull all amino acid records with gene names beginning with Tas2, ie all type 2 taste receptors). These records are then search for N-glycosylation motifs, which are used to build a list of positions. The list of positions is then plotted. 

GlycanClasses.py holds functionality of Glycosylationnumber.py, as a Glycan class. 
