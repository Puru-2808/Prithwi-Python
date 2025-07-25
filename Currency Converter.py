print("Currency coverter to INR and vice versa")

while True:
    a=str(input("Enter currency you want to convert: "))
    b=float(input("Enter price: "))    
    if a=="usd":
        p=b*84.11
        print("Rs.",p)
    elif a=="rupees":
        p=b/84.11
        p1=b/22.40
        p2=b/109.96
        p3=b/274.36
        p4=b/0.88
        p5=b/92.05
        print(p," usd",'\n',p1," sar",'\n',p2," pound",'\n',p3," kd",'\n',p4," ruble",'\n',p5," euro")
    elif a=="sar":
        p=b*22.40
        print("Rs.",p)
    elif a=="pound":
        p=b*109.96
        print("Rs.",p)
    elif a=="kd":
        p=b*274.36
        print("Rs.",p)
    elif a=="ruble":
        p=b*0.88
        print("Rs.",p)
    elif a=="euro":
       p=b*92.05
       print("Rs.",p)
    c=str(input("Do you want to continue(y/n): "))
    if c=="n":
       break
print("........Closed........")