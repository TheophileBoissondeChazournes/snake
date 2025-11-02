from pyray import *
from raylib import *
import random

SIDE = 40
WIDTH = 20
HEIGHT = 10

def nouvelle_partie():
    vitesse=[1,0]
    fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
    super_fruit = None
    super_timer = 0
    snake = [[1,1],[2,1],[3,1]]
    perdu = False
    frame = -1
    score = 0
    speed = 10
    return vitesse, fruit, super_fruit, super_timer, snake, perdu, frame, score, speed

init_window(WIDTH * SIDE, HEIGHT * SIDE, "Jeu du Serpent")
set_target_fps(60)

vitesse, fruit, super_fruit, super_timer, snake, perdu, frame, score, speed = nouvelle_partie()

while not window_should_close():
    frame+=1
    begin_drawing()
    clear_background(BLACK)

#DESSIN DES CASES
    for x in range(WIDTH + 1):
        draw_line(x * SIDE, 0, x * SIDE, HEIGHT * SIDE, DARKGRAY)
    for y in range(HEIGHT + 1):
        draw_line(0, y * SIDE, WIDTH * SIDE, y * SIDE, DARKGRAY)

#GESTION DES TOUCHES
    if not perdu:
        if is_key_pressed(KEY_LEFT) and vitesse != [1, 0]:
            vitesse = [-1, 0]
        elif is_key_pressed(KEY_RIGHT) and vitesse != [-1, 0]:
            vitesse = [1, 0]
        elif is_key_pressed(KEY_DOWN) and vitesse != [0, -1]:
            vitesse = [0, 1]
        elif is_key_pressed(KEY_UP) and vitesse != [0, 1]:
            vitesse = [0, -1]

#VITESSE
    speed = max(3, 10 - score // 10)

#ANIMATION
    if not perdu and frame%speed == 0:
        vx,vy = vitesse
        hx, hy = snake[-1]
        new_head = [hx+vx, hy+vy]

# JEU CIRCULAIRE
        new_head[0] %= WIDTH
        new_head[1] %= HEIGHT


#TRANSFORMATION DU SERPENT
        if new_head in snake:
            perdu = True

        if new_head == fruit:
            snake.append(new_head)
            score += 1
            fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]

        elif super_fruit and new_head == super_fruit:
            snake.append(new_head)
            score += 5
            super_fruit = None
            super_timer = 0

        else:
            snake = snake[1:] + [new_head]

#APPARITION SUPER FRUIT
    if not perdu and super_fruit is None and random.randint(0, 2000) < 3: 
        super_fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
        super_timer = 300

#TIMER SUPER FRUIT
    if super_fruit:
        super_timer -= 1
        if super_timer <= 0:
            super_fruit = None

#DESSIN
    draw_circle(fruit[0]* SIDE + SIDE // 2 , fruit[1]* SIDE + SIDE // 2 , SIDE // 2, RED)

    if super_fruit:
        draw_circle(super_fruit[0] * SIDE + SIDE // 2, super_fruit[1] * SIDE + SIDE // 2, SIDE // 2 - 6, YELLOW)

    for i,(x,y) in enumerate(snake):
        color = GREEN if i == len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,color)
    
# Score
    draw_text(f"Score : {score}", 10, 10, 20, RAYWHITE)   

# ECRAN DE FIN DE PARTIE
    if perdu:
        draw_text("PERDU !", WIDTH * SIDE // 2 - 60, HEIGHT * SIDE // 2 - 30, 40, RAYWHITE)
        draw_text("Appuyez sur [ENTRÉE] pour rejouer", WIDTH * SIDE // 2 - 160, HEIGHT * SIDE // 2 + 20, 20, RAYWHITE)

        # Si le joueur appuie sur Entrée → relance la partie
        if is_key_pressed(KEY_ENTER):
            vitesse, fruit, super_fruit, super_timer, snake, perdu, frame, score, speed = nouvelle_partie()


    end_drawing()

close_window()

