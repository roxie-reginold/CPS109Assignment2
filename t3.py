import unittest
def getUniquePairs():
    lines = [] #create empty list to store file contents
    unique_dict = {} #create dictionary for unique pairs
    x = open('unique_QA_Pairs.txt', 'r') 
    with x as f:
        lines = f.readlines() #read lines to list
    x.close() #close file

    for L in range(0,len(lines),2): #itterate over lines and add QA pair to dictionary
        unique_dict[lines[L].replace("\n","")] = lines[L+1].replace("\n","")

    return (unique_dict, lines) #return dictionary and lines

file1 = open('QAdictionary.txt', 'w') #create dictionary text file

##    for keys,values in unique_dict.items():
##        line = "{} : {} \n".format(keys, values)
##        file1.write(line)

file1.write(str(getUniquePairs()[0])) #output dictionary results as a string to file

file1.close() #close file
    

##file1 = open('QAdictionary.txt', 'r')
##print(file1.read())
##file1.close()


##class myTest(unittest.TestCase):
##    def testUnique(self):
##        self.assertEqual(len(getUniquePairs()[0]),2915)
##    def testlinesinlist(self):
##        self.assertIsNotNone(getUniquePairs()[1])
##   
##
##if __name__ == '__main__':
##    unittest.main()

