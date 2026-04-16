import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Cascade Project")

# create a Player
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key press
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect the collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect the successful collision
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()