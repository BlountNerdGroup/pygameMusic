import pygame
from pygame import *

pygame.init()
screen = pygame.display.set_mode([400, 400])


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

global number
number = 255

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                s = pygame.mixer.Sound("Bell2.wav")
                s.play()
                byte = s.get_raw()
                for i in byte:
                    if is_number(i):
                        number = int(i)

            screen.fill(number, 255, 255)
    pygame.display.update()