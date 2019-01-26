import pygame
import os
import time
import numpy as N
import pygame.surfarray as surfarray
import pickle
scriptDirectory = os.path.dirname(os.path.realpath(__file__))
pygame.init()
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(600/2))
    disp.blit(TextSurf, TextRect)

def doSave():
    cancel=False
    savedfull = []
    file=input("What would you like to name this?")
    if os.path.isfile(scriptDirectory+"/"+file+".drw"):
        over=input("That save alredy exists. do you want to override it? 1=yes 0=no, cancel.")
        if int(over)==0:
            cancel=True
            print ("Canceled.")
        if os.path.isfile(scriptDirectory+"/"+file+".unt"):
            print ("An untouchable drawing is already named that.")
            cancel=True
    if not cancel:
        savef = open(scriptDirectory+"/"+file+".drw","wb")
        print ("Saving.")
        for j in range(0, pygame.Surface.get_height(disp)):
            for i in range(0, pygame.Surface.get_width(disp)):
                savedfull.append(pygame.Surface.get_at(disp,(i,j)))
        pickle.dump(savedfull, savef, pickle.HIGHEST_PROTOCOL)
        savef.close()
        print ("Saved.")
                            
disp=pygame.display.set_mode((800,600))
pygame.display.set_caption('Draw')
clock = pygame.time.Clock()
active = True
white = (255,255,255)
black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
orange = (255,165,0)
color=black
w=3
h=3
md=False
saved= []
savedfull = []
disp.fill(white)
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active=False
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(disp, color,(0,0,800,20))
        if event.type == pygame.MOUSEBUTTONDOWN:
            md=True
        if event.type == pygame.MOUSEBUTTONUP:
            md=False
        if md:
            if color == (255,255,255):
                pygame.draw.rect(disp, color,(mouse[0]-3,mouse[1]-3,7,7))
            else:
                pygame.draw.rect(disp, color,(mouse[0]-1,mouse[1]-1,w,h))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                disp.fill(white)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                color=white
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                color=black
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color=red
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                color=green
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                color=blue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                color=yellow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                color=orange
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                run = True
                while run:
                    decision = input("What would you like to do? Type help for help.")
                    if decision.lower()=="save":
                        doSave()
                    elif decision.lower()=="load":
                        exist=True
                        file=input("What would you like to load?")
                        if not os.path.isfile(scriptDirectory+"/"+file+".drw") and not os.path.isfile(scriptDirectory+"/"+file+".unt") and not os.path.isfile(scriptDirectory+"/"+file+".txt"):
                            print ("Drawing does not exist.")
                            exist=False
                        if os.path.isfile(scriptDirectory+"/"+file+".txt"):
                            print ("This is a text file and cannot be opened from within the application.")
                            exist = False
                        if exist:
                            if os.path.isfile(scriptDirectory+"/"+file+".drw"):
                                savef = open(scriptDirectory+"/"+file+".drw","rb")
                            if os.path.isfile(scriptDirectory+"/"+file+".unt"):
                                savef = open(scriptDirectory+"/"+file+".unt","rb")
                            print ("Loading.")
                            finaltrans = pickle.load(savef)
                            ded=0
                            for j in range(0, pygame.Surface.get_height(disp)):
                                for i in range(0, pygame.Surface.get_width(disp)):
                                    pygame.Surface.set_at(disp,(i,j),finaltrans[ded])
                                    ded = ded + 1
                            print ("Loaded.")
                            savef.close()
                    elif decision.lower()=="list":
                        print (os.listdir(scriptDirectory))
                    elif decision.lower()=="delete":
                        exist = True
                        file = input("What drawing do you want to delete?")
                        if not os.path.isfile(scriptDirectory+"/"+file+".drw"):
                            if os.path.isfile(scriptDirectory+"/"+file+".unt"):
                                print ("Drawing is untouchable")
                                exist = False
                            else:
                                print ("Drawing does not exist.")
                                exist=False
                        if exist:
                            cont=True
                            yes=input("Do you want to continue or not? 1 or 0.")
                            if yes == "1":
                                os.remove(scriptDirectory+"/"+file+".drw")
                                print ("Deleted")
                            else:
                                print ("Canceled")
                    elif decision.lower() =="help":
                        print ("save :saves the drawring. \nload :loads a drawing. \nlist :lists all drawings. \ndelete :deletes a drawing. \nhelp :lists commands. \nexit :exits command line. \nquit :quits the program. same as escape key or X button.")
                    elif decision.lower() =="untouchable":
                        file = input("What drawing do you want to make untouchable?")
                        cancel = False
                        if not os.path.isfile(scriptDirectory+"/"+file+".drw"):
                            print ("Drawing does not exist.")
                            cancel = True
                        if os.path.isfile(scriptDirectory+"/"+file+".unt"):
                            print ("A drawing named that is already untouchable.")
                            cancel = True
                        if not cancel:
                            os.rename(scriptDirectory+"/"+file+".drw",scriptDirectory+"/"+file+".unt")
                            print ("Drawing is now untouchable.")
                    elif decision.lower() =="exit":
                        print ("Exited")
                        run = False
                    elif decision.lower() =="quit":
                        active=False
                        run = False
                    else:
                        print ("Invalid command.")
                    pygame.display.update()
        pygame.display.update()
message_display('Bye!')
pygame.display.update()
time.sleep(.5)
pygame.quit()
