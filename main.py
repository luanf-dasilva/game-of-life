import pygame
import typer
import os

from typing import Tuple
from game_options import options_map, options_tuple
from conway import random_init, run_gol
from util import RGB, Integer, timer
__app_name__ = "CONWAY'S SIMPLE (AND FUNCTIONAL) GAME OF LIFE"
__version__ = "0.5.0"

class GOLInputs:
    n = Integer(minsize = 1, maxsize = 10000, input_name = "iterations")
    run_option = Integer(minsize = 0, maxsize = len(options_tuple._fields) + 1, input_name = "run_option")
    width = Integer(minsize = 180, maxsize = 1980, input_name = "iterations")
    height = Integer(minsize = 180, maxsize = 1980, input_name = "height")
    scale = Integer(minsize = 1, maxsize = 100, input_name = "scale")
    offset = Integer(minsize = 1, maxsize = 5, input_name = "offset")
    fps = Integer(minsize = 10, maxsize = 90, input_name = "fps")
    millisecs_between_secs = Integer(minsize = 0, maxsize = 1500, input_name = "millisecs_between_secs")
    active_color = RGB(input_name = "active_color")
    inactive_color = RGB(input_name = "inactive_color")

@timer
def run_gol_iterations(n, run_option, rows, columns, surface, scale, offset, millisecs_between_iters, active_color, inactive_color):
    for iteration in run_gol(initial_cond = run_option, n = n):
        for row in range(rows):
            for col in range(columns):
                if (row, col) in iteration:
                    pygame.draw.rect(surface, active_color, [col * scale, row * scale, scale - offset, scale - offset])
                else:
                    pygame.draw.rect(surface, inactive_color, [col * scale, row * scale, scale - offset, scale - offset])
        pygame.time.delay(millisecs_between_iters)
        pygame.display.update()

def parse_cli_args(
        n: int = typer.Option(200, help = "How many iterations to go through"), 
        run_option: int = typer.Option(0, help = "Which type of game of life to run. Starting at default 0: [random, options_tuple._field1, options_tuple._field2, ...]"),
        width: int = typer.Option(910, help = "Width of the screen"),
        height: int = typer.Option(540, help = "Height of the screen"),
        scale: int = typer.Option(5, help = "Scales how many total cells appear relative to width and height"),
        offset: int = typer.Option(1, help = "Thickness of borders"),
        fps: int = typer.Option(60, help = "Frames per second"),
        millisecs_between_iters:int = typer.Option(100, help = "How many milliseconds that passes between each iterations."),
        active_color: Tuple[int, int, int] = typer.Option((0, 14, 71), help = "RGB tuple for color of active cells. Default -> Blue"),
        inactive_color: Tuple[int, int, int] = typer.Option((255, 255, 255), help = "RGB tuple color of inactive cells. Default -> White")
        ):

        gol_input_validator = GOLInputs()
        gol_input_validator.n = n
        gol_input_validator.width = width
        gol_input_validator.height = height
        gol_input_validator.scale = scale
        gol_input_validator.offset = offset
        gol_input_validator.millisecs_between_secs = millisecs_between_iters
        gol_input_validator.active_color = active_color
        gol_input_validator.inactive_color = inactive_color

        run_set = options_map(run_option, width, height, scale)
        main(n, run_set, width, height, scale, offset, fps, millisecs_between_iters, active_color, inactive_color)

def main(n, initial_cond, width, height, scale,  offset, fps, millisecs_between_iters, active_color, inactive_color):
    run = True
    rows = int(height / scale)
    columns = int(width / scale)

    print("""\n%s cols
            \n%s rows
            \nRunning Conway's game for %s iterations""" 
            %(columns, rows, n))


    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    surface = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    clock.tick(fps)
    surface.fill((0,0,0))

    rows = int(height / scale)
    columns = int(width / scale)

    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not initial_cond:
            initial_cond = random_init(width, height, scale)

        run_gol_iterations(n, initial_cond, rows, columns, surface, scale, offset, millisecs_between_iters, active_color, inactive_color)
        print(f"{n} iterations")

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    typer.run(parse_cli_args)