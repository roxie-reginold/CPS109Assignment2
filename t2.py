import unittest

lines = []
x = open('QA_Pairs.txt', 'r')
with x as f:
    lines = f.readlines()
x.close()
pairs=[]
for L in range(0,len(lines),2):
    part = "ï»¿"
    if part in lines[L]:
        a = lines[L].replace("ï»¿","")
        lines[L] = a
    else: 
        a = lines[L]
    #a = lines[L]
    q = lines[L+1]
    A = a.lower()
    Q = q.lower()
    pairs.append((A,Q))

Pairs = pairs[:] #clone pairs 

def overlapandunique(PAIRS = Pairs): #function to find overlapping and unique pairs
    overlapping = [] #create empty overlapping list
    unique = [] #create empty unique list
    seen = [] #create list for seen question and answers
    for P1 in PAIRS: #iterate through pairs 
        if P1[0] in seen or P1[1] in seen: #if question or answer seen previously
            overlapping.append(P1) #append to overlapping list
        if P1[0] not in seen and P1[1] not in seen:
            #if question and answer in pair is not seen before
            #append to unique and seen to ensure the question and answer would not be repeated
            unique.append(P1)
            seen.append(P1[0])
            seen.append(P1[1])
    return (overlapping,unique) #return overlapping and unique pairs    
OVERLAP = overlapandunique()[0] #from return statment overalapping is index 0
UNIQUE = overlapandunique()[1] #unique is index one
print(len(OVERLAP), "overlapping pairs") #number of overlapping pairs
print(len(UNIQUE), "unique pairs") #number of unique pairs
file1 = open('Overlapping.txt', 'w') #create Overlapping.txt to write
file2 = open('unique_QA_Pairs.txt', 'w') #create Unique.txt to write

for o in OVERLAP: #itterate through overlapping pairs
    file1.write(o[0]) #write to file
    file1.write(o[1])

for u in UNIQUE: #iterate through unique pairs
    file2.write(u[0]) #write to file
    file2.write(u[1])

file1.close()
file2.close() #close files

##file1 = open('Overlapping.txt', 'r')
##print(file1.read())
##file1.close()
##
##file2 = open('unique_QA_Pairs.txt', 'r')
##print(file2.read())
##file2.close()

##class myTest(unittest.TestCase):
##    def testOverlap(self):
##        self.assertEqual(len(overlapandunique()[0]),2810)
##    def testUnique(self):
##        self.assertIsNotNone(overlapandunique()[1])
##
##if __name__ == '__main__':
##    unittest.main()  
