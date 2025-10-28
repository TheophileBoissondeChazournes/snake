from pyray import *

SIDE = 40
WIDTH = 20
HEIGHT = 10

snake = [[1,1],[2,1],[3,1]]
init_window(800, 450, "Mon jeu")
set_target_fps(10)

#while not window_should_close():
   # begin_drawing()
    #clear_background(RAYWHITE)
    #draw_text("Hello Raylib", 190, 200, 20, LIGHTGRAY)
    #draw_circle(400, 225, 50, RED)
   # end_drawing()

#close_window()


while not window_should_close():
    begin_drawing()
    clear_background(BLACK)

    #ANIMATION

    vitesse=[1,0]
    vx,vy =vitesse
    hx, hy = snake[-1]
    new_head = [hx+vx, hy+vy]
    snake = snake[1:]+[new_head]

    #DESSEIN

    for i,(x,y) in enumerate(snake):
        color = GREEN if i == len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE+1,SIDE+1,SIDE-2,SIDE-2,color)
    is_key_up
    end_drawing()
    
close_window()
