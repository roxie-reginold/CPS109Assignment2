from t4 import createQApairs #import functions return value
import unittest

##def createQApairs():
##    lines = []
##    #unique_dict = {}
##    x = open('unique_QA_Pairs.txt', 'r')
##    with x as f:
##        lines = f.readlines()
##    x.close()
###print(len(lines)) #5830
##    return lines

def createAnswers(Lines = createQApairs()):
    answers = [] #create empty list for answers
    for L in range(0,len(Lines),2):
        A = Lines[L].replace("\n","")
        a = A.replace("answer ","")
        answers.append(a) #append answer to list
    return answers #return asnwers list


answers = createAnswers() #assign answers to function's return value
file2 = open('Answers.txt', 'w') #open answers txt file 
    #unique_dict = {}
for Answer in answers:
    line = "{}\n".format(Answer)
    file2.write(line) #write each answer to txt file
file2.close() #close file
     

##file2 = open('Answers.txt', 'r')
##print(file2.read())
##file2.close()
####
##class myTest(unittest.TestCase):
##    def testUnique(self):
##        self.assertEqual(len(createQApairs()),5830)
##    def testlinesinlist(self):
##        self.assertIsNotNone(createAnswers())
##
##if __name__ == '__main__':
##    unittest.main()
