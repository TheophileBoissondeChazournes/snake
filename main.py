from pyray import *
from raylib import *
import random

SIDE = 40
WIDTH = 20
HEIGHT = 10

vitesse=[1,0]
fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
snake = [[1,1],[2,1],[3,1]]
perdu = False
frame=-1

init_window(800, 450, "Jeu du Serpent")
set_target_fps(60)


while not window_should_close() and not perdu:
    frame+=1
    begin_drawing()
    clear_background(BLACK)

#GESTION DES TOUCHES

    if is_key_pressed(KEY_LEFT) and vitesse != [1, 0]:
        vitesse = [-1, 0]
    elif is_key_pressed(KEY_RIGHT) and vitesse != [-1, 0]:
        vitesse = [1, 0]
    elif is_key_pressed(KEY_DOWN) and vitesse != [0, -1]:
        vitesse = [0, 1]
    elif is_key_pressed(KEY_UP) and vitesse != [0, 1]:
        vitesse = [0, -1]

#ANIMATION

    if frame%10==0:
        vx,vy = vitesse
        hx, hy = snake[-1]
        new_head = [hx+vx, hy+vy]

        if new_head == fruit:
            snake.append(new_head)
            fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
        else:
            snake = snake[1:] + [new_head]


#DESSIN

    draw_rectangle(fruit[0] * SIDE, fruit[1] * SIDE, SIDE, SIDE, RED)

    for i,(x,y) in enumerate(snake):
        color = GREEN if i == len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,color)
    
    

#CONDITION DE FIN DE PARTIE

    if new_head[0]>WIDTH or new_head[0]<0 or new_head in snake[:-1]:
        perdu = True
    if new_head[1]>HEIGHT or new_head[1]<0:
        perdu = True

    if perdu:
        draw_text("PERDU !", WIDTH * SIDE // 2 - 60, HEIGHT * SIDE // 2 - 10, 30, RAYWHITE)

    end_drawing()



