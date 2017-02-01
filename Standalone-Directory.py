'''
Intended to create a directory of all my methods

Brandon Shaver
Python Directory
Started Thursday, October 16, 2013

I proudly present a list of all programs created in my time to be
    in, for, and by programs made by people like me.
'''

import Conversions
import DivisibleBy
import Standalone-FactorQuadraticsAddition
import GCF
import ReduceFraction

functions = ['Conversions', 'DivisibleBy', 'FactorQuadraticsAddition',
             'GCF', 'ReduceFraction', ]

def GetProgram():
    print (functions)
    test = input("What would you like to do: ")
    return test

def Main():
    test = GetProgram()
    
    if test == ('ReduceFraction'):
        ReduceFraction.Main()
        
    elif test == ('DivisibleBy'):
        num = int( input("What number are you testing: ") )
        print ( DivisibleBy.Main(num) )
        
    elif test == ('FactorQuadraticsAddition'):
        FactorQuadraticsAddition.Main()

    elif test == ('Conversions'):
        Conversions.Main()

    elif test == ('GCF'):
        a = int( input("First number: ") )
        b = int( input("Second number: ") )
        print ( GCF.Main(a, b) )
        
    else:
        print ("Unknown directory")
        Main()
    
Main()
