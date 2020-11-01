u"""Modulo para direções."""
import pygame as pg

"""variaveis de direção"""
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
init = LEFT


def analize_directions(event, my_direction):
    u"""Verifica a tecla pressionada e muda a direção."""
    direction = my_direction

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            if direction != DOWN:
                direction = UP
        if event.key == pg.K_DOWN:
            if direction != UP:
                direction = DOWN
        if event.key == pg.K_LEFT:
            if direction != RIGHT:
                direction = LEFT
        if event.key == pg.K_RIGHT:
            if direction != LEFT:
                direction = RIGHT

    return direction
