def Main(name, num):
    for x in range (num):
        locals()[name + str(x)] = x
