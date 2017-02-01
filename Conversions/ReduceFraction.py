def ReduceFraction(num, denom):
    from fractions import gcd

    divisor = gcd (num, denom)
    
    num = num / divisor 
    denom = denom / divisor
    
    final = [num, denom]

    return final
