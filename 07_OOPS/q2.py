class Car:
 
    def __init__(self,brand,model): #self is this of other languages
        self.brand= brand
        self.model= model

    def name(self):
        print(f'Model is {self.model} & brand is {self.brand}')        

my_car=Car('toyota','corolla')
my_car.name()