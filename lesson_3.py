import random

class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        self.trip_distance += distance
        self.fuel += distance

car1 = Car("Daewoo", "White")
car2 = Car("Audi", "Grey")
car3 = Car("Dodje", "Red")

desired_dist = 100
race_dist = 0

while race_dist < desired_dist:
    for car in [car1, car2, car3]:
        distance = random.randrange(0, 9)
        car.move(distance)
        if car.trip_distance >= desired_dist:
            print(f"Переміг автомобіль {car.model}! Проїхав {car.trip_distance} км.")
            break
    else:
        race_dist += 1
        continue
    break


for car in [car1, car2, car3]:
    print(f"Автомобіль {car.model} проїхав {car.trip_distance} км. Залишок палива: {car.fuel}.")
