
import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, p):
        return math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2 + (self.z-p.z)**2)

    def move(self, d):
       self.x += d
       self.y += d
       self.z += d

    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return "[" + str(self.p1) + "," + str(self.p2) + ","  + str(self.p3) + "]"

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







