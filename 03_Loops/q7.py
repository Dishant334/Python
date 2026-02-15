got=False
while got ==False:
    n=int(input("Enter a number in 1 to 10"))
    if(n in range(1,11)):
        print('Got the number')
        got=True