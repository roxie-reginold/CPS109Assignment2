import unittest

def createQApairs():
    lines = []
    
    x = open('unique_QA_Pairs.txt', 'r')
    with x as f:
        lines = f.readlines()
    x.close()

    return lines

def create_Questions(Lines = createQApairs()):
    questions = [] #create empty list for only questions
    for L in range(0,len(Lines),2):
        Q = Lines[L+1].replace("\n","") #replace new line syntax
        q = Q.replace("question ","") #remove word question
        questions.append(q) #append question to list
    return questions



questions = create_Questions() #assignment questions to return value of function

file1 = open('Questions.txt', 'w') #open a file to write all questions

for Question in questions:
    line = "{}\n".format(Question) #add question line by line to txt file
    file1.write(line)
file1.close() #close file
     

#file1 = open('Questions.txt', 'r')
#print(file1.read())
#file1.close()

##class myTest(unittest.TestCase):
##    def testUnique(self):
##        self.assertEqual(len(createQApairs()),5830)
##    def testlinesinlist(self):
##        self.assertIsNotNone(createQuestions())
##
##if __name__ == '__main__':
##    unittest.main()
