import langid
import os

test_path = 'corpus-esaren.train'

langid.load_model(path="corpus-esaren.model/model")

class Accuracy:

    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def update(self, correct=True):
        if correct:
            self.correct += 1
        else:
            self.incorrect += 1
        #print 'updates', self.correct, self.incorrect

    def evaluate(self):
        total_cases = self.correct + self.incorrect
        accuracy = self.correct * 100.0 / total_cases
        print 'Accuracy = %f %% (of %d test cases)' % (accuracy, total_cases)

def visit(arg, dirname, names):
    path = dirname.split('/')

    if len(path) == 1:
        #print names
        for i in range(len(names)-1,0,-1):
            if names[i].startswith('.'):
                del names[i]
        #print names
    else:
        lang = path[1]
        #print arg, dirname, names
        for name in names:
            fd = open(dirname + '/' + name,'r')
            for line in fd.readlines():
                res = langid.classify(line)
                #print lang, ':', res
                if lang == res[0]:
                    a.update(correct=True)
                else:
                    #print 'incorrect:', lang, res
                    a.update(correct=False)
            fd.close()

    
a = Accuracy()
os.path.walk(test_path, visit, '')
a.evaluate()

#res = langid.classify("This is a test")
#print res