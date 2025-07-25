while True:
    a=int(input("enter number: "))
    b=int(input("enter number: "))

    aa=[]
    bb=[]
    cc=[]

    for i in range(1,a+1):
         if a%i==0:
             aa.append(i)
    for j in range(1,b+1):
        if b%j==0:
             bb.append(j)

    for i in range(len(aa)):
         if aa[i] in bb:
             cc.append(aa[i])

    max=cc[0]
    for i in range(len(cc)):
          if cc[i]>=max:
               max=cc[i]
    print("gcd:",max)
    c=str(input("do you want to continue?(y/n): "))
    if c=="n":
        break
print("thank you")