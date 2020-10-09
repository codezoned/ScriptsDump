import pygame
from random import randrange
import time

pygame.init()

# Different colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)


# size of the screen
width = height = 500
# set the height and width of the screen
screen = pygame.display.set_mode((width, height))
# Name on the top of the window
pygame.display.set_caption('Snake Game')
# Load the icon for the openning window
icon = pygame.image.load('assets/images/icon/snake.jpg')
pygame.display.set_icon(icon)


scoreboard = 40

def snake(snk_xy, size):
    for xy in snk_xy:
        pygame.draw.rect(screen, green, (xy[0], xy[1], size, size))

# 
def apple(apl_x, apl_y, size):
    pygame.draw.rect(screen, red, (apl_x, apl_y, size, size))


def text(txt_msg, txt_clr, txt_x, txt_y, txt_size,):
    font = pygame.font.SysFont('serif', txt_size)
    txt = font.render(txt_msg, True, txt_clr)
    screen.blit(txt, (txt_x, txt_y))


# Music play while in game
pygame.mixer_music.load('assets/sounds/game_music_2.wav')
# pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.2)

# adding the sound effect and set the volume
snake_bite = pygame.mixer.Sound('assets/sounds/sound_effects/got_apple.wav')
pygame.mixer.Sound.set_volume(snake_bite, 0.5)

game_over_sound = pygame.mixer.Sound('assets/sounds/sound_effects/game_over.wav')
pygame.mixer.Sound.set_volume(game_over_sound, 0.5)


def game():
    game_close = True
    game_over = False
    # keep track of time
    clock = pygame.time.Clock()
    score = 0

    # initial position of the snake
    snk_x, snk_y = int(width / 2), int(height / 2)

    # stores the coordinates of the blocks in the snake
    snk_xy = []
    # snake length
    snk_scale = 0
    # size of the block
    size = 10

    # speed in x an y direction of the snake
    spd_x = spd_y = 0

    # initial position of the apple
    apl_x = randrange(0, width - size, size)
    apl_y = randrange(0, height - size - scoreboard, size)

    pygame.mixer.music.play(-1)

    t1 = time.time()
    measured_time = 0

    while game_close:
        # slow the runtime speed of the game by 5 milliseconds
        clock.tick(7)
        # fill the complete screen with black
        screen.fill(black)

        # draw the scorecard in the bottom
        pygame.draw.rect(screen, blue, (0, height - scoreboard, width, scoreboard))
        # text on the scorecard
        t2 = time.time()
        measured_time = t2-t1
        text('Score: ' + str(score), white, 10, width - scoreboard, 20)
        text('Time Elapsed: ' + str(round(measured_time,2))+' s', white, 300, width - scoreboard, 20)

        # snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = False
                game_over_sound.play()
                pygame.mixer.music.stop()

            # Key press events
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP and spd_y != size:
                    spd_x = 0
                    spd_y = - size
                if event.key == pygame.K_DOWN and spd_y != -size:
                    spd_x = 0
                    spd_y = size
                if event.key == pygame.K_RIGHT and spd_x != -size:
                    spd_y = 0
                    spd_x = size
                if event.key == pygame.K_LEFT and spd_x != size:
                    spd_y = 0
                    spd_x = - size

        # size of the snake
        snk_x += spd_x
        snk_y += spd_y

        # check for wall collision
        if snk_x >= height or snk_x < 0 or snk_y >= (width - scoreboard) or snk_y < 0:
            game_over = True
            pygame.mixer.music.stop()
            game_over_sound.play()


        # if the snake has reached the apple location
        if snk_x == apl_x and snk_y == apl_y:
            apl_x = randrange(0, width - size, size)
            apl_y = randrange(0, height - size - scoreboard, size)
            # play the sound
            snake_bite.play()
            snk_scale += 1
            score += 1

        # store the coordinates of the current snake location
        if len(snk_xy) > snk_scale:
            del snk_xy[0]
        snk_head = [snk_x, snk_y]
        snk_xy.append(snk_head)
        # print(snk_xy)

        # snake eating himself
        if any(bloc == snk_head for bloc in snk_xy[: -1]):
            game_over = True
            pygame.mixer.music.stop()
            game_over_sound.play()

        # draw the snake and the apple 
        snake(snk_xy, size)
        apple(apl_x, apl_y, size)
        
        # Update portions of the screen for software displays
        pygame.display.update()

        # When the user collides and the snake dies
        while game_over:

            screen.fill(black)

            # Rect parameter ( Xloc, Yloc, width,height)
            pygame.draw.rect(screen, green, (100, 180, 125, 25))
            pygame.draw.rect(screen, red, (280, 180, 120, 25))
            pygame.draw.rect(screen, blue, (0, height - scoreboard, width, scoreboard))

            # Put the text in the screen
            text('Game Over', blue, 170, 100, 30)
            text('[Y] New Game', white, 100, 180, 20)
            text('[N] End Game', white, 280, 180, 20)
            
            text('Score: ' + str(score), white, 10, width - scoreboard, 20)
            text('Time Elapsed: ' + str(round(measured_time,2))+' s', white, 300, width - scoreboard, 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_close = False
                    pygame.mixer.music.stop()
                    game_over_sound.play()

                'CONTROLS/MOUSE'
                if event.type == pygame.KEYDOWN:
                    # New game ie Y letter is pressed in keyboard 
                    if event.key == pygame.K_y:
                        return game()
                    # End game ie N letter is pressed in keyboard 
                    elif event.key == pygame.K_n:
                        game_over = False
                        game_close = False
                        pygame.mixer.music.stop()
                        game_over_sound.play()

                # Mouse click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = pygame.mouse.get_pos()[0]
                    mouse_y = pygame.mouse.get_pos()[1]
                    # if New game is clicked
                    if 100 < mouse_x < 220 and 180< mouse_y < 205 :
                        return game()
                    # if End game is clicked
                    if 280 < mouse_x < 400 and 180 < mouse_y < 205:
                        game_over = False
                        game_close = False
                        pygame.mixer.music.stop()
                        game_over_sound.play()

            # update the display
            pygame.display.update()


game()

pygame.quit()