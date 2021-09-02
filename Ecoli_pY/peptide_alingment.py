#!/usr/bin/python
#NKS Program for read csv file peptide sequence and aling with fasta file
#1/1/2019
import csv
import re


#def read_sequencefile(line):
#with open("humanprotein.fasta", 'r') as fh:
with open("EcoliK12_pY_FDR_separate_2018-07-11_16.10.41.csv", 'r', newline='') as seq, open ("ecoli-K12-mg1665.fasta",'r') as fh, open('result.csv','w',newline='') as csvFile:
	csv_reader = csv.reader(seq, delimiter=',')
	#for firstline in csv_reader:
		#print(firstline)
		#break
	#without_header = next(csv_reader)
	#print(without_header)
	#print(csv_reader)
	#print("hello")
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
	#print(d)
	#return d
	seq_key = d.keys()
	seq_value = d.values()
	#writ = csv.writer(csvFile, dialect=',')
	#for row in d:
		#writ.writerow(row)
	#csvfile.close()
	#print(d.values(0))
	#c = "AVTLYLGAVAATVR"
	#for  key,val in d.items():
		#if c in val:
			#print(key)



	store_values = csv.writer(csvFile, delimiter=',')
	store_values.writerow(["Peptide","Peptide Mass","Protein Id","Protein Description","Protein length","Start pos","end pos","peptide size"])
	total_mass = ''
	#for i, m in enumerate(csv_reader):
	for m in csv_reader:
		#m = m.rstrip(',')
		#print(seq_value)
		#break
		b = m[5]
		#store_values = csv.writer(csvFile, dialect='excel-tab')
		#store_values.writerow(b)
		mass = m[4]
		charge = m[2]
		#store_values = csv.writer(csvFile, delimiter=',')
		#store_values.writerow([b])
		#cal = mass * charge
		#total_mass = cal - charge
		#print(b)
		#for seq_values
		for  key,val in d.items():
			if b in val:
				match_result = key
				#print(match_result)
				m = re.search(b, val)
				start_point = m.start()
				end_point = m.end()
				span_point = m.span()
				#span_point = span_point.strip('\s')
				part = match_result.split('|')
				id  = part[0] + '|' + part[1] + '|' + part[2]
				protein_length = len(val)
				protein_des = part[4]
				peptide_size = span_point[1] - span_point[0]
				#start_end = b.start()
				#combine_data = b + ',' mass + ',' id + ',' protein_des + ',' protein_length + ',' end_point + ',' end_point + ',' span_point
				#csvFile.write(combine_data)
				#print(b, total_mass, id, protein_des, protein_length, end_point, end_point, span_point[0], span_point[1])
				#store_values = csv.writer(csvFile, dialect='excel-tab')
				store_values = csv.writer(csvFile, delimiter=',')
				#store_values.writerow([b,',', total_mass, ',', id, ',', protein_des,',', protein_length,',', end_point,',', end_point,',', span_point[0], ',',span_point[1]])
				store_values.writerow([b,mass,id,protein_des,protein_length,span_point[0]+1,span_point[1],peptide_size])
				#store_values.writerow([b.strip('\n')])
				break