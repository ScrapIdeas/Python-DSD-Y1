listA = [1,2,3]
#It also accepts integers, like a normal list.

#Mixed-type.
listB = [1,"2",3.0]
#It accepts '2', and 3.0 which are char / str and floats in there.

decimalresult = listA[1] + listB[2]
print(decimalresult)
#Addition between decimals works fine, it uses ListB's 3.0 with listA's 2.


if(listA[0] <= listB[2]):
    print("dec.")
#Easily compares yet again.
elif(listA[2] == listB[2]):
    print("equal dec.")
#Easily compares with no problem, no crashes and what not except for powershell whining in the background.