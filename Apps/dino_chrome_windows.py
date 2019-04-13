from PIL import ImageGrab
import time
import numpy
import pyautogui

box = (400, 584, 550, 677)


def pegarScreen():
    img = ImageGrab.grab(box).convert('L')
    img = numpy.array(img)

    return img


def pular():
    pyautogui.press('space')


time.sleep(2)
pular()
while True:
    img = pegarScreen()
    if numpy.any(img != 255):
        pular()
