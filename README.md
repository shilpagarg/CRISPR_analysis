This tool is designed for the analysis of multiplex base editing in repetitive and non-repetitive regions. In the Church lab, recent efforts are ongoing for the development of safe DNA editors capable of multiplex engineering. This tool can help answer questions like which bases have been edited in the window specific to gRNA, finding percent of reads with indels after editing and so on.

Dependencies: samtools, picard, bwa, snakemake <br/>
These dependencies can be easily installed using Anaconda.

Directory structure: <br/>
1. Download Snakefile and other scripts in the current working directory <br/>
2. Make input directory. <br/>
3. The input folder contains reference genomes and their indexes, gRNA and other samples. The names of each file follows standard format as explained in test data.

You are good to go now using: <br/>
snakemake -j 40

Output: This will generate summary files for SNVs and indels in current folder.
