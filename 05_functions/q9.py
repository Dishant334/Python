def even_generator(a):
    for i in range(2,a+1,1):
        yield i
    

for num in even_generator(10):
    print(num)
