class Car:

    def __init__(self,brand,doors,color,year, name):
        self.brand=brand
        self.doors=doors
        self.color=color
        self.year=year
        self.name=name
    
    def max_speed(self,max_speed):
        print("")
        print('The max speed of the car is: '+ str(max_speed))

    def drive(self,current_speed):
        print("")
        print(self.brand+" "+self.name+" is driving at "+str(current_speed)+"km/h")
    
    def security_alarm(self):
        print("")
        print("niiiinoooooniiiiinnoooonnniiiiooo")

my_car=Car('Audi','3','White','2016','A1')

my_car.max_speed(230)

my_car.drive(88)

my_car.security_alarm()
