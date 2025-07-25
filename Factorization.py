while True:
    a=int(input("Enter number: "))
    
    b=a

    bb=[]

    while b >= 1:
        b=b/10
        bb.append(b)
    n=len(bb)               # The input numner is of "n" digit
        
    for i in range(1,10**n):
        for j in range(1,10**n):
            if i*j==a:
                print(i,"*",j)
    c=str(input("Do you want to continue(yes/no)?: "))
    if c=="no":
        break
print("Thanks for using")