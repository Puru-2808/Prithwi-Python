import random
while True:
    a1=0
    b1=0
    print("Doing Toss")
    t=random.choice(["Bat","Bowl"])
    print("You will",t)

    
    if t=="Bat":
        a=int(input("Select any Number (1 to 6): "))
        b=random.randint(1,6)
        while True:
            if a>6 or a<1:
                print("Enter valid input")
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
            else:
                break
        while True:
            if a!=b:
                a1+=a
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
                while True:
                    if a>6 or a<1:
                        print("Enter valid input")
                        a=int(input("Select any Number (1 to 6): "))
                        b=random.randint(1,6)
                    else:
                        break
            else:
                break
        print("You're out, your run is: ",a1," computer will bat")
        a=int(input("Select any Number (1 to 6): "))
        b=random.randint(1,6)
        while True:
            if a>6 or a<1:
                print("Invalid Input")
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
            else:
                break
        while True:
            if a!=b:
                b1+=b
                if b1>a1:
                    break
                else:
                    a=int(input("Select any Number (1 to 6): "))
                    b=random.randint(1,6)
                    while True:
                        if a>6 or a<1:
                            print("Enter valid input")
                            a=int(input("Select any Number (1 to 6): "))
                            b=random.randint(1,6)
                        else:
                            break
            else:
                break
        print("Computer's run is: ",b1)
        if a1>b1:
            print("You win")
        else:
            print("Computer win")
    elif t=="Bowl":
        a=int(input("Select any Number (1 to 6): "))
        b=random.randint(1,6)
        while True:
            if a>6 or a<1:
                print("Enter valid input")
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
            else:
                break
        while True:
            if a!=b:
                b1+=b
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
                while True:
                    if a>6 or a<1:
                        print("Enter valid input")
                        a=int(input("Select any Number (1 to 6): "))
                        b=random.randint(1,6)
                    else:
                        break
            else:
                break
        print("Computer is out, computer's run is: ",b1," you will bat")
        a=int(input("Select any Number (1 to 6): "))
        b=random.randint(1,6)
        while True:
            if a>6 or a<1:
                print("Invalid Input")
                a=int(input("Select any Number (1 to 6): "))
                b=random.randint(1,6)
            else:
                break
        while True:
            if a!=b:
                a1+=a
                if a1>b1:
                    break
                else:
                    a=int(input("Select any Number (1 to 6): "))
                    b=random.randint(1,6)
                    while True:
                        if a>6 or a<1:
                            print("Enter valid input")
                            a=int(input("Select any Number (1 to 6): "))
                            b=random.randint(1,6)
                        else:
                            break
            else:
                break
        print("your run is: ",a1)
        if a1>b1:
            print("You win")
        else:
            print("Computer win")
    v=input("Do uou want to play again?(yes/no): ")
    while True:
        if v!="yes" and v!="no":
            print("Enter valid input")
            v=input("Do uou want to play again?(yes/no): ")
        else:
            break
    if v=="no":
        break
print("Thanks for playing. Hope you enjoy")