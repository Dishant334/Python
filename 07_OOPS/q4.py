class Car:
 
    def __init__(self,brand,model): #self is this of other languages
        
        self.__brand= brand
        self.model= model

    def get_brand(self):
        return self.__brand + ' ! '
    def name(self):
        print(f'Model is {self.model} & brand is {self.__brand}  {self.battery_size}')        

class ElectricCar(Car):

    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size



my_car=ElectricCar('toyota','corolla','10')
print(my_car.__brand)
print(my_car.get_brand())