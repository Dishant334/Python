class Car:
 
    def __init__(self,brand,model): #self is this of other languages
        self.brand= brand
        self.model= model

    def name(self):
        print(f'Model is {self.model} & brand is {self.brand}  {self.battery_size}')        

class ElectricCar(Car):

    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size



my_car=ElectricCar('toyota','corolla','10')
my_car.name()