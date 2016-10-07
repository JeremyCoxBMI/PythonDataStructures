__author__ = 'COX1KB'

from suffix_tree import SuffixTree
import mytimer as mt

# This is supposed to build a suffix tree in O(n) time.  Do you believe it?
# Why is the build time different with the two different strings length 300?
# Can you make one that takes more time and uses more memory?

if __name__ == "__main__":

    timer = mt.mytimer()
    timer.start()
    st = SuffixTree('abc')
    print "building length 3 took "+timer.elapsed()
    print "memory complexity length 3 took "+str(st.sizeEdges())+" edges "+" and "+str(st.sizeNodes())+ " nodes"
    print ""

    timer.start()
    st = SuffixTree('TTAAAAAATATTTATTCTGGTTCATTGACC')
    print "building length 30 took "+timer.elapsed()
    print "memory complexity length 30 took "+str(st.sizeEdges())+" edges "+" and "+str(st.sizeNodes())+ " nodes"
    print ""

    seed = 'TTAAAAAATATTTATTCTGGTTCATTGACC'
    seed += seed + seed + seed + seed
    seed += seed

    timer.start()
    st = SuffixTree(seed)
    print "building length 300 took "+timer.elapsed()
    print "memory complexity length 300 took "+str(st.sizeEdges())+" edges "+" and "+str(st.sizeNodes())+ " nodes"
    print ""

    seed = "ATCCTCAATAAAATATGCACAATAGATCTCTACTGAGAAAACTTTATATTTTAGAAGCAATTCATCTCCC"+ \
            "TTTTAAAATACAAACTTGCATAGGATTGCCATAAATTAATGCACCTAAAATTAAGTCGTTTCTATGAAAT"+ \
            "TTATTTTAGGTGTGAAATTATATATTAGGTGTACAATTAGCCATACCATTCCGACAATATCGACATAGGA"+ \
            "ATATTGAGTAGAACAAGATGTACCATTATTAGCTTCTGGGTTGGCATAAGGGAATACAGGCAAAGACTTA"+ \
            "AACCTATTCGGACTCTGTAG"

    timer.start()
    st = SuffixTree(seed)
    print "building length 300 took "+timer.elapsed()
    print "memory complexity length 300 took "+str(st.sizeEdges())+" edges "+" and "+str(st.sizeNodes())+ " nodes"
    print ""



    timer.start()
    print "Has substring (expect true) = "+str(st.has_substring("ACTCTGTAG"))
    print "substring suffix of length 9 took "+timer.elapsed()

    timer.start()
    print "Has substring (expect false) = "+str(st.has_substring("TCTCTGTAG"))
    print "substring suffix of length 9 took "+timer.elapsed()

    timer.start()
    print "Has substring (expect true) = "+str(st.has_substring("ATATTGAGTAGAACAAGATGTACCATTATTAGCTTCTGGGTTGGCATAAGGGAATACAGGCAAAGACTTAAACCTATTCGGACTCTGTAG"))
    print "substring suffix of length 90 took "+timer.elapsed()


    string180 = "TTAAGTCGTTTCTATGAAAT"+ \
            "TTATTTTAGGTGTGAAATTATATATTAGGTGTACAATTAGCCATACCATTCCGACAATATCGACATAGGA"+ \
            "ATATTGAGTAGAACAAGATGTACCATTATTAGCTTCTGGGTTGGCATAAGGGAATACAGGCAAAGACTTA"+ \
            "AACCTATTCGGACTCTGTAG"

    timer.start()
    print "Has substring (expect true) = "+str(st.has_substring(string180))
    print "substring suffix of length 180 took "+timer.elapsed()

    timer.start()
    print "Has substring (expect true) = "+str(st.has_substring(seed))
    print "substring suffix of length 300 took "+timer.elapsed()