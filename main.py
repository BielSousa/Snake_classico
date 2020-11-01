"""Meu primeiro jogo pygame."""
import pygame as pg
from colors import cores
from collision import collision_check
from move import analize_move
from directionoptions import init, analize_directions
from snake import Snake
import appleoptions
import points
import events
import screenoptions

# inicializados do pygame
pg.init()


class Game(object):
    """Classe que cria o jogo."""

    def game_over_screen(self):
        u"""Tela de game over."""
        init_game = False

        while not init_game:
            for event in pg.event.get():
                init_game = events.analize(event)

            if init_game:
                self.init_game()

            pg.display.set_caption('Snake')
            screen = pg.display.set_mode(screenoptions.size_screen)
            game_over_font = pg.font.Font('freesansbold.ttf', 30)
            continue_font = pg.font.Font('freesansbold.ttf', 15)
            game_over_screen = game_over_font.render(
                                "Game Over",
                                True, cores['white']
                                            )
            continue_screen = continue_font.render(
                                "Pressione Enter para continuar",
                                True, cores['white']
                                            )
            screen.blit(game_over_screen, (120, 180))
            screen.blit(continue_screen, (90, 220))
            pg.display.update()

    # Loop do jogo
    def init_game(self):
        u"""Tela principal do jogo."""
        # inicializando tela e itens do game
        pg.display.set_caption('Snake')
        screen = pg.display.set_mode(screenoptions.size_screen)
        screen_game = pg.Surface(screenoptions.size_screen_game)
        screen_point = pg.Surface(screenoptions.size_screen_point)
        snake = Snake()
        snake_skin = pg.Surface(screenoptions.size_itens)
        apple = pg.Surface(screenoptions.size_itens)

        # Definindo cores
        screen.fill(cores['blue'])
        screen_point.fill(cores['grey-light'])
        snake_skin.fill(cores['green'])
        apple.fill(cores['red'])

        # Set do clock
        clock = pg.time.Clock()

        # Definindo variaveis do jogo
        direction = init
        game_over = False
        apple_pos = appleoptions.create()

        # Loop principal do jogo
        while not game_over:
            clock.tick(15)

            for event in pg.event.get():
                events.analize(event)
                direction = analize_directions(event, direction)

            apple_pos, points.point = snake.eat_apple(snake.body,
                                                      apple_pos, points.point)
            game_over = collision_check(snake.body, screenoptions.width,
                                        screenoptions.height)

            if game_over:
                if points.point > points.record:
                    points.record = points.point
                points.point = 0
                self.game_over_screen()

            for i in range(len(snake.body) - 1, 0, -1):
                snake.body[i] = (snake.body[i-1][0], snake.body[i-1][1])

            analize_move(direction, snake.body)

            txttela = points.point_font.render(
                                        ("Pontuação: " + str(points.point) +
                                         "       " +
                                         'record: ' + str(points.record)),
                                        1, cores['black'])

            screen.blit(screen_point, (0, 0))
            screen.blit(txttela, (50, 20))
            screen.blit(screen_game, (0, 50))
            screen_game.fill(cores['black'])
            screen_game.blit(apple, apple_pos)

            for pos in snake.body:
                screen_game.blit(snake_skin, pos)

            pg.display.update()


game = Game()
game.init_game()
