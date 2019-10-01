#motifFinding Program

#Nolaundron 'Ray' Harris

def getDNALists():
    infile=open("motifFinding.txt","r")    
    DNALists=infile.readlines()
    s=(DNALists[0].strip("\n"))
    t=(DNALists[1].strip("\n"))
    return (s,t)
   

def getPositions(s,t):
    Positions=[]
    for i in range(len(s)):
        if s[i:i+len(t)]==t:
            Positions.append(i)
    return (Positions)           
    

def outputResults(Positions):
    posStr = ""
    for i in Positions:
        if (i != 784):
            posStr += str(i) + ", "
        else:
            posStr += str(i) + ". "

    print("The sub-string t occurs within the string s at starting "
          "positions indexed at ",posStr, sep="")

def main():
    s,t=getDNALists()
    findPositions=getPositions(s,t)
    outputResults(findPositions)
    
main()
