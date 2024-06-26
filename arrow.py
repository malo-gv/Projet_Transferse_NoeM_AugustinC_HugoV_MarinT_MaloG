import pygame
from constants import *
import math

def showArrow(window, arrowX, arrowY, arrowAngle):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrowAngle)
    arrowRectange = arrowImage.get_rect(center = (arrowX, arrowY))
    window.blit(arrowImage, arrowRectange.topleft)
    return arrowRectange

def moveArrow(arrowX, arrowY, shootForce, arrowAngle, timerShoot):
    time = timerShoot
    arrowX = arrowX + (shootForce * math.cos(math.radians(arrowAngle)) * time)
    arrowY = arrowY + 0.5 * gravity * (time ** 2) - ((shootForce * math.sin(math.radians(arrowAngle))) * time)
    return arrowX, arrowY

def calculateArrowAngle(mouseX, mouseY, arrowX, arrowY):
    dx = mouseX - arrowX
    dy = mouseY - arrowY
    angle = math.degrees(math.atan2(dy, dx))
    return -angle

def collisionCible(arrowX, arrowY, targetX, targetY):
    if (arrowX > targetX + 10 and arrowX < targetX + 90) and (arrowY > targetY + 20 and arrowY < targetY + 80):
        return True
    else:
        return False
def collisionCible2(arrowX, arrowY, arrowAngle, targetX, targetY, target):
    arrowImage = pygame.image.load("sprites character/arrow.png")
    arrowImage = pygame.transform.scale(arrowImage, (int(arrowImage.get_width() * 0.1), int(arrowImage.get_height() * 0.1)))
    arrowImage = pygame.transform.rotate(arrowImage, arrowAngle)
    arrowRectange = arrowImage.get_rect(center = (arrowX, arrowY))
    target = pygame.transform.scale(target , (int(target.get_width() * 0.6), int(target.get_height() * 0.6)))
    colisionZone = target.get_rect(topleft=(targetX + target.get_width()*0.2, targetY + target.get_height()*0.2))
    if arrowRectange.colliderect(colisionZone):
        return True
    else:
        return False

def drawTrajectory(window, arrowX, arrowY, shootForce, arrowAngle, steps=15):
    for step in range(steps):
        t = step / 10.0  # Échelonner le temps pour obtenir des points plus rapprochés
        arrowX  = arrowX + (shootForce * math.cos(math.radians(arrowAngle)) * t)
        arrowY  = arrowY + 0.5 * gravity * (t ** 2) - ((shootForce * math.sin(math.radians(arrowAngle))) * t)
        pygame.draw.circle(window, (0, 0, 0), (int(arrowX), int(arrowY)), 2)

def drawPowerGauge(window, shootDuration, maxForce):
    gauge_width = 200
    gauge_height = 20
    gauge_x = 20
    gauge_y = LENGTH - 40
    fill_width = min(gauge_width, int((shootDuration / (maxForce / 10)) * gauge_width))

    pygame.draw.rect(window, (255, 255, 255), (gauge_x, gauge_y, gauge_width, gauge_height), 2)
    pygame.draw.rect(window, (0, 255, 0), (gauge_x, gauge_y, fill_width, gauge_height))