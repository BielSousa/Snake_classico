"""Mudulos para verificar eventos."""
import pygame as pg


def analize(event):
    """Verifica a saida."""
    if event.type == pg.QUIT:
        pg.quit()
        exit()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            pg.quit()
            exit()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
            return True
    return False
