import os

#input file
fin = open("url_images.csv", "rt")
#output file to write the result to
fout = open("out.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('https://drive.google.com/file/d/', 'https://drive.google.com/uc?export=download&id='))
#close input and output files
fin.close()
fout.close()

fin = open("out.txt", "rt")
#output file to write the result to
fout = open("outfinal.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('/view?usp=drivesdk',''))
#close input and output files
fin.close()
fout.close()
