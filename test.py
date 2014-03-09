import langid
import os

import corpuslib  

test_path = 'corpus-esaren.train'

langid.load_model(path="corpus-esaren.model/model")

    
a = corpuslib.Accuracy()
t = corpuslib.Test(test_path, langid=langid, accuracy=a)
t.start()
a.evaluate()

#res = langid.classify("This is a test")
#print res