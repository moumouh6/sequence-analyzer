import streamlit as st
from src.dna_analysis import gc_content, reverse_complement, nucleotide_frequency, plot_nucleotide_frequency
from src.protein_analysis import molecular_weight, isoelectric_point, amino_acid_composition, plot_amino_acid_composition
import os
import pandas as pd

st.title("DNA & Protein Sequence Analyzer")
st.write("Enhanced tool with more analysis and downloadable results.")

# --- Sequence input ---
uploaded_file = st.file_uploader("Upload a sequence file (txt/fasta)", type=["txt", "fasta"])
seq_input = st.text_area("Or paste your sequence here:")

seq = None
if uploaded_file:
    seq = uploaded_file.read().decode("utf-8").replace("\n", "").strip().upper()
elif seq_input:
    seq = seq_input.strip().upper()

# --- Sequence type selection ---
choice = st.radio("Select sequence type:", ("DNA", "Protein"))

# --- Analyze button ---
if st.button("Analyze"):
    if not seq:
        st.warning("Please provide a sequence!")
    else:
        os.makedirs("results", exist_ok=True)

        if choice == "DNA":
            gc = gc_content(seq)
            rev_comp = reverse_complement(seq)
            nuc_freq = nucleotide_frequency(seq)
            at_content = round((seq.count('A') + seq.count('T')) / len(seq) * 100, 2)
            gc_skew = round((seq.count('G') - seq.count('C')) / (seq.count('G') + seq.count('C')), 2)

            st.write(f"**GC content:** {gc}%")
            st.write(f"**AT content:** {at_content}%")
            st.write(f"**GC skew:** {gc_skew}")
            st.write(f"**Reverse complement:** {rev_comp}")
            st.write("**Nucleotide counts:**", nuc_freq)

            plot_file = 'results/nucleotide_freq.png'
            plot_nucleotide_frequency(seq, plot_file)
            st.image(plot_file, caption="Nucleotide Frequency")

            # Download CSV
            df = pd.DataFrame(list(nuc_freq.items()), columns=['Nucleotide', 'Count'])
            df['GC%'] = gc
            df['AT%'] = at_content
            st.download_button("Download DNA Results CSV", df.to_csv(index=False), "dna_results.csv")

        else:
            mw = molecular_weight(seq)
            pI = isoelectric_point(seq)
            aa_freq = amino_acid_composition(seq)
            total_aa = sum(aa_freq.values())

            st.write(f"**Molecular weight:** {mw:.2f} Da")
            st.write(f"**Isoelectric point:** {pI:.2f}")
            st.write(f"**Total amino acids:** {total_aa}")
            st.write("**Amino acid counts:**", aa_freq)

            plot_file = 'results/amino_acid_freq.png'
            plot_amino_acid_composition(seq, plot_file)
            st.image(plot_file, caption="Amino Acid Composition")

            # Download CSV
            df = pd.DataFrame(list(aa_freq.items()), columns=['Amino Acid', 'Count'])
            df['Molecular Weight'] = mw
            df['Isoelectric Point'] = pI
            st.download_button("Download Protein Results CSV", df.to_csv(index=False), "protein_results.csv")
