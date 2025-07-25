print("......CALENDER (2000-2099)......")


dd=["sunday","monday", "tuesday", "wednesday", "thursday","friday","saturday"]

while True:
    date=int(input("enter date: "))
    month=int(input("enter month: "))
    year=int(input("enter year: "))
    if month==1:
        d=date
        while d>=7:
            d=d-7
    elif month==2:
        d=date+31
        while d>=7:
            d=d-7
    elif month==3:
        if year%4==0:
            d=date+31+29
        else:
            d=date+31+28
        while d>=7:
            d=d-7
    elif month==4:
        if year%4==0:
            d=date+31+29+31
        else:
            d=date+31+28+31
        while d>=7:
            d=d-7
    elif month==5:
        if year%4==0:
            d=date+31+29+31+30
        else:
            d=date+31+28+31+30
        while d>=7:
            d=d-7
    elif month==6:
        if year%4==0:
            d=date+31+29+31+30+31
        else:
            d=date+31+28+31+30+31
        while d>=7:
            d=d-7
    elif month==7:
        if year%4==0:
            d=date+31+29+31+30+31+30
        else:
           d=date+31+28+31+30+31+30
        while d>=7:
           d=d-7
    elif month==8:
        if year%4==0:
            d=date+31+29+31+30+31+30+31
        else:
           d=date+31+28+31+30+31+30+31
        while d>=7:
           d=d-7
    elif month==9:
        if year%4==0:
            d=date+31+29+31+30+31+30+31+31
        else:
            d=date+31+28+31+30+31+30+31+31
        while d>=7:
            d=d-7
    elif month==10:
        if year%4==0:
            d=date+31+29+31+30+31+30+31+31+30
        else:
           d=date+31+28+31+30+31+30+31+31+30
        while d>=7:
          d=d-7
    elif month==11:
        if year%4==0:
            d=date+31+29+31+30+31+30+31+31+30+31
        else:
           d=date+31+28+31+30+31+30+31+31+30+31
        while d>=7:
           d=d-7
    elif month==12:
        if year%4==0:
            d=date+31+29+31+30+31+30+31+31+30+31+30
        else:
           d=date+31+28+31+30+31+30+31+31+30+31+30
        while d>=7:
          d=d-7
        
    a=len(dd)-1+(d+(year-1)-len(dd))
    while year%4!=0:
            year=year+1
    b=(year-4)//4
    c=a+b
    while c>=len(dd):
            c=c-len(dd)
    print(dd[c])
    q=str(input("Do you want to continue?(yes/no)?: "))
    if q=="no":
        break
print("..........Thank you for using...........")