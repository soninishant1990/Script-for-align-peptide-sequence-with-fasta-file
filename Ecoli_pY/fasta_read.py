#!/usr/bin/python
#NKS Program for read csv file peptide sequence and aling with fasta file
#1/1/2019
import csv
import re


#def read_sequencefile(line):
#with open("humanprotein.fasta", 'r') as fh:
with open("EcoliK12_pY_FDR_separate_2018-07-11_16.10.41.csv", 'r', newline='') as seq, open ("ecoli-K12-mg1665.fasta",'r') as fh, open('result.csv','w',newline='') as csvFile:
	csv_reader = csv.reader(seq, delimiter=',')
	d = dict()
	line =fh.readline()
	while line:
		line = line.rstrip('\n')
		if '>' in line:
			#d[key] = key_value
			key = line
			d[key] = ''
			#print(d)
		else:
			key_value = line
			d[key] += key_value
			#print(d)
		line =fh.readline()
	#d[key] = key_value
	print(d)
	#return d