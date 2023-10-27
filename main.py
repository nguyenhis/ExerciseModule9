
#1
class Car:
    def __init__(self, regPlate, maxSpeed):
        self.regPlate = regPlate
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0
#2
    def accelerate(self, acceleration):
        self.speed = min(max(self.speed+acceleration, 0), self.maxSpeed)
#3
    def drive(self, time):
        self.odometer += self.speed * time

Porsche = Car("ABC-313", 240)
print(f"Register plate {Porsche.regPlate}, Max speed {Porsche.maxSpeed} km/h, "
      f"Current Speed {Porsche.speed} km/h, Odometer {Porsche.odometer} km.")


Porsche.accelerate(30)
Porsche.accelerate(70)
Porsche.accelerate(50)
print(f"Current Speed is {Porsche.speed} km/h.")
Porsche.accelerate(-200)
print(f"Current Speed is {Porsche.speed} km/h.")

Porsche.accelerate(60)
Porsche.drive(1.5)
print(f"Distance Travelled: {Porsche.odometer} km.")

#4
import random
cars = []
for i in range(10):
    cars.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

odomax = 0
while odomax < 10000:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1.)
        odomax = max(car.odometer, odomax)

for car in cars:
    print(f"{car.regPlate:6s}: {car.maxSpeed}, {car.odometer}")







