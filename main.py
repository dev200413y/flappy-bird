import random
import sys
import pygame
from pygame.locals import *
import os

# Global variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    '''Show welcome images and wait for user to press a key to start the game'''
    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['bird'].get_height()) / 2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['bird'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    '''This function represents the main game loop where the game is played'''
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENHEIGHT / 2)
    basex = 0

    # Create two pipes for the game
    firstPipe = createPipe()
    if firstPipe is None:
        print("Error: Failed to create first pipe")
        pygame.quit()
        sys.exit()
    secondPipe = createPipe()
    if secondPipe is None:
        print("Error: Failed to create second pipe")
        pygame.quit()
        sys.exit()

    # List of upper and lower pipes
    upperPipes = [
        {'x': SCREENWIDTH + 300 - 150, 'y': firstPipe[0]['y']},
        {'x': SCREENWIDTH + 300 - 150 + (SCREENWIDTH / 2), 'y': secondPipe[0]['y']}
    ]
    lowerPipes = [
        {'x': SCREENWIDTH + 300 - 150, 'y': firstPipe[1]['y']},
        {'x': SCREENWIDTH + 300 - 150 + (SCREENWIDTH / 2), 'y': secondPipe[1]['y']}
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        # Check for game over
        if isGameOver(playerx, playery, upperPipes, lowerPipes):
            return

        # Check for score
        playerMidPos = playerx + GAME_SPRITES['bird'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

        # Apply gravity
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['bird'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # Move pipes
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Remove off-screen pipes and add new ones
        if upperPipes and upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
            newPipe = getRandomPipe()
            if newPipe is None:
                print("Error: Failed to create new pipe")
                pygame.quit()
                sys.exit()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # Blit sprites
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['bird'], (playerx, playery))

        # Display score
        myDigit = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigit:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width) / 2
        for num in myDigit:
            SCREEN.blit(GAME_SPRITES['numbers'][num], (Xoffset, SCREENHEIGHT * 0.02))
            Xoffset += GAME_SPRITES['numbers'][num].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isGameOver(playerx, playery, upperPipes, lowerPipes):
    '''Check if the player has collided with pipes or ground'''
    playerWidth = GAME_SPRITES['bird'].get_width()
    playerHeight = GAME_SPRITES['bird'].get_height()
    
    # Check ground or ceiling collision
    if playery + playerHeight > GROUNDY or playery < 0:
        GAME_SOUNDS['hit'].play()
        return True
    
    # Check pipe collision
    for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
        pipeWidth = GAME_SPRITES['pipe'][0].get_width()
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        
        # Check collision with upper pipe
        if (playerx + playerWidth > upperPipe['x'] and playerx < upperPipe['x'] + pipeWidth and
            (playery < upperPipe['y'] + pipeHeight)):
            GAME_SOUNDS['hit'].play()
            return True
        
        # Check collision with lower pipe
        if (playerx + playerWidth > lowerPipe['x'] and playerx < lowerPipe['x'] + pipeWidth and
            (playery + playerHeight > lowerPipe['y'])):
            GAME_SOUNDS['hit'].play()
            return True
    
    return False

def getRandomPipe():
    '''Generates positions of two pipes (one bottom and one top rotated) for blitting on the screen'''
    try:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        baseHeight = GAME_SPRITES['base'].get_height()
        offset = SCREENHEIGHT / 3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - baseHeight - 1.2 * offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1},  # Upper pipe
            {'x': pipeX, 'y': y2}    # Lower pipe
        ]
        return pipe
    except Exception as e:
        print(f"Error in getRandomPipe: {e}")
        return None

def createPipe():
    '''This function generates a pair of pipes for the game'''
    return getRandomPipe()

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')

    # Initialize sprites and sounds with error handling
    try:
        GAME_SPRITES['numbers'] = (
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha()
        )
        GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
        GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
        GAME_SPRITES['bird'] = pygame.image.load(PLAYER).convert_alpha()
        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['pipe'] = (
            pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
            pygame.image.load(PIPE).convert_alpha()
        )

        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    except pygame.error as e:
        print(f"Error loading assets: {e}")
        pygame.quit()
        sys.exit()

    # Verify critical sprites are loaded
    if 'pipe' not in GAME_SPRITES or 'base' not in GAME_SPRITES:
        print("Error: Failed to load pipe or base sprites")
        pygame.quit()
        sys.exit()

    while True:
        welcomeScreen()
        mainGame()