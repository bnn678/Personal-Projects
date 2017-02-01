import TempConversions
import FractionConversions

def CallTest(typeTest, count):
    while count < 3:
        if typeTest == "TempConversions":
            TempConversions.Run()
            Main()
        elif typeTest == "FractionConversions":
            FractionConversions.Run()
            Main()
        else:
            print ("Unknown directory.")
            count += 1
            typeTest = input("What would you like to convert: ")
    print ("Exceeded number of tests")

## Make a run file for each class to call
def Main():
    count = 0
    
    conversionList = ["TempConversions","FractionConversions"]
    print (conversionList)
    typeTest = input("What would you like to convert: ")

    CallTest(typeTest, count)
        
Main()
