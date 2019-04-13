import cv2 as cv
import pyscreenshot as ImageGrab
import numpy
import pyautogui
import time

#posicoes importantes do jogo
RESTART_BUTTON = (986, 570)
BOX_ARVORE = (600, 620, 650, 650)
BOX_RESTART = (537, 520, 1039, 609)
 
def pegarFrame(area):                     
    image = ImageGrab.grab(area)
    image = cv.cvtColor(numpy.array(image), cv.COLOR_BGR2GRAY)
    return image 

def pular():
    pyautogui.press('space')
     
#código principal
pular()                     
while True:                                 
    img = pegarFrame(BOX_ARVORE)
    if numpy.any(img == 84):                                            
        pular()
        
