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
    
    if d<=90:
     w1=(2800+(25*d))/1000
     w2=(3000+(25*d))/1000
     print("Minimum weight: ",w1,"Kg")
     print("Maximum weight: ",w2,"Kg")
    elif d<=720:
      w1=(2800+(25*90)+(15*(d-90)))/1000
      w2=(3000+(25*90)+(15*(d-90)))/1000
      print("Minimum weight: ",w1,"Kg")
      print("Maximum weight: ",w2,"Kg")
    elif d<=4320:
      w1=(2800+(25*90)+(15*630)+((2500/360)*(d-720)))/1000
      w2=(3000+(25*90)+(15*630)+((3000/360)*(d-720)))/1000
      print("Minimum weight: ",w1,"Kg")
      print("Maximum weight: ",w2,"Kg")
    else:
      print("Invalid input")
    q=str(input("Do you want to continue?(yes/no): "))
    
    if q=="no":
        break
print("....Calculator is closed.Thanks for using....")