from pygame.locals import *
from arrow import *
from constants import *
from target import *

currentTime = pygame.time.get_ticks() / 1000
print(currentTime)
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, LENGTH))

# fond
background = pygame.image.load("Images background/background v1.jpg").convert()

# archer
character = pygame.image.load("sprites character/archer.png")
character = pygame.transform.scale(character, (int(character.get_width() * 0.25), int(character.get_height() * 0.25)))
character = pygame.transform.flip(character, True, False)

target = pygame.image.load("sprites character/bullseye.png")
target = pygame.transform.scale(target, (int(target.get_width() * 0.20), int(target.get_height() * 0.20)))

keys = pygame.key.get_pressed()

running = True
arrowMoving = False
JAD = False
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION and arrowMoving == False and colisionActive == False:
            mouseX, mouseY = pygame.mouse.get_pos()  # Pour obtenir les coord de la souris
            arrowAngle = calculateArrowAngle(mouseX, mouseY, arrowX, arrowY)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shootStartTime = pygame.time.get_ticks()
        if event.type == KEYUP:
            if event.key == K_j:
                JAD = True
            if event.key == K_SPACE and arrowMoving is False:
                shootEndTime = pygame.time.get_ticks()
                shootDuration = (shootEndTime - shootStartTime) / 1000.0
                shootForce = min(maxForce, shootDuration * 10)
                initialArrowX = arrowX
                initialArrowY = arrowY
                arrowMoving = True
                startTime = pygame.time.get_ticks() / 1000
                shootStartTime = None

    if not arrowMoving and not colisionActive:
        mouseX, mouseY = pygame.mouse.get_pos()
        arrowAngle = calculateArrowAngle(mouseX, mouseY, arrowX, arrowY)

    if arrowMoving:
        previousArrowX, previousArrowY = arrowX, arrowY
        currentTime = pygame.time.get_ticks() / 1000
        timerShoot = currentTime - startTime
        print(timerShoot)
        arrowX, arrowY = moveArrow(arrowX, arrowY, shootForce, arrowAngle, timerShoot)

        arrowTilt = calculateArrowAngle(arrowX, arrowY, previousArrowX, previousArrowY)

        if collisionCible(arrowX,arrowY, targetX, targetY):
            pygame.time.wait(750)
            arrowMoving = False
            colisionActive = True

    if arrowMoving is False and colisionActive:
        pygame.time.wait(2000)
        score = score + 1
        colisionActive = False
        arrowX = baseX
        arrowY = baseY
        targetX, targetY = bougerCible()
        arMissed = 0

    if arrowY > 570:
        pygame.time.wait(750)
        arrowX = baseX
        arrowY = baseY
        arrowMoving = False
        arMissed = arMissed + 1

    if (arrowX > WIDTH or arrowY > LENGTH):
        arrowX = baseX
        arrowY = baseY
        arrowMoving = False
        arMissed = arMissed + 1

    if arMissed >= 5 :
        finished = True


    window.blit(background, (0, 20))
    window.blit(character, (75, baseGround))
    window.blit(target, (targetX, targetY))
    font = pygame.font.SysFont("comicsans", 30, True)
    textScore = font.render("Dans le mille ! : " + str(score), 1, (255, 255, 255))
    textMiss = font.render("Tirs ratés : " + str(arMissed), 1, (255, 255, 255))
    textGameOver = font.render("5 tirs ratés = GAME OVER", 1, (200, 30, 30))
    window.blit(textScore, (55, 30))
    window.blit(textMiss, (55, 70))
    window.blit(textGameOver, (660, 20))

    if JAD == True :
        imageJAD = pygame.image.load("sprites character/jad.png")
        imageJAD = pygame.transform.scale(imageJAD,(int(character.get_width() * 0.4), int(character.get_height() * 0.4)))
        imageJAD = pygame.transform.flip(imageJAD, True, False)
        window.blit(imageJAD, (116, 448))

    if finished:
        gameOver = pygame.image.load("sprites character/game-over.png")
        gameOver = pygame.transform.scale(gameOver, (int(gameOver.get_width() * 0.65), int(gameOver.get_height() * 0.65)))
        window.blit(gameOver, (380, 200))

    if not arrowMoving and shootStartTime:
        currentShootDuration = (pygame.time.get_ticks() - shootStartTime) / 1000.0
        drawPowerGauge(window, currentShootDuration, maxForceDraw)
        drawTrajectory(window, initialArrowX, initialArrowY, min(maxForceDraw, currentShootDuration * 10), arrowAngle)

    if arrowMoving:
        showArrow(window, arrowX, arrowY, arrowTilt)

    if not arrowMoving:
        showArrow(window, arrowX, arrowY, arrowAngle)

    pygame.display.update()
    clock.tick(60)

    if finished:
        pygame.time.wait(2000)
        pygame.quit()
pygame.quit()