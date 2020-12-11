class Vehical:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def fare(self):
        return  self.mileage*100
class Bus(Vehical):
    pass

School_bus = Bus("School Volov",12,50)
print("Total Bus fare is",School_bus.fare())
