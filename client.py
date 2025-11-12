import socket
import json
import pygame
import threading
import sys
import os
HOST = '127.0.0.1'
PORT = 12345
WIDTH, HEIGHT = 800, 500
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oẳn Tù Tì")
clock = pygame.time.Clock()
