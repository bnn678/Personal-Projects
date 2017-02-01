def Run():
    type1 = input("What are you starting with: (Fah,Cel,Kel) ")
    type2 = input("What do you want to end with: (Fah,Cel,Kel) ")
    value1 = float(  input("How many degrees "+type1+":")  )

    if type1 == "Fah" and type2 == "Cel":
        final = FahToCel(value1)
    elif type1 == "Cel" and type2 == "Fah":
        final = CelToFah(value1)
    elif type1 == "Cel" and type2 == "Kel":
        final = CelToKel(value1)
    elif type1 == "Kel" and type2 == "Cel":
        final = KelToCel(value1)
    elif type1 == "Fah" and type2 == "Kel":
        final = FahToKel(value1)
    elif type1 == "Kel" and type2 == "Fah":
        final = KelToFah(value1)
    else:
        print ("Error raised")
        Run()

    print( str(final) + " "+type2+" ")
    print(" ")

def FahToCel(fah):
    celTemp = (5/9)*(fah-32)
    return celTemp

def CelToFah(cel):
    fahTemp = (cel*(9/5)) + 32
    return fahTemp

def CelToKel(cel):
    kelTemp = cel+273.15
    return kelTemp

def KelToCel(kel):
    celTemp = kel-273.15
    return celTemp

def FahToKel(fah):
    kelTemp = (fah-32)*(5/9)+273.15
    return kelTemp

def KelToFah(kel):
    fahTemp = (kel-273.15)*(9/5)+32
    return fahTemp
