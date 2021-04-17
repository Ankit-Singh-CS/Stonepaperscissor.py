import random
import time
i=0
while (i!=10):
    print("Your choice are:\n ""s:Stone\n","p:Paper\n","z:Scissor\n")
    x=input("Enter your choice here:")
    s="Stone"
    p="Paper"
    z="Scissor"

    if x=='s':
        print("Your choice is:Stone")
        a=random.choice((s,p,z))
        print("Computer choice is:",a)
        if a=="paper":
            print("You loose")
        elif a=="Stone":
            print("Draw")
        else:
            print("You Win")

    if x == 'p':
        print("Your choice is:Paper")
        b = random.choice((s,p,z))
        print("Computer choice is:", b)
        if b == "Scissor":
            print("You loose")
        elif b == "Paper":
            print("Draw")
        else:
            print("You Win")


    if x == 'z':
        print("Your choice is:Scissor")
        c = random.choice((s, p, z))
        print("Computer choice is:", c)
        if c == "Scissor":
            print("Draw")
        elif c == "Paper":
            print("You Win")
        else:
            print("You loose")
    i=i+1
    w=10-i
    print("$$$$$$$$ HAVE A NICE DAY lawde $$$$$$$$$")
    print("%% WHETHER YOU LOOSE OR WIN DON'T FORGET TO TRY AGAIN %%")
    print("You have",w,"chances left" )
    print("Made by Ankit Singh")
    time.sleep(5s
    )

