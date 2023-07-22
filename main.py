import pygame as pg
from sys import exit
from settings import *
from jokes import *

class App():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.display.set_caption("Joke Generator")

        icon_surf = pg.image.load("icon.png")
        pg.display.set_icon(icon_surf)

        self.clock = pg.time.Clock()

    def check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

    def draw_screen(self):
        SCREEN.fill("#abfae3")
        normal_jokes.update()

    def update_screen(self):
        pg.display.update()
        self.clock.tick(FPS)

    def run(self):
        while True:
            self.check_for_events()
            self.draw_screen()
            self.update_screen()

app = App()
app.run()