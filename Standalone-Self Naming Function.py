def Main():
    num = input ("How many do you want: ")
    name = input ("What do you want them to be called: ")
    for x in range ( int(num) ):
        locals()[name + str(x)] = x
Main()
