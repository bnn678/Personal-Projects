import DivisibleBy

## This is the universal code used by both addition and subtraction
## It gets all necessary info to solve either problem

## NOTE: This is not a standalone program, just contains info to be called elsewhere

## Gets the coeffecients of the quadratic in the order of ax^2, bx, c 
def GetNumbers():
    numbers = [input('Enter a number: ') for i in range(3)]
    return numbers

## Take out a common factor if possible
def GetSimplified(a,b,c):
    testNums = []
    refinedFactors = []
    numbers = [a,b,c]
    shouldTest = False

    ## Only use for 'numbers' is to find greatest test number
    for x in range (int(max(numbers))):
        if x > 1:
            if a % x == 0:
                if b % x == 0:
                    if c % x == 0:
                        ## Eliminates the common factor if there is one
                        testNums.append(x)
                        shouldTest = True
                        
    ## Factors out the GREATEST common coeffecient then return the factors and the coeffeicent
    if shouldTest == True:
        trueTest = max(testNums)
        refinedFactors.append(a/trueTest)
        refinedFactors.append(b/trueTest)
        refinedFactors.append(c/trueTest)
        refinedFactors.append(max(testNums))
    return refinedFactors

## Returns the factors of any given number
## This would be redundant if I imported DivisibleBy into FactorQuadraticsAddition
    ## This is to keep from having to import DivisibleBy into FactorQuadraticsAddition
def GetFactors(givenNumber):
    factors = list( DivisibleBy.Main(givenNumber) )

    return factors

## Returns the 'front factors' or the lesser of two numbers in a multiplication equation
## Ex. 3*8=24:  'front factor' = 3
def GetFirstSet(factors, half):
    firstSet = factors[:half]

    return firstSet

## Returns the 'latter factors' or the greater of two numbers in a multiplication equation
## Ex. 8*3=24: 'latter factor' = 8
def GetSecondSet(factors,firstSet, half):
    secondSet = []
    for i in factors:
        if i not in firstSet:
            secondSet.append(i)        

    ## the list is reversed so the the factors of the first and second set line up
    ## Ex.  Factors of 24 = 1,2,3,4 || 6,8,12,24
            ## 4*6 = 24: firstSet[3]=4 and secondSet[3]=6
    secondSet.reverse()
    return secondSet
