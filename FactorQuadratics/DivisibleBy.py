def TestNumbersSolve(num):
    testNums = []
    for x in range ( 1, int ( (num**0.5) + 1 ) ):
        if num % x == 0:
            testNums.append(x)
    return testNums

def Factors(num, testNums):
    factors = []
    for i in testNums:
        a = 1

        while num % (i*a) == 0:
            if num % (i*a) == 0:
                factors.append(i*a)
            a = a + 1
                
        if num % (i*a) == 0:
            factors.append(i*a)
    return factors

def CleanUp(factors, final):
    factors.sort()

    for value in factors:
        if value not in final:
            final.append(value)

    return final

def OtherHalf(num, factors, testNums):
    for i in testNums:
        other = num / i
        factors.append(other)
                       
def Main(num):
    final = []

    testNums = TestNumbersSolve(num)
    factors = Factors(num, testNums)
    OtherHalf(num, factors, testNums)
    final = CleanUp(factors, final)
    return final
