def FindNextPrime():
    with open("PrimeList.py", "r") as PrimeList:
        primes = PrimeList.read()
        PrimeList.close()

    try:  
        primes = primes.replace( '\n', '' )
        primes = primes.split(',')
            
        for item in range( len(primes) ):
            primes[item] = int( primes[item] )
    except( ValueError ):
        print('Check the PrimeList file for errors.')
        return 0
        
    found = False
    num = primes[-1]
    while found == False:
        num += 1
        found = IsPrime( num, primes )
        
    with open("PrimeList.py", "a") as PrimeList:
        PrimeList.write( ',' + str( num ) )
    PrimeList.close()
    
    return num

def IsPrime( num, primes ):
    for prime in primes:
        if num % prime == 0:
            return False
    return True
