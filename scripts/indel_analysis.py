import sys
import pysam

bam = str(sys.argv[1])
bamfile = pysam.AlignmentFile(bam, 'rb')

total=0
rd_indel=0

for read in bamfile:
	if not read.is_unmapped:
		total+=1
		tmp = str(read.cigarstring)
		if 'I' in tmp or 'D' in tmp:
			rd_indel+=1

freq = rd_indel/total
out = open(sys.argv[2],'w')
out.write(str(total) + '\t' + str(freq))
