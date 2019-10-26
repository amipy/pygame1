import pygame

def drawLine(linearr, linenum, line):
    line = 5-line
    for ind, val in enumerate(linearr):
        if val:
            pygame.draw.rect(disp, blue, (linenum*10, ind*10-(len(linearr)*10-100)-(line-1)*110+450, 10, 10))
            pygame.draw.rect(disp, green, (linenum*10, 660-line*110, 10, 10))
            pygame.display.update()
           
disp = pygame.display.set_mode((1400,660))

white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
i=0

for line in range(0,6):
    linenum=0
    for e in range(0,140):
        binStr = bin(i)[2:]
        linearr = []
        for k in binStr:
            linearr.append(k == "1")
        drawLine(linearr, linenum, line)
        i+=1
        linenum+=1
