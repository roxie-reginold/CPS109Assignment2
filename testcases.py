#testcases
import unittest
#import all tasks 
from t1 import *
from t2 import *
from t3 import *
from t4 import *
from t5 import *
from t6 import *
from t7 import *



class myTest(unittest.TestCase): #test cases for Tasks
    def testnum(self): #t1
        self.assertEqual(displaynum(),5725)
    def testlist(self):
        self.assertIsNotNone(lines)
    def testOverlap(self): #t2
        self.assertEqual(len(overlapandunique()[0]),2810)
    def testUnique(self):
        self.assertIsNotNone(overlapandunique()[1])
    def testnumberUnique(self): #t3
        self.assertEqual(len(getUniquePairs()[0]),2915)
    def testallUniquePairs(self):
        self.assertIsNotNone(getUniquePairs()[1])
    def testQAUniquePairs(self): #t4
        self.assertEqual(len(createQApairs()),5830)
    def testlengthQuestions(self):
        self.assertEqual(len(create_Questions()),2915)
    def testQApairs(self):#t5
        self.assertIsNotNone(createQApairs())
    def testlengthAnswers(self):
        self.assertEqual(len(createAnswers()),2915)
    def testnumQApairs(self): #t6
        self.assertNotEqual(len(createQApairs()),2915)
    def testlinesinlist(self):
        self.assertIsNotNone(createfrequency()[2])
    def testlistFrequency(self): #t7
        self.assertNotEqual(List_freq,createfrequency_list())
    def testfrequency(self):
        self.assertIsNotNone(createfrequency_list())

if __name__ == '__main__': #run test cases
    unittest.main()
