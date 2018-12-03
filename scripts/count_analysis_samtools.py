import sys
import vcf
import pysam
from collections import defaultdict

vcff = sys.argv[1]
out = sys.argv[2]

outfile = open(out, 'w')
# all are 1-based
vcf_reader = vcf.Reader(open(vcff, 'r'))
for record in vcf_reader:
	str1 = '\t'.join(str(i) for i in record.ALT)
	if type(record.samples[0]['AD']) == list:
		str2 = '\t'.join(str(i) for i in record.samples[0]['AD'])
	else:
		str2 = str(record.samples[0]['AD'])

	outfile.write(str(record.POS) + "\t" + str(record.REF) + "\t" + str1 + "\t" + str(record.INFO['DP'])  + "\t" + str2 + "\n")	
