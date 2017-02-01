import DivisibleBy

def GetNumbers():
    numbers = [input('Enter a number: ') for i in range(3)]
    return numbers

def GetSimplified(a,b,c,numbers):
    testNums = []
    refinedFactors = []
    shouldTest = False
    for x in range (int(max(numbers))):
        if x > 1:
            if a % x == 0:
                if b % x == 0:
                    if c % x == 0:
                        testNums.append(x)
                        shouldTest = True
    if shouldTest == True:
        trueTest = max(testNums)
        refinedFactors.append(a/trueTest)
        refinedFactors.append(b/trueTest)
        refinedFactors.append(c/trueTest)
        refinedFactors.append(max(testNums))
    return refinedFactors

def GetFactors(numbers, givenNumber):
    factors = list( DivisibleBy.Main(givenNumber) )

    return factors

def GetFirstSet(factors, half):
    firstSet = factors[:half]

    return firstSet

def GetSecondSet(factors,firstSet, half):
    secondSet = []
    for i in factors:
        if i not in firstSet:
            secondSet.append(i)        

    secondSet.reverse()
    return secondSet
