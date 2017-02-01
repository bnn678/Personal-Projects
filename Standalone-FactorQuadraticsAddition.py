#######
##
## ax2 + bx + c
##
## You must find all factors of c
## Then test which add up to b when multiplied by a
##
## 
## 
#######

#######
## test cases:
## 2x^2 + 13x + 20
##  1(2x + 5)(x + 4)
## 4x^2 + 8x + 4
##  4(x + 1)(x + 1)
## 6x^2 + 20x + 22
##  (3x + 5)(2x + 4)
##  2(3x + 5)(x + 2)
## 3x^2 + 10x + 11
##  (3x + 5)(x + 2)
#######

## Ex: 3x^2 + 4x + 1 = (3x+1)(x+1)
## Final Test 1-4 are the four possible ways to find the solution
## Test 1&2 deal with factors of a and c
## Test 3&4 deal with factors of a and b

import FactorQuadraticsInfo
from FactorQuadraticsInfo import *

def FinalTest(firstSetA, secondSetA, firstSetB, secondSetB, firstSetC, secondSetC, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fB = firstSetB
    sB = secondSetB
    fC = firstSetC
    sC = secondSetC

    for y in range (len(fA)):
        for x in range (len(fC)):
            if fA[y] * fC[x] + sA[y] * sC[x] == b:
                final = ("(" + str(fA[y]) + "x + " + str(sC[x]) + ")(" + str(sA[y]) + "x + " + str(fC[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fC)):
                if sA[y] * fC[x] + fA[y] * sC[x] == b:
                    final = ("(" + str(sA[y]) + "x + " + str(sC[x]) + ")(" + str(fA[y]) + "x + " + str(fC[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fB)):
                if fA[y] * fB[x] + sA[y] * sB[x] == c:
                    final = ("(" + str(fA[y]) + "x + " + str(sB[x]) + ")(" + str(sA[y]) + "x + " + str(fB[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fB)):
                if sA[y] * fB[x] + fA[y] * sB[x] == c:
                    final = ("(" + str(sA[y]) + "x + " + str(sB[x]) + ")(" + str(fA[y]) + "x + " + str(fB[x]) + ")")

    return final

def Main():
    ## Gets the test numbers to use, could also have 'Main(numbers)'
    numbers = FactorQuadraticsInfo.GetNumbers()
    
    ## The code will ONLY work with whole numbers, no decimals 
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    d = 1

    ## Factors out a common factor if there is one, NOTE: d = common factor
    refinedNumbers = FactorQuadraticsInfo.GetSimplified(a,b,c)
    if len(refinedNumbers) > 0:
        a = int(refinedNumbers[0])
        b = int(refinedNumbers[1])
        c = int(refinedNumbers[2])
        d = int(refinedNumbers[3])

    ## Get factors of a, b, and c  in EQ: ax^2 + bx + c
    factorsA = FactorQuadraticsInfo.GetFactors(a)
    factorsB = FactorQuadraticsInfo.GetFactors(b)
    factorsC = FactorQuadraticsInfo.GetFactors(c)

    ## Info for ax^2
    halfA = int (len(factorsA)/2)
    firstSetA = FactorQuadraticsInfo.GetFirstSet(factorsA, halfA)
    secondSetA = FactorQuadraticsInfo.GetSecondSet(factorsA, firstSetA, halfA)

    ## Info for bx
    halfB = int (len(factorsB)/2)
    firstSetB = FactorQuadraticsInfo.GetFirstSet(factorsB, halfB)
    secondSetB = FactorQuadraticsInfo.GetSecondSet(factorsB, firstSetB, halfB)

    ## Info for constant
    halfC = int (len(factorsC)/2)
    firstSetC = FactorQuadraticsInfo.GetFirstSet(factorsC, halfC)
    secondSetC = FactorQuadraticsInfo.GetSecondSet(factorsC, firstSetC, halfC)

    ## Takes out perfect square numbers
    z = max(factorsA) ** 0.5
    if z == int (z):
        firstSetA.append(secondSetA[len(secondSetA) - 1])
    z = max(factorsB) ** 0.5
    if z == int (z):
        firstSetB.append(secondSetB[len(secondSetB) - 1])
    z = max(factorsC) ** 0.5
    if z == int (z):
        firstSetC.append(secondSetC[len(secondSetC) - 1])

    ## only tests addition    
    final = FinalTest(firstSetA, secondSetA, firstSetB, secondSetB, firstSetC, secondSetC, a, b, c)
    
    print (d, final)
    Main()
Main()
