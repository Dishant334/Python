s=int(input("Enter the age"))
price=0;
day=input("Enter the day")

if(0<s<18):
    price+=8
else:
    price+=12


price=price-2 if day=='wednesday' else price


print(price)