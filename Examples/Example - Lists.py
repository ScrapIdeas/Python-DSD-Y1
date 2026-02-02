import os
thing = []
L = True
N = 0
R = ""


while(L == True):
    print("Tell me, what are your top 5 songs?")
    R = input("")
    thing.append(R)
    N = N + 1
    os.system("CLS")
    if(N == 5):
        L == False
        print(f"Your top five songs are: {list}")
        break