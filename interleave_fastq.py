#!/usr/bin/env python3

import argparse
from Bio import SeqIO

def interleave_fastq(forward_file, reverse_file, output_file):
    """Interleave two paired-end FASTQ files into one output FASTQ file."""
    with open(forward_file, "r") as fwd, open(reverse_file, "r") as rev, open(output_file, "w") as out:
        # Write interleaved output
        for fwd_read, rev_read in zip(SeqIO.parse(fwd, "fastq"), SeqIO.parse(rev, "fastq")):
            SeqIO.write(fwd_read, out, "fastq") # Write forward read
            SeqIO.write(rev_read, out, "fastq") # Write reverse read

    print(f"Interleaved FASTQ file saved as: {output_file}")

if __name__ == '__main__':
    # Set up command-line argument
    parser = argparse.ArgumentParser(description='Interleave Paired-End FASTQ Files')
    parser.add_argument('forward_file', help='Forward reads FASTQ file (R1)')
    parser.add_argument('reverse_file', help='Reverse reads FASTQ file (R2)')
    parser.add_argument('output_file', help='Output interleaved FASTQ file')
    
    # Parse arguments and call function
    args = parser.parse_args()
    interleave_fastq(args.forward_file, args.reverse_file, args.output_file)

