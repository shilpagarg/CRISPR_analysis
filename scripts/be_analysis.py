import sys
import vcf
import pysam
from collections import defaultdict

editor = sys.argv[1]
grna_alns = sys.argv[2]
data = sys.argv[3]
output = sys.argv[4]
outfile = open(output, 'w')


# all are 1-based
for line in open(editor, 'r'):
	tokens= line.rstrip().split(" ")

datax = defaultdict()
with open(data) as fp:
	for line in fp:
		tokens = line.rstrip().split("\t")
		datax[tokens[0]] = line.rstrip()
	
editorx = defaultdict(list)
for line in open(editor):
	tokens = line.rstrip().split("\t")
	editorx[tokens[0]].append(tokens[1])
	editorx[tokens[0]].append(tokens[2])
	editorx[tokens[0]].append(tokens[3])
	editorx[tokens[0]].append(tokens[4])


samfile = pysam.AlignmentFile(grna_alns, "rb")
for read in samfile.fetch():
	be = str(data.split("_")[1])
	pam = len(str(editorx[be][0]))
	pos = read.reference_start + 1 + pam + 1
	if read.is_reverse == False:
		pos = read.reference_start + 1
	be = str(data.split("_")[1])
	if editorx[be][2] =="-":
		ws = int(pos)
		we = int(pos) + 30
		at = str(editorx[be][1])
	else:
		ws = int(pos) + int(editorx[be][2])-1
		we = int(pos) + int(editorx[be][3]) -1 
		at = str(editorx[be][1])
	for i in range(ws,we+1):
		if str(i) in datax:
			outfile.write(datax[str(i)]+ "\n")
