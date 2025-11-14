from Bio.SeqUtils import ProtParam
import matplotlib.pyplot as plt
import os

def amino_acid_composition(seq):
    """Return amino acid counts"""
    analysis = ProtParam.ProteinAnalysis(seq)
    return analysis.count_amino_acids()

def molecular_weight(seq):
    """Return protein molecular weight"""
    analysis = ProtParam.ProteinAnalysis(seq)
    return analysis.molecular_weight()

def isoelectric_point(seq):
    """Return protein isoelectric point"""
    analysis = ProtParam.ProteinAnalysis(seq)
    return analysis.isoelectric_point()

def plot_amino_acid_composition(seq, output_file='results/amino_acid_freq.png'):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    freq = amino_acid_composition(seq)
    plt.bar(freq.keys(), freq.values(), color='lightgreen')
    plt.title('Amino Acid Frequency')
    plt.xlabel('Amino Acid')
    plt.ylabel('Count')
    plt.savefig(output_file)
    plt.close()
