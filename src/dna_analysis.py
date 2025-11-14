from Bio.Seq import Seq
import matplotlib.pyplot as plt
import os

def gc_content(seq):
    """Calculate GC content percentage"""
    gc_count = seq.count('G') + seq.count('C')
    return round(gc_count / len(seq) * 100, 2)

def reverse_complement(seq):
    """Return reverse complement of a DNA sequence"""
    return str(Seq(seq).reverse_complement())

def nucleotide_frequency(seq):
    """Return nucleotide counts"""
    return {nuc: seq.count(nuc) for nuc in 'ATGC'}

def plot_nucleotide_frequency(seq, output_file='results/nucleotide_freq.png'):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    freq = nucleotide_frequency(seq)
    plt.bar(freq.keys(), freq.values(), color='skyblue')
    plt.title('Nucleotide Frequency')
    plt.xlabel('Nucleotide')
    plt.ylabel('Count')
    plt.savefig(output_file)
    plt.close()
