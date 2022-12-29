
import unittest #import unittest 
lines = [] #create empty list to add file contents

x = open('QA_Pairs.txt', 'r') #open QA_Pairs.txt for reading
with x as f:
    lines = f.readlines() #read to list

x.close() #close file

pairs=[] #create empty lists to store QA pairs
for L in range(0,len(lines),2):
    part = "ï»¿" #code part in the begining of the file
    remove = "\n" #remove new line
    if part in lines[L]:#if the part is in the Line
        a = lines[L].replace("ï»¿","") #remove it
        lines[L] = a.replace("\n","") #also remove newlines
    else: 
        a = lines[L].replace("\n","") #remove new line
    #a = lines[L]
    q = lines[L+1].replace("\n","") #remove newline in question
    A = a.lower() #lowercase both question and answer
    Q = q.lower()
    pairs.append((Q,A)) #append QA pair as a tuple to pairs list

def displaynum(x = len(pairs)): #function to display number of pairs
    return x  

print(displaynum(), "number of pairs") #print number of pairs

##class myTest(unittest.TestCase):
##    def testnum(self):
##        self.assertEqual(displaynum(),5725)
##    def testlist(self):
##        self.assertIsNotNone(lines)
##
##if __name__ == '__main__':
##    unittest.main()        
