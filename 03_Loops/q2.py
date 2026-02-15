n=int(input("Enter the total numbers"))
count=0

for ch in range(1,n+1):
    if(ch%2==0):
        count+=ch

print(count)        