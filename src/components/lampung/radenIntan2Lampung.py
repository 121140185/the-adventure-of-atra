import pygame
import random

from src.components.interactableItem import InteractableItem

class RadenIntan2Lampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/radenIntan2.png", x, y, scale=1)