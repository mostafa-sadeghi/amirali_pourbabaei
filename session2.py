from snake_game_utils import *
from time import sleep


def onclose():
    # file = open("snake_result.txt", "w")
    # file.write(str(high_score))
    # file.close()
    with open("snake_result.txt", "w") as f:
        f.write(str(high_score))

    global running
    running = False


score = 0

try:
    # file = open("snake_result.txt", "r")
    with open("snake_result.txt") as f:
        high_score = int(f.read())
except:

    high_score = 0

main_surface = make_screen()
root = main_surface._root
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", onclose)
# main_surface.register_shape("strawberry.gif")

snake_head = make_turtle("square", "blue")
snake_head.direction = ""
snake_food = make_turtle("circle", "red")
# snake_food = make_turtle("strawberry.gif", "red")
change_food_position(snake_food)


score_board = make_turtle("square", "white")
score_board.goto(0, 260)
score_board.hideturtle()


main_surface.listen()
main_surface.onkeypress(lambda: change_dir_to_up(snake_head), "Up")
main_surface.onkeypress(lambda: change_dir_to_down(snake_head), "Down")
main_surface.onkeypress(lambda: change_dir_to_left(snake_head), "Left")
main_surface.onkeypress(lambda: change_dir_to_right(snake_head), "Right")

main_surface.onkeypress(lambda: change_dir_to_up(snake_head), "w")
main_surface.onkeypress(lambda: change_dir_to_down(snake_head), "s")
main_surface.onkeypress(lambda: change_dir_to_left(snake_head), "a")
main_surface.onkeypress(lambda: change_dir_to_right(snake_head), "d")
snake_tails = list()
running = True
while running:
    main_surface.update()
    # update the scoreboard
    score_board.clear()
    score_board.write(f"Score: {score}\tHighScore:{high_score}", align="center",
                      font=("Terminal", 28))
    # Checking snake_head and snake_food collisions
    if snake_head.distance(snake_food) < 20:
        score += 1
        if score > high_score:
            high_score = score
        change_food_position(snake_food)
        new_tail = make_turtle("square", "cyan")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        prev_x_cor = snake_tails[i-1].xcor()
        prev_y_cor = snake_tails[i-1].ycor()
        snake_tails[i].setpos(prev_x_cor,
                              prev_y_cor)

    if len(snake_tails) > 0:
        x_head = snake_head.xcor()
        y_head = snake_head.ycor()

        snake_tails[0].setpos(x_head, y_head)

    if snake_head.xcor() > 290 or\
        snake_head.xcor() < -290 \
            or snake_head.ycor() > 250 or\
    snake_head.ycor() < -290:
        reset(snake_head, snake_tails)
        score = 0

    move_snake(snake_head)

    for tail in snake_tails:
        if tail.distance(snake_head) < 20:
            reset(snake_head, snake_tails)
            score = 0

    sleep(0.2)
