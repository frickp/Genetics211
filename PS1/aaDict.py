#!/bin/bash
from sys import stdin

# In[4]:

d={
    'ATG': 'methionine',
    'AAA': 'lysine',
    'TTA': 'Leucine',
    'TTG': 'Leucine',
    'CTT': 'Leucine',
    'CTC': 'Leucine',
    'CTA': 'Leucine',
    'CTG': 'Leucine',
    'CCT': 'Proline',
    'CCC': 'Proline',
    'CCA': 'Proline',
    'CCG': 'Proline',
}

usrIn=stdin.readline()
usrIn=usrIn.rstrip("\r\n")

if usrIn in list(d.keys()):
	print d[usrIn]
else:
	print "Nucleotide key not found, try another."
	print "The keys are:"
	print d.keys()
#print d['ATG']




