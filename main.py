from src.dna_analysis import gc_content, reverse_complement, plot_nucleotide_frequency
from src.protein_analysis import molecular_weight, isoelectric_point, plot_amino_acid_composition

def main():
    print("Welcome to DNA & Protein Sequence Analyzer!\n")
    choice = input("Analyze DNA or Protein? (DNA/Protein): ").strip().upper()
    seq = input("Enter your sequence: ").strip().upper()

    if choice == "DNA":
        print(f"GC content: {gc_content(seq)}%")
        print(f"Reverse complement: {reverse_complement(seq)}")
        plot_nucleotide_frequency(seq)
        print("Nucleotide frequency plot saved in results/")
    elif choice == "PROTEIN":
        print(f"Molecular weight: {molecular_weight(seq):.2f} Da")
        print(f"Isoelectric point: {isoelectric_point(seq):.2f}")
        plot_amino_acid_composition(seq)
        print("Amino acid frequency plot saved in results/")
    else:
        print("Invalid choice! Please select DNA or Protein.")

if __name__ == "__main__":
    main()
