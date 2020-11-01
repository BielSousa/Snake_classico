"""Modulo relativo a snake."""
from appleoptions import create


class Snake(object):
    """Classe snake."""

    def __init__(self):
        """Inicia o corpo da snake."""
        self.body = [(200, 200), (210, 200), (220, 200)]

    def eat_apple(self, snake, apple_pos, point):
        u"""Detecta se a cobra comeu a maca."""
        size_body_piece = (10, 10)
        if(
            (self.body[0][0] == apple_pos[0])and
            (self.body[0][1] == apple_pos[1])
        ):
            self.body.append(size_body_piece)
            return create(), point + 1
        return apple_pos, point
