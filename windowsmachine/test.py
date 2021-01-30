import sys, csv

infile = "data.txt"
outfile = "output.csv"

with open(outfile) as f:
     for line in f:
        print(line.split(',')[0]+":\t"+str(line.split(',')[1:]))
