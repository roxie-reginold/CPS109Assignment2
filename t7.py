import unittest
from t6 import createfrequency #import function from t6

def createfrequency_list(words = createfrequency()[0],Words_list = createfrequency()[2]):
    listfrequency = [] #create list for frequency
    #words = createfrequency()[0]
    #Words_list = createfrequency()[2]
    for word in words:
        n = Words_list.count(word)
        listfrequency.append((word,n)) #store word,n tuple to list
    return listfrequency

#print(listfrequency)
List_freq = createfrequency_list()[:] #clone list from function's return value

def Secondindex(num): #sort frequency values
    return num[1]

List_freq.sort(key=Secondindex,reverse=True) #sort list by 2nd intex value of tuple
#sort in desending order
#print(List_freq)
file1 = open('Decreasing_Frequency.txt', 'w') #open file to store frequencies in descending order
for t in List_freq: #itterate through list of tuples
    line = "{},{}\n".format(t[0],t[1])
    file1.write(line) #append word with value
file1.close() #close file

##file1 = open('Decreasing_Frequency.txt', 'r')
##print(file1.read())
##file1.close()

##class myTest(unittest.TestCase):
##    def testUnique(self):
##        self.assertNotEqual(List_freq,createfrequency_list())
##    def testlinesinlist(self):
##        self.assertIsNotNone(createfrequency_list())
##
##if __name__ == '__main__':
##    unittest.main()
