import pygame
import random

from src.components.gameEntity import GameEntity

class SisingamangaradjaSumateraUtara(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/sisingamangaradja.png", x, y, scale=1)