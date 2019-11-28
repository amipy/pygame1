import pygame
import time
import random
pygame.init()
pygame.display.set_caption('Race!')
width = 1000
height = 900
white=(255,255,255)
black=(0,0,0)
disp = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
disp.fill(white)
carImg = pygame.image.load('raceCar.png')
disp.blit(carImg, ((width/2)-50,height-200))
pygame.display.update()
carPos=int((width/2)-50)
mover=0
obsPos=[]
score=0
speed=7
speedc=0
def moveCar(direction):
    global carPos
    global width
    #-1 is left and 1 is right
    disp.blit(carImg, (carPos+direction,height-200))
    carPos=carPos+direction
    if carPos<0:
        disp.blit(carImg, (0,height-200))
    if carPos+100>width:
        disp.blit(carImg, (width-100,height-200))
on=True
def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    disp.blit(TextSurf, TextRect)
def displayText(text, x, y, size):
    Font = pygame.font.Font(None, size)
    Surface = Font.render(text, True, (0, 0, 0))
    disp.blit(Surface, (x, y))
    pygame.display.update()
while True:
    on=True
    obsPos=[]
    score=0
    carPos=int((width/2)-50)
    speed=7
    while on:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover=-speed
                if event.key == pygame.K_RIGHT:
                    mover=speed
                if event.key == pygame.K_UP:
                    speedc=speedc+1
                if event.key == pygame.K_DOWN:
                    speedc=speedc-1
            if event.type == pygame.KEYUP:
                mover=0
                speedc=0
        speed=speed+speedc
        createObstacle=random.randint(0,15)
        if createObstacle==0:
            if len(obsPos)<9:
                obspos1=random.randint(0,width-50)
                obsPos.append([obspos1,0,obspos1-50,50])
        pygame.Surface.fill(disp,white)
        moveCar(0)
        for (i, value) in enumerate(obsPos):
            pygame.draw.rect(disp,black,(obsPos[i][0],obsPos[i][1],50,50))
            obsPos[i][1]=obsPos[i][1]+speed+3
            obsPos[i][3]=obsPos[i][3]+speed+3
            if obsPos[i][1]>height:
                del obsPos[i]
                score=score+1
        carPosLeft=carPos-50
        carPosRight=carPos+50
        carPosTop=height-200
        carPosBottom=height-25
        for i, value in enumerate(obsPos):
            if obsPos[i][0]>carPosLeft and obsPos[i][2]<carPosRight and obsPos[i][3]>carPosTop and obsPos[i][1]<carPosBottom:
                on=False
        moveCar(mover)
        displayText("Score: "+str(score)+" Speed:"+str(speed),0,0,30)
        pygame.display.update()
        clock.tick(60)
        if speed<1:
            speed=1
    messageDisplay("You crashed")
    displayText("Score: "+str(score),width/2,(height/2)+100,75)
    pygame.display.update()
    time.sleep(1.5)
    pygame.display.update()
