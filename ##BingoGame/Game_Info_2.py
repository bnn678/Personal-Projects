## Enter tile info here
mainList = ['I','V','M','C','II','IV','VIII',
            'XII','g','h','i','j','90','80',
            'k','l','m','n','o','90','80',
            'p','q','r','s','t','90','80',
            'u','v','w','x','y','90','80', '70', '60']

## Resets Checklist to a full list containing all items in mainList
def FillCheckList(checkList):
    for x in range( len(mainList)-1 ):
        checkList.append(mainList[x])
    return checkList

## Returns a random letter from a given list
def GetLetter(mainList, checkList):
    final = []
    for x in range(5):
        randomNum = random.randint(0,len(mainList)-1)
        
        while (mainList[randomNum] in checkList) == False:
            randomNum = random.randint(0,len(mainList)-1)
            
        final.append(mainList[randomNum])
        checkList.remove(mainList[randomNum])
    return final
