import DivisibleBy
import ReduceFraction
from decimal import *

def Run():
    type1 = input("What are you starting with: (Decimal, Fraction) ")

    if type1 == "Decimal":
        final = DecimalConvert()
    elif type1 == "Fraction":
        final = FractionConvert()
    else:
        print ("Unknown entry")
        Run()
    
    print (final)

def DecimalConvert():
    print ( "   Do not include repeating digits or numbers greater than 1" )
    num = float( input("Please enter the number: ") )

    length = len( str( num ) ) - 2 # digits after the decimal when in format 0.25 etc.
    denom = 10**length

    num = num * denom

    fraction = ReduceFraction.ReduceFraction(num, denom)
    num = fraction[0]
    denom = fraction[1]
    
##    num = num + (count * denom)

    if num > 1000000:
        print ("Value is not a clean fraction.")
        deciTest = input ("Would you like to display anyways: (Yes, No) ")
        if deciTest == "Yes":
                final = ( "(" + str ( num ) + "/" + str ( denom ) + ")" )

        while deciTest != "Yes" or "No":
            if deciTest == "Yes":
                final = ( "(" + str ( num ) + "/" + str ( denom ) + ")" )
            elif deciTest == "No":
                break
            else:
                print ("Unexpected insertion.")
                print ('')
                print ("Value is not a clean fraction.")
                deciTest = input ("Would you like to display anyways: (Yes, No)")
            
    else:
        final = ( "(" + str ( num ) + "/" + str ( denom ) + ")" )

    return final

def FractionConvert():
    num = int(  input("Numerator: ")  )
    denom = int(  input("Denominator: ")  )

    final = ( num/denom )

    return final
