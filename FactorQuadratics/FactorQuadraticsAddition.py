import FactorQuadraticsInfo

# now edit in the x^2, be sure to use its factors
def FinalTest1(firstSetA, secondSetA, firstSetC, secondSetC, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fC = firstSetC
    sC = secondSetC

    for y in range (len(fA)):
        for x in range (len(fC)):
            if fA[y] * fC[x] + sA[y] * sC[x] == b:
                final = ("(" + str(fA[y]) + "x + " + str(sC[x]) + ")(" + str(sA[y]) + "x + " + str(fC[x]) + ")")
    return final

def FinalTest2(firstSetA, secondSetA, firstSetC, secondSetC, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fC = firstSetC
    sC = secondSetC

    for y in range (len(fA)):
        for x in range (len(fC)):
            if sA[y] * fC[x] + fA[y] * sC[x] == b:
                final = ("(" + str(sA[y]) + "x + " + str(sC[x]) + ")(" + str(fA[y]) + "x + " + str(fC[x]) + ")")
    return final

def FinalTest3(firstSetA, secondSetA, firstSetB, secondSetB, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fB = firstSetB
    sB = secondSetB

    for y in range (len(fA)):
        for x in range (len(fB)):
            if fA[y] * fB[x] + sA[y] * sB[x] == c:
                final = ("(" + str(fA[y]) + "x + " + str(sB[x]) + ")(" + str(sA[y]) + "x + " + str(fB[x]) + ")")
    return final

def FinalTest4(firstSetA, secondSetA, firstSetB, secondSetB, a, b, c):
    final = 0
    fA = firstSetA
    sA = secondSetA
    fB = firstSetB
    sB = secondSetB

    for y in range (len(fA)):
        for x in range (len(fB)):
            if sA[y] * fB[x] + fA[y] * sB[x] == c:
                final = ("(" + str(sA[y]) + "x + " + str(sB[x]) + ")(" + str(fA[y]) + "x + " + str(fB[x]) + ")")

    return final

def Main():
    ## remeber to test perfect square factors, they are currently factored out!!!!
    numbers = FactorQuadraticsInfo.GetNumbers()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    d = 1

    refinedNumbers = FactorQuadraticsInfo.GetSimplified(a,b,c,numbers)
    if len(refinedNumbers) > 0:
        a = int(refinedNumbers[0])
        b = int(refinedNumbers[1])
        c = int(refinedNumbers[2])
        d = int(refinedNumbers[3])

    ## got factors of x^2 and constant
    factorsA = FactorQuadraticsInfo.GetFactors(numbers, a)
    factorsB = FactorQuadraticsInfo.GetFactors(numbers, b)
    factorsC = FactorQuadraticsInfo.GetFactors(numbers, c)

    ## info for x^2
    halfA = int (len(factorsA)/2)
    firstSetA = FactorQuadraticsInfo.GetFirstSet(factorsA, halfA)
    secondSetA = FactorQuadraticsInfo.GetSecondSet(factorsA, firstSetA, halfA)

    ## info for x
    halfB = int (len(factorsB)/2)
    firstSetB = FactorQuadraticsInfo.GetFirstSet(factorsB, halfB)
    secondSetB = FactorQuadraticsInfo.GetSecondSet(factorsB, firstSetB, halfB)

    ## info for constant
    halfC = int (len(factorsC)/2)
    firstSetC = FactorQuadraticsInfo.GetFirstSet(factorsC, halfC)
    secondSetC = FactorQuadraticsInfo.GetSecondSet(factorsC, firstSetC, halfC)

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

    ## only tests addition    
    final = FinalTest1(firstSetA, secondSetA, firstSetC, secondSetC, a, b, c)
    if final == 0:
        final = FinalTest2(firstSetA, secondSetA, firstSetC, secondSetC, a, b, c)
    if final == 0:
        final = FinalTest3(firstSetA, secondSetA, firstSetB, secondSetB, a, b, c)
    if final == 0:
        final = FinalTest4(firstSetA, secondSetA, firstSetB, secondSetB, a, b, c)
    
    print (d, final)
