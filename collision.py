u"""Modulo de para detectar colisões."""


def collision_check(snake_body, width, height):
    u"""Detecta colisões."""
    if(
        (snake_body[0][0] == width)or(snake_body[0][0] == -10)or
        (snake_body[0][1] == height - 50)or(snake_body[0][1] == -10)
    ):
        return True
    for i in range(1, len(snake_body) - 1):
        if(
            (snake_body[0][0] == snake_body[i][0])and
            (snake_body[0][1] == snake_body[i][1])
        ):
            return True
    return False
