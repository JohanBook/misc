"""
This program works as lockscreen, except that it will play
a song (e.g. Barbie by Aqua) upon user input. It will generate
a training log for a ANN to hide its initial stdout.

NB: I have no clue how to turn it of when triggered.

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

# Set this path to the song to be played
# It should be in ogg-format
SONG_PATH = 'barbie.ogg'


active = False
started = False
color = (255, 255, 255)


def play_song(path):
    """
    Play a song. Duh.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    
def create_prank():
    """
    Start a thread playing specified song and create a pygame display
    that occupies whole screen.
    """
    threading.Thread(target=play_song, args=(SONG_PATH,)).start()
    return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def get_color():
    """
    Generate a random color.
    """
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1, 1))
    pygame.mouse.set_visible(0)

    # Generate some fake logs
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
