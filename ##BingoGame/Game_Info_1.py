## Enter tile info here
bList = ['Jason','Hercules','Theseus','Odesseus','e','90','80']
iList = ['753 B.C.','509 B.C.','27 B.C.','476 A.D.','264 B.C.','146 B.C.','60 B.C.','43 B.C.','72 B.C.', '44 B.C.']
nList = ['k','l','m','n','o','90','80']
gList = ['p','q','r','s','t','90','80']
oList = ['u','v','w','x','y','90','80']
mainList = [bList, iList, nList, gList, oList]

def CheckRun():
    listCheck = ListCheck()
    if listCheck == False:
        print ("Lists are not the minimum length, please correct.")
    elif listCheck == True:
        main()

## Resets Checklist to a full list containing all items in mainList
def FillCheckList(checkList):
    length = ( len(bList) + len(iList) + len(nList) + len(gList) + len(oList) )
    b = len(bList)
    i = len(iList)
    n = len(nList)
    g = len(gList)
    o = len(oList)
    count = -1
        
    for x in range (length-1):
        count += 1
        if count <= (b-1):
            checkList.append(bList[x])
        elif count <= ( (b+i) -1):
            checkList.append(iList[x- (b) ])            
        elif count <= ( (b+i+n) -1):
            checkList.append(nList[x- (b+i) ])            
        elif count <= ( (b+i+n+g) -1):
            checkList.append(gList[x- (b+i+n) ])            
        elif count <= ( (b+i+n+g+o) -1):
            checkList.append(oList[x- (b+i+n+g) ])            
    return checkList

## Checks equal length for all the lists
def ListCheck():
    b = len(bList)
    i = len(iList)
    n = len(nList)
    g = len(gList)
    o = len(oList)

    if (b > 5) and (i > 5) and (n > 5) and (g > 5) and (i > 5):
       return True
    else:
        return False

## Returns a random letter from a given list
def GetLetter(mainList,checkList):
    final = []
    for x in range(5):
        randomNum = random.randint(0,4)
        currentList = mainList[x]

        while (currentList[randomNum] in checkList) == False:
            randomNum = random.randint(0,len(currentList)-1)

        final.append(currentList[randomNum])
        checkList.remove(currentList[randomNum])

    return final
