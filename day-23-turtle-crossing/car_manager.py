from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def random_car(self):
        randint = random.randint(1, 6)
        if randint <= self.speed // 5: # Increases the chance to compensate for higher speed
            self.create_car()

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        # Define position
        random_y = self.create_random_y()
        car.goto(320, random_y)
        self.cars.append(car)

    def create_random_y(self):
        # List the y_cor of the last 5 created cars
        y_cor_last_5_cars = []
        number_of_cars = len(self.cars)
        if number_of_cars == 0:
            pass
        else:
            max_range = min(number_of_cars, 5) + 1
            for i in range (-1, -max_range, -1):
                y_cor = self.cars[i].ycor()
                y_cor_last_5_cars.append(y_cor)
        # Create a random value different than the value of the 5 previous cars
        random_y = random.randrange(-230, 270, 30)
        while random_y in y_cor_last_5_cars:
            random_y = random.randrange(-230, 270, 30)
        return random_y

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.setx(new_x)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
