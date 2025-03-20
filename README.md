### 1. Objective
The goal of this assignment was to develop a Python script that interleaves two 
paired-end FASTQ files into a single FASTQ file. This process is essential for various 
bioinformatics workflows.

### 2. Tools Used
- **Python 3** (Programming Language)
- **BioPython (SeqIO)** (For reading and writing FASTQ files)
- **BBMap (For validation)
- **Linux Commands (`diff`, `head`)** (For verification)

### 3. Code Explanation
The script `interleave_fastq.py`:
1. **Takes three command-line arguments**:
   - `bacterium_R1.fastq` (Forward reads)
   - `bacterium_R2.fastq` (Reverse reads)
   - `interleaved_output.fastq` (Output file)

2. **Opens the input FASTQ files** and reads them using `SeqIO.parse()`.  
3. **Writes the reads in an interleaved manner**:  
   - First writes a **forward read (R1)**.
   - Then writes the corresponding **reverse read (R2)**.
   - Repeats for all read pairs.

### 4. Testing and Verification
#### **4.1 Running the Script**
Executed the script using:
```bash
python3 interleave_fastq.py \bacterium_R1.fastq \bacterium_R2.fastq \interleaved_output.fastq
