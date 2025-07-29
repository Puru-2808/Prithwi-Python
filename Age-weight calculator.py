print("............Age-Weight Calculator...........")

while True:
    year=float(input("Enter child's age in year(0 to 12):  "))
    while True:
        if year>12 or year<0:
            print("Invalid input")
            year=float(input("Enter child's age in year(0 to 12):  "))
        else:
            break
    month=float(input("Enter child's age in month: "))
    day=float(input("Enter child's age in day: "))

    d=(year*12*30)+(month*30)+day
    
    if d<=90:                         # 0 to 3 months
        w1=(2500+(25*d))/1000
        w2=(3000+(25*d))/1000
        print("Minimum weight: ",w1,"Kg")
        print("Maximum weight: ",w2,"Kg")
    elif d<=150:                            # by 5 months
      w1=(2800*2)/1000
      w2=(3000*2)/1000
      print("Minimum weight: ",w1,"Kg")
      print("Maximum weight: ",w2,"Kg")
    elif d<=360:                           # by 1 year
      w1=(2800*3)/1000
      w2=(3000*3)/1000
      print("Minimum weight: ",w1,"Kg")
      print("Maximum weight: ",w2,"Kg")
    elif d<=720:                           # by 2 years
       w1=(2800*4)/1000
       w2=(3000*4)/1000
       print("Minimum weight: ",w1,"Kg")
       print("Maximum weight: ",w2,"Kg")
    elif d<=(12*12*30):                    # after 2 years upto 12 years
       w1=((2800*4)+(2500*((d-720)/(30*12))))/1000
       w2=((3000*4)+(3000*((d-720)/(30*12))))/1000
       print("Minimum weight: ",w1,"Kg")
       print("Maximum weight: ",w2,"Kg")
    else:
      print("Invalid input")
    q=str(input("Do you want to continue?(yes/no): "))
    
    if q=="no":
        break
print("....Calculator is closed.Thanks for using....")