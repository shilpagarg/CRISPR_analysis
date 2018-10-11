import sys
import vcf
import pysam
from collections import defaultdict

editor = sys.argv[1]
grna_alns = sys.argv[2]
data = sys.argv[3]
vcff = sys.argv[4]
outfile = open(sys.argv[5], 'w')


# all are 1-based
for line in open(editor, 'r'):
	tokens= line.rstrip().split(" ")

datax = defaultdict(list)
for line in open(data):
	tokens = line.rstrip().split("\t")
	datax[tokens[0]].append(tokens[1])
	datax[tokens[0]].append(tokens[2])
	datax[tokens[0]].append(tokens[3])
	datax[tokens[0]].append(tokens[4])
	
editorx = defaultdict(list)
for line in open(editor):
	tokens = line.rstrip().split("\t")
	editorx[tokens[0]].append(tokens[1])
	editorx[tokens[0]].append(tokens[2])
	editorx[tokens[0]].append(tokens[3])
	editorx[tokens[0]].append(tokens[4])

vcfx = defaultdict(list)
vcf_reader = vcf.Reader(open(vcff, 'r'))
for record in vcf_reader:
	vcfx[str(record.POS)].append(str(record.REF))
	vcfx[str(record.POS)].append(str((record.ALT)[0]))

samfile = pysam.AlignmentFile(grna_alns, "rb")
for read in samfile.fetch():
	pos = read.reference_start + 1
	be = str(read.query_name.split("_")[1])
	ws = int(pos) + int(editorx[be][2])-1
	we = int(pos) + int(editorx[be][3])-1
	at = str(editorx[be][1])
	for i in range(ws,we+1):
		if str(i) in vcfx:
			if vcfx[str(i)][0] == at:
				if len(datax[str(i)])>0:
					outfile.write(str(i) + "\t" + str(datax[str(i)][0]) + "\t" + str(datax[str(i)][1]) + "\t" + str(datax[str(i)][2])  + "\t" + str(datax[str(i)][3]) + "\t" + str(at) + "\n")	

		
	
	
	
