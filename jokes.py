import pygame as pg
import requests
from settings import *

class NormalJokes():
    def __init__(self):
        pg.font.init()

        self.categories = ["Any", "Misc", "Programming", "Dark", "Pun", "Spooky"]
        self.categorie_index = 0

        self.any_button = pg.image.load("button_images/button_0.png").convert_alpha()
        self.misc_button = pg.image.load("button_images/button_1.png").convert_alpha()
        self.programming_button = pg.image.load("button_images/button_2.png").convert_alpha()
        self.dark_button = pg.image.load("button_images/button_3.png").convert_alpha()
        self.pun_button = pg.image.load("button_images/button_4.png").convert_alpha()
        self.spooky_button = pg.image.load("button_images/button_5.png").convert_alpha()

        self.any_rect = self.any_button.get_rect(center = (100, 315))
        self.misc_rect = self.misc_button.get_rect(center = (400, 315))
        self.programming_rect = self.programming_button.get_rect(center = (700, 315))
        self.dark_rect = self.dark_button.get_rect(center = (100, 435))
        self.pun_rect = self.pun_button.get_rect(center = (400, 435))
        self.spooky_rect = self.spooky_button.get_rect(center = (700, 435))

        self.mouse_clicked = False

        self.font = pg.font.SysFont("Arial", 30)
        self.setup_surf = self.font.render("", False, "white")
        self.delivery_surf = self.font.render("", False, "white")

    def change_text(self, setup: str, delivery: str):
        self.setup_surf = self.font.render(setup, False, "white")
        self.delivery_surf = self.font.render(delivery, False, "white")

    def draw_text(self):
        SCREEN.blit(self.setup_surf, (50,50))
        SCREEN.blit(self.delivery_surf, (50,150))

    def make_request(self):
        api_url = f"https://v2.jokeapi.dev/joke/{self.categories[self.categorie_index]}"
        response = requests.get(api_url)
        data = response.json()
        joke_setup = data['setup']
        joke_delivery = data['delivery']
        self.change_text(joke_setup, joke_delivery)

    def draw_buttons(self):
        SCREEN.blit(self.misc_button, self.misc_rect)
        SCREEN.blit(self.any_button, self.any_rect)
        SCREEN.blit(self.pun_button, self.pun_rect)
        SCREEN.blit(self.programming_button, self.programming_rect)
        SCREEN.blit(self.dark_button, self.dark_rect)
        SCREEN.blit(self.spooky_button, self.spooky_rect)

    def check_for_click(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.any_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 0
                self.make_request()

        if self.misc_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 1
                self.make_request()

        if self.programming_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 2
                self.make_request()

        if self.dark_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 3
                self.make_request()

        if self.pun_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 4
                self.make_request()

        if self.spooky_rect.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and self.mouse_clicked == False:
                self.mouse_clicked = True
                self.categorie_index = 5
                self.make_request()

        self.reset_click()
    
    def reset_click(self):
        if pg.mouse.get_pressed()[0] == False:
            self.mouse_clicked = False

    def update(self):
        self.draw_buttons()
        self.check_for_click()
        self.draw_text()

normal_jokes = NormalJokes()