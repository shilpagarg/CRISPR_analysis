import sys
import pysam
import re

bam = str(sys.argv[1])
startpos = sys.argv[2]
endpos = sys.argv[3]
bamfile = pysam.AlignmentFile(bam, 'rb')

total=0
rd_indel=0


for read in bamfile:
        if not read.is_unmapped:
                total+=1
                ref_pos = read.pos
                query_pos = 0
                # MIDNSHPX= => 012345678
                for cigar_op, length in read.cigartuples:
                        if cigar_op in (0, 7, 8):
                                query_pos += length
                                ref_pos += length
                        elif cigar_op == 1:
                                query_pos += length
                                if ref_pos >= int(startpos) and ref_pos <= int(endpos):
                                        rd_indel+=1
                                        break
                        elif cigar_op == 2:
                                if ref_pos >= int(startpos) and ref_pos <= int(endpos):
                                        rd_indel+=1
                                        break
                                ref_pos += length
                        elif cigar_op == 3:
                                ref_pos += length
                        elif cigar_op == 4:
                                query_pos += length
                        elif cigar_op == 5 or cigar_op == 6:
                                pass

freq = (rd_indel/total)*100
out = open(sys.argv[4],'w')
s = bam.split('/')[-1].split('.')[0]
print(s)
out.write('sample \t total_reads \t indel_reads \t %indel_reads \n ')
out.write(s + '\t' + str(total) + '\t' + str(rd_indel) + '\t' + str(freq) + '\n')
