import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from roadways import draw_roads

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create instances
draw_roads()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Create initial cars
for i in range(100):
    car_manager.random_car()
    car_manager.move()

# Screen instructions
screen.listen()
screen.onkeypress(player.move, "Up")

# Game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a car at random intervals
    car_manager.random_car()

    # Movement cars
    car_manager.move()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.gameover()

    # Go to next level
    if player.finish_line_reached():
        player.go_to_start()
        scoreboard.upgrade_level()
        car_manager.increase_speed()


screen.exitonclick()

