import random
import time
import pygame
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 448
SCREEN_HEIGHT = 384

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
title = pygame.display.set_caption("ConnectFour")

background = pygame.image.load("attached\\background.png")
computer = pygame.image.load("attached\\computer.png")
player = pygame.image.load("attached\\player.png")
computernew = pygame.image.load("attached\\computernew.png")
playernew = pygame.image.load("attached\\playernew.png")
computersucc = pygame.image.load("attached\\computersucc.png")
playersucc = pygame.image.load("attached\\playersucc.png")
start = pygame.image.load("attached\\start.png")

grids = [[0 for i in range(7)] for i in range(6)]
NotEnd = True
update = True
Start = False
Notclick = True
playerprevious = None
computerprevious = None


def drop(grids, column, target):
    if grids[0][column] != 0:
        return None
    else:
        for i in range(1, 6):
            if(grids[i][column] != 0):
                grids[i-1][column] = target
                return [i-1, column]
        grids[5][column] = target
        return [5, column]


def convertcosys(cor_init):
    if cor_init != None:
        return (cor_init[1]*64, cor_init[0]*64)


def tie(grids):
    for j in range(0, 7):
        if(grids[0][j] == 0):
            return False
    for i in range(0, 6):
        for j in range(0, 7):
            if(grids[i][j] == 1):
                screen.blit(playersucc, convertcosys([i, j]))
            if(grids[i][j] == 2):
                screen.blit(computersucc, convertcosys([i, j]))
    return True


def judgefour(grids, target, sub):
    for i in range(0, 3):
        for j in range(0, 7):
            if(grids[i][j] == target):
                if(grids[i + 1][j] == target and grids[i + 2][j] == target and grids[i + 3][j] == target):
                    if(sub != None):
                        screen.blit(sub, convertcosys([i, j]))
                        screen.blit(sub, convertcosys([i + 1, j]))
                        screen.blit(sub, convertcosys([i + 2, j]))
                        screen.blit(sub, convertcosys([i + 3, j]))
                    return True
    for j in range(0, 4):
        for i in range(0, 6):
            if(grids[i][j] == target):
                if(grids[i][j + 1] == target and grids[i][j + 2] == target and grids[i][j + 3] == target):
                    if(sub != None):
                        screen.blit(sub, convertcosys([i, j]))
                        screen.blit(sub, convertcosys([i, j + 1]))
                        screen.blit(sub, convertcosys([i, j + 2]))
                        screen.blit(sub, convertcosys([i, j + 3]))
                    return True
                if i in range(0, 3):
                    if(grids[i + 1][j + 1] == target and grids[i + 2][j + 2] == target and grids[i + 3][j + 3] == target):
                        if(sub != None):
                            screen.blit(sub, convertcosys([i, j]))
                            screen.blit(sub, convertcosys([i + 1, j + 1]))
                            screen.blit(sub, convertcosys([i + 2, j + 2]))
                            screen.blit(sub, convertcosys([i + 3, j + 3]))
                        return True
                if i in range(3, 6):
                    if(grids[i - 1][j + 1] == target and grids[i - 2][j + 2] == target and grids[i - 3][j + 3] == target):
                        if(sub != None):
                            screen.blit(sub, convertcosys([i, j]))
                            screen.blit(sub, convertcosys([i - 1, j + 1]))
                            screen.blit(sub, convertcosys([i - 2, j + 2]))
                            screen.blit(sub, convertcosys([i - 3, j + 3]))
                        return True
    return False


def randomAI(grids):
    possible = []
    for i in range(0, 7):
        if(grids[0][i] == 0):
            possible.append(i)
    possiblecopy = possible
    for i in possible:
        answerr = drop(grids, i, 2)
        nextr = drop(grids, i, 1)
        if judgefour(grids, 1, None):
            possible.remove(i)
        grids[answerr[0]][i] = 0
        if nextr != None:
            grids[nextr[0]][i] = 0
    if possible != []:
        ram = random.randint(0, len(possible) - 1)
        return possible[ram]
    else:
        if len(possiblecopy) != 1:
            ram = random.randint(0, len(possiblecopy) - 1)
            return possiblecopy[ram]
        else:
            return possiblecopy[0]


def predict(grids):
    for j in range(0, 7):
        answer = drop(grids, j, 2)
        if answer != None:
            if judgefour(grids, 2, None):
                grids[answer[0]][j] = 0
                return j
            grids[answer[0]][j] = 0
    for j in range(0, 7):
        answer = drop(grids, j, 1)
        if answer != None:
            if judgefour(grids, 1, None):
                grids[answer[0]][j] = 0
                return j
            grids[answer[0]][j] = 0
    return randomAI(grids)


def computerAI(grids):
    return convertcosys(drop(grids, predict(grids), 2))


screen.blit(start, (0, 0))
pygame.display.flip()
while Notclick:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                Start = True
                Notclick = False

while Start:
    grids = [[0 for i in range(7)] for i in range(6)]
    if update == True:
        screen.blit(background, (0, 0))
        pygame.display.flip()
    state = 0
    ticks = None
    while NotEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and state == 0:
                if event.key == K_1:
                    result = drop(grids, 0, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_2:
                    result = drop(grids, 1, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_3:
                    result = drop(grids, 2, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_4:
                    result = drop(grids, 3, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_5:
                    result = drop(grids, 4, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_6:
                    result = drop(grids, 5, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
                if event.key == K_7:
                    result = drop(grids, 6, 1)
                    if result != None:
                        state = 1
                        ticks = pygame.time.get_ticks()
        if state == 1 and ticks and pygame.time.get_ticks() > ticks + 1000:
            state = 2
        if state > 0:
            screen.blit(playernew, convertcosys(result))
            if playerprevious != None:
                screen.blit(player, playerprevious)
            pygame.display.flip()
            if judgefour(grids, 1, playersucc):
                pygame.display.flip()
                break
        if state > 1:
            playerprevious = convertcosys(result)
            temp = computerAI(grids)
            screen.blit(computernew, temp)
            if computerprevious != None:
                screen.blit(computer, computerprevious)
            computerprevious = temp
            pygame.display.flip()
            if judgefour(grids, 2, computersucc):
                pygame.display.flip()
                break
            if tie(grids):
                pygame.display.flip()
                break
            state = 0
            ticks = None
    NotEnd = False
    update = False
    playerprevious = None
    computerprevious = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                NotEnd = True
                update = True
