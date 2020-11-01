"""Modulo para analizar movimentos."""
import directionoptions


def analize_move(my_direction, snake_body):
    u"""Verifica a direção e movimenta a cobra na direção."""
    if my_direction == directionoptions.UP:
        snake_body[0] = (snake_body[0][0], snake_body[0][1] - 10)
    if my_direction == directionoptions.DOWN:
        snake_body[0] = (snake_body[0][0], snake_body[0][1] + 10)
    if my_direction == directionoptions.RIGHT:
        snake_body[0] = (snake_body[0][0] + 10, snake_body[0][1])
    if my_direction == directionoptions.LEFT:
        snake_body[0] = (snake_body[0][0] - 10, snake_body[0][1])
