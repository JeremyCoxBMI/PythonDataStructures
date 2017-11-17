__author__ = 'COX1KB'

#look up the chromosome, then the SNP

import mytimer as mt
import SNPmaster as sm

def lookups( array ):
    time = 0
    snps = []

    chromo = sm.chromosome()
    for snp in array:
        time += chromo.lookupChromosome(snp[0],"http://ncbi.nih.gov/")
        (t, snpVal) = chromo.getSnp(snp[1])
        time += t
        snps.append( (snp[0],snp[1],snpVal))

    return (time, snps)

# Avery's real-life example
# Why does sorting help?  hint: look at SNPmaster.py

if __name__ == "__main__":

    NumberSteps = 2000

    array = []
    for k in range(0,NumberSteps):
        #random chromosome number, random SNP
        array.append(  (mt.rando(25), mt.rando(100000))  )
    (time, snps) = lookups(array)

    print "Time to look up unsorted snps "+str(time)+" ms"

    array.sort()
    (time, snps) = lookups(array)

    print "Time to look up sorted   snps "+str(time)+" ms"