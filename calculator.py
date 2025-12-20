print("..........CALCULATOR............")

while True:
    n=float(input("Enter number: "))
    op=str(input("Enter operation type(+,-,*,/): "))
    while True:
        if op!="+" and op!="-" and op!="*" and op!="/":
            print("Enter valid operation type")
            op=str(input("Enter operation type(+,-,*,/): "))
        else:
           break
    n1=float(input("Enter number: "))
    if op=="+":
        s=n+n1
        print(s)
    elif op=="-":
        s=n-n1
        print(s)
    elif op=="*":
        s=n*n1
        print(s)
    elif op=="/":
        while True:
            if n1==0:
                print("Can't divide by zero")
                n1=float(input("Enter number: "))
            else:
                break
        s=n/n1
        print(s)
    con=str(input("Do you want to continue? (y/n): "))
    if con=="y":
        continue
    else:
        print("Thank you for using the calculator")
        break