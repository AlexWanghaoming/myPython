from Bio import Entrez
import os,sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
import sys, os, argparse, os.path,re,math,time
'''
database:
['pubmed', 'protein', 'nucleotide', 'nuccore', 'nucgss', 'nucest',
'structure', 'genome', 'books', 'cancerchromosomes', 'cdd', 'gap',
'domains', 'gene', 'genomeprj', 'gensat', 'geo', 'gds', 'homologene',
'journals', 'mesh', 'ncbisearch', 'nlmcatalog', 'omia', 'omim', 'pmc',
'popset', 'probe', 'proteinclusters', 'pcassay', 'pccompound',
'pcsubstance', 'snp', 'taxonomy', 'toolkit', 'unigene', 'unists']
'''
parser = argparse.ArgumentParser(description='This script is used to fasta from ncbi ')
parser.add_argument('-t','--term',help='input search  term : https://www.ncbi.nlm.nih.gov/books/NBK3837/#_EntrezHelp_Entrez_Searching_Options_',required=True)
parser.add_argument('-d','--database',help='Please input database to search nucleotide or protein  default nucleotide',default = 'nucleotide',required=False)
parser.add_argument('-r','--rettype',help='return type fasta or gb default gb',default = "gb",required=False)
parser.add_argument('-o','--out_dir',help='Please input  out_put directory path',default = os.getcwd(),required=False)
parser.add_argument('-n','--name',default ='seq',required=False,help='Please specify the output, seq')
args = parser.parse_args()
dout=''

if os.path.exists(args.out_dir):
    dout=os.path.abspath(args.out_dir)
else:
    os.mkdir(args.out_dir)
    dout=os.path.abspath(args.out_dir)
output_handle = open(dout+'/'+args.name+'.%s'%args.rettype, "w")
Entrez.email = "huangls@biomics.com.cn"     # Always tell NCBI who you are
#handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
#print(handle.read())
handle = Entrez.esearch(db=args.database, term=args.term, idtype="acc")
record = Entrez.read(handle)

for i in record['IdList']:
    print i+'\n'
    handle = Entrez.efetch(db=args.database, id=i, rettype=args.rettype, retmode="text")
    #print(handle.read())
    record = SeqIO.read(handle, args.rettype)
    SeqIO.write(record, output_handle, args.rettype)

output_handle.close()
