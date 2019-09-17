"""
This program works as lockscreen, except that it will play
a song (e.g. Barbie by Aqua) upon user input. It will generate
a training log for a ANN to hide its initial stdout.

Usage:
  - Install pygame
  - Run program
  - Arm it by pressing 'a'
  - Wait for your victim
  - Disarm it by pressing 'a'
"""
import pygame
import random
import threading
import time


SONG_PATH = 'barbie.ogg'
active = False
started = False
color = (255, 255, 255)


pygame.init()
screen = pygame.display.set_mode((1, 1))
pygame.mouse.set_visible(0)


def play_song(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    

def create_prank():
    """
    Do required setup and start prank
    """
    threading.Thread(target=play_song, args=(SONG_PATH,)).start()
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def get_color():
    """
    Generate a random color
    """
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


for i in range(78):
    print(f'EPOCH {i} val acc {27.32+i/2-i/15-i/7:.2f}% loss {4.32 - i/21:.2f}')


while True:
    events = pygame.event.get()
    for event in events:
        
        # Activate that shit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if active:
                    exit()
                active = True
                break

        # Ignore key up otherwise triggers directly
        # on activation
        if active and not started and event.type != pygame.KEYUP:
            screen = create_prank()
            started = True
         
    color = get_color()
    screen.fill(color)

    pygame.display.update()
    time.sleep(0.1)
    
pygame.quit()
