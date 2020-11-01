u"""Modulo relativo as maçãs."""

from random import randint


def create():
    u"""Ajustar maçã a tela."""
    x = randint(0, 390)
    y = randint(0, 340)
    return (x//10 * 10, y//10 * 10)
