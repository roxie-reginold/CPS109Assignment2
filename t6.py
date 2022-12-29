import unittest
from t4 import createQApairs
##def createQApairs():
##    lines = []
##    unique_dict = {}
##    x = open('unique_QA_Pairs.txt', 'r')
##    with x as f:
##        lines = f.readlines()
##    x.close()
##    #print(lines)
##    return lines

def createfrequency(lines= createQApairs()):
    string = '' #create a empty string
    for L in lines: #itterate through lines
        #remove any punctuation or syntax that may disturb word count
        a = L.replace("'s",'')
        b = a.replace("\n","")
        c = b.replace("?","")
        #d = c.replace("questions", "question")
        d = c.replace(",",'')
        e = d.replace("(", '')
        f = e.replace(")", '')
        g = f.replace("'",'')
        addto = "{} ".format(g)
        string = string + addto.replace("\n","") #add final line to string
    string_words = string #create alliance for string
    List_of_words = string_words.split() #split string into a list of words
    #print(List_of_words)
    words = set(List_of_words) #create a set where repeated words are removed
    #print(words)
    return (words,string,List_of_words)
#reassign function return values
Words = createfrequency()[0] 
list_of_words = createfrequency()[2]
file1 = open('Frequency.txt', 'w') #create new txt called Frequency
for word in Words: #itterate through words set
    n = list_of_words.count(word) #count number of times word appears
    line = "{},{}\n".format(word,n) 
    file1.write(line) #format and write frequency to file
file1.close() #close file
    #return string

#file1 = open('Frequency.txt', 'r')
#print(file1.read())
#file1.close()

##class myTest(unittest.TestCase):
##    def testUnique(self):
##        self.assertEqual(len(createQApairs()),5830)
##    def testlinesinlist(self):
##        self.assertIsNotNone(createfrequency()[2])
##
##if __name__ == '__main__':
##    unittest.main()
