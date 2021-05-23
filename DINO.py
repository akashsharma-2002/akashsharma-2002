import pyautogui
from win32com.client import Dispatch
from PIL import Image,ImageGrab
import time
from numpy import asarray

replay_button=(683,406)
dino=(142,439)
speak=Dispatch("SAPI.spVOICE")
speak.speak("your game is about to start in another 3 second")
speak.speak("hold back, and enjoy")
speak.speak("three")
speak.speak("two")
speak.speak("one")


def hit():
    pyautogui.click(replay_button)
def space():
    pyautogui.keyDown("up")
def down():
    pyautogui.keyDown("down")

def bird():
    imag=dino[0]+150,dino[1]-36,dino[0]+280,dino[1]-28
    img=ImageGrab.grab(imag).convert('L')
    b=asarray(img)
    print(b.sum())
    return(b.sum())

def collide():
    image=dino[0]+50,dino[1],dino[0]+260,dino[1]+41
    img=ImageGrab.grab(image).convert('L')
    b=asarray(img)
    print(b.sum())
    return(b.sum())

#bird= 816000
hit()

while(True):
    collide()
    bird()
    #black_cac()
    #black_bird()
    if(collide()!=2195550): #2195550
        space()

    elif(bird()!=265200 ):
        space()


