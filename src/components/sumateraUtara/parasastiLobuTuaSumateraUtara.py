import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiLobuTuaSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/prasastiLobuTua.png", x, y, scale=1)