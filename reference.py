from pipeline import *

if __name__ == '__main__':
    gene = 'reference'
    changeNameSequences()
    alignSequences(gene)
    createBoostrap(gene)
    createDistanceMatrix(gene)
    createUnrootedTree(gene)
    createConsensusTree(gene)