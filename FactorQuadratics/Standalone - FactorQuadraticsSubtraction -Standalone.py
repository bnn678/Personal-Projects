#######
## test cases:
## x^2 + 8x - 20
##  1(x + 10)(x - 2)
## x^2 - 4x - 5
#######

import ExpandQuadraticsInfo

def FinalTest1(firstSetA, secondSetA, firstSetB, secondSetB, firstSetC, secondSetC, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fB = firstSetB
    sB = secondSetB
    fC = firstSetC
    sC = secondSetC

    for y in range (len(fA)):
        for x in range (len(fC)):
            if fA[y] * fC[x] - sA[y] * sC[x] == b:
                final = ("(" + str(fA[y]) + "x + " + str(sC[x]) + ")(" + str(sA[y]) + "x + " + str(fC[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fC)):
                if sA[y] * fC[x] - fA[y] * sC[x] == b:
                    final = ("(" + str(sA[y]) + "x + " + str(sC[x]) + ")(" + str(fA[y]) + "x + " + str(fC[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fB)):
                if fA[y] * fB[x] - sA[y] * sB[x] == c:
                    final = ("(" + str(fA[y]) + "x + " + str(sB[x]) + ")(" + str(sA[y]) + "x + " + str(fB[x]) + ")")

    if final == 0:
        for y in range (len(fA)):
            for x in range (len(fB)):
                if sA[y] * fB[x] - fA[y] * sB[x] == c:
                    final = ("(" + str(sA[y]) + "x + " + str(sB[x]) + ")(" + str(fA[y]) + "x + " + str(fB[x]) + ")")

    return final

def Main():
    ## remeber to test perfect square factors, they are currently factored out!!!!
    numbers = ExpandQuadraticsInfo.GetNumbers()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    d = 1

    refinedNumbers = ExpandQuadraticsInfo.GetSimplified(a,b,c,numbers)
    if len(refinedNumbers) > 0:
        a = int(refinedNumbers[0])
        b = int(refinedNumbers[1])
        c = int(refinedNumbers[2])
        d = int(refinedNumbers[3])

    ## got factors of x^2 and constant
    factorsA = ExpandQuadraticsInfo.GetFactors(numbers, a)
    factorsB = ExpandQuadraticsInfo.GetFactors(numbers, b)
    factorsC = ExpandQuadraticsInfo.GetFactors(numbers, c)

    ## info for x^2
    halfA = int (len(factorsA)/2)
    firstSetA = ExpandQuadraticsInfo.GetFirstSet(factorsA, halfA)
    secondSetA = ExpandQuadraticsInfo.GetSecondSet(factorsA, firstSetA, halfA)

    ## info for x
    halfB = int (len(factorsB)/2)
    firstSetB = ExpandQuadraticsInfo.GetFirstSet(factorsB, halfB)
    secondSetB = ExpandQuadraticsInfo.GetSecondSet(factorsB, firstSetB, halfB)

    ## info for constant
    halfC = int (len(factorsC)/2)
    firstSetC = ExpandQuadraticsInfo.GetFirstSet(factorsC, halfC)
    secondSetC = ExpandQuadraticsInfo.GetSecondSet(factorsC, firstSetC, halfC)

    ## takes out perfect square numbers
    z = max(factorsA) ** 0.5
    if z == int (z):
        firstSetA.append(secondSetA[len(secondSetA) - 1])
    z = max(factorsB) ** 0.5
    if z == int (z):
        firstSetB.append(secondSetB[len(secondSetB) - 1])
    z = max(factorsC) ** 0.5
    if z == int (z):
        firstSetC.append(secondSetC[len(secondSetC) - 1])

    final = FinalTest(firstSetA, secondSetA, firstSetB, secondSetB, firstSetC, secondSetC, a, b, c)
    print (d, final)
    
    Main()
Main()
