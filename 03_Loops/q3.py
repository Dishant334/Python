n=int(input("Enter the number you want table of"))
for i in range(1,11):
    if(i==5):
        continue;
    print(n,' * ',i,' = ',n*i)