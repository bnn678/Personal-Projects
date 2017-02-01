def ReduceFraction(num, denom):
    from fractions import gcd

    divisor = gcd (num, denom)
    
    num = num / divisor 
    denom = denom / divisor
    
    print ( str(num) + "/" + str (denom) )
