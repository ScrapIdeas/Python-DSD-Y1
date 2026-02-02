loopityloop = True
def recursion():
    number1 = 0
    loopityloop = True
    number1+=1
    recursion()
    if(number1 == 10):
        print("Uh-Oh!")
        loopityloop = False
    return number1


while(loopityloop == True):
    recursion()
    print(number1)


