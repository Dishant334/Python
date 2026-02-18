
def rec(n,i):
    if(i==n):
        return 1;
    return (i+1)*rec(n,i+1)

print(rec(6,0))