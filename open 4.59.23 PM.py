filename ='/Users/beverly/Downloads/Boleracea.v1.cds.fasta'
inputfile = open(filename, 'r')
dna_dictionary = dict()

for line in inputfile:
	#print line
	if line.startswith('>'):
		header = line[1:]
		dna_dictionary[header] = ""
	else: 
		dna_dictionary[header] += line 
#print dna_dictionary

new_header = open('seq_header.txt', 'w')

for x,y in dna_dictionary.items():
	new_header.write(x)
	print 


#dna_dictionary = {}
#my_dictionary = {1: 'beverly', 2: 'bev', 3: 'b'}
#for x, y in my_dictionary.items():
	#print x, y
#for x,y in my_dictionary.items():
	#print x
#for x,y in my_dictionary.items():
	#print y
#my_dictionary[4] = 'bam'
#print my_dictionary
#new_dictionary ={'T':'a', 'G': 'c', 'A':'t', 'C':'g'}
#print new_dictionary
#new_string = 'ACGTACAGATACAGATACAGATAGCAGATAGACATAGACATCAGT'
#for x,y in new_dictionary.iteritems():
	#print x, 'corresponds to' , y
	#new_string = new_string.replace(x,y)
	#print new_string


