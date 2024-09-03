class Car:
  
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        # print(brand,model)
    
    def display(self):
        print(self.__brand,"",self.model)


class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        self.batterySize=batterySize
        super().__init__(brand,model)
        print(brand,model,batterySize)

Tesla=ElectricCar("TATA","Curvv",250)
Tesla.display()