print("......CALENDER (2000-2099)......")

import pandas as pd

dd=["sunday","monday", "tuesday", "wednesday", "thursday","friday","saturday"]

d1=[]
ff=[]
nn=[]

month=int(input("enter month: "))
year=int(input("enter year: "))

if month==1:
        for i in range(1,32):
            date=i    
            d=date
            nn.append(d)
            while d>=7:
                 d=d-7
            d1.append(d)
elif month==2:
        if year%4==0:
            for i in range(1,30):
                date=i
                nn.append(i)
                d=date+31
                while d>=7:
                     d=d-7
                d1.append(d)
        else:
            for i in range(1,29):
                date=i
                nn.append(i)
                d=date+31
                while d>=7:
                    d=d-7
                d1.append(d)
elif month==3:
        for i in range(1,32):
            date=i
            nn.append(i)
            if year%4==0:
                  d=date+31+29
            else:
                 d=date+31+28
            while d>=7:
                d=d-7
            d1.append(d)
elif month==4:
        for i in range(1,31):
            date=i
            nn.append(date)
            if year%4==0:
                  d=date+31+29+31
            else:
                 d=date+31+28+31
            while d>=7:
                 d=d-7
            d1.append(d)
elif month==5:
        for i in range(1,32):
            date=i
            nn.append(date)
            if year%4==0:
                  d=date+31+29+31+30
            else:
                  d=date+31+28+31+30
            while d>=7:
                 d=d-7
            d1.append(d)
elif month==6:
        for i in range(1,31):
            date=i
            nn.append(date)
            if year%4==0:
                 d=date+31+29+31+30+31
            else:
                d=date+31+28+31+30+31
            while d>=7:
                d=d-7
            d1.append(d)
elif month==7:
        for i in range(1,32):
            date=i
            nn.append(date)
            if year%4==0:
                 d=date+31+29+31+30+31+30
            else:
                 d=date+31+28+31+30+31+30
            while d>=7:
                d=d-7
            d1.append(d)
elif month==8:
        for i in range(1,32):
            date=i
            nn.append(date)
            if year%4==0:
                 d=date+31+29+31+30+31+30+31
            else:
                 d=date+31+28+31+30+31+30+31
            while d>=7:
                d=d-7
            d1.append(d)
elif month==9:
        for i in range(1,31):
            date=i
            nn.append(date)
            if year%4==0:
                d=date+31+29+31+30+31+30+31+31
            else:
               d=date+31+28+31+30+31+30+31+31
            while d>=7:
              d=d-7
            d1.append(d)
elif month==10:
        for i in range(1,32):
            date=i
            nn.append(date)
            if year%4==0:
                  d=date+31+29+31+30+31+30+31+31+30
            else:
                 d=date+31+28+31+30+31+30+31+31+30
            while d>=7:
              d=d-7
            d1.append(d)
elif month==11:
        for i in range(1,31):
            date=i
            nn.append(date)
            if year%4==0:
                 d=date+31+29+31+30+31+30+31+31+30+31
            else:
                 d=date+31+28+31+30+31+30+31+31+30+31
            while d>=7:
              d=d-7
            d1.append(d)
elif month==12:
        for i in range(1,32):
            date=i
            nn.append(date)
            if year%4==0:
                  d=i+31+29+31+30+31+30+31+31+30+31+30
            else:
                  d=i+31+28+31+30+31+30+31+31+30+31+30
            while d>=7:
                 d=d-7
            d1.append(d)

for i in range(len(d1)):
           a=len(dd)-1+(d1[i]+(year-1)-len(dd))
           y=year
           while y%4!=0:
                  y=y+1
           b=(y-4)//4
           c=a+b
           while c>=len(dd):
                 c=c-len(dd)
           f=dd[c]
           ff.append(f)
print(pd.DataFrame(nn,ff))

print("..........Thank you for using...........") 