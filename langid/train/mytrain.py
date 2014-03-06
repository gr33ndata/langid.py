import os
import subprocess 

CWD = os.getcwd()

def main():

    # Indexing
    cmd = "python %s/langid/train/index.py -l en -l es -l ar -d gvo -d internet -d egypt %s/corpus-esaren" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)
    
    # Tokenization
    cmd = "python %s/langid/train/tokenize.py %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

    cmd = "python %s/langid/train/DFfeatureselect.py %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

    # Information Gain
    cmd = "python %s/langid/train/IGweight.py -d %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

    cmd = "python %s/langid/train/IGweight.py -lb %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)
    
    # LD Featureselect
    cmd = "python %s/langid/train/LDfeatureselect.py %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

    # Scanner
    cmd = "python %s/langid/train/scanner.py %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

    
    # NB Train
    cmd = "python %s/langid/train/NBtrain.py %s/corpus-esaren.model" % (CWD, CWD)
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)

       

import cProfile
import pstats
cProfile.run('main()','train_prof')
p_stats = pstats.Stats('train_prof')
p_stats.sort_stats('time').print_stats(10)

print 'Done'