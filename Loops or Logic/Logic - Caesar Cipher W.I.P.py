#If I dont finish this now, I'll more than likely submit it then resubmit it with the actual program later :O(
#P.S. It would definitely help if I could move to a better seat.



def ceasarciphr(thetext, theshift):
    
    theshift = 0
    thetext = ""
    result = "" 

    for char in thetext:
        if char.isupper():
            result += chr((ord(char) - 65 + theshift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + theshift) % 26 + 97)



theshift = int(input("So.. what is your shift?"))
thetext = input("And what is your text?")
ceasarciphr(thetext,theshift)