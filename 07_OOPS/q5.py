class Car:
    total_car=0
    def __init__(self,brand,model): #self is this of other languages
        
        self.__brand= brand
        self.__model= model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + ' ! '
    def name(self):
        print(f'Model is {self.__model} & brand is {self.__brand}  {self.battery_size}')        

    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
class ElectricCar(Car):

    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric Charge"
    
  


my_car=ElectricCar('toyota','corolla','10')

print(my_car.general_description)