from gpiozero import Button, LED
from time import sleep
from signal import pause
import SevenSeg

class Cuve :
    def __init__(self,pve,pvr,pcn0,pcn1,pcn2,pcn3,pa,pb,pc,pd,pe,pf,pg,ppd,type):
        self.__pvr = LED(pvr)
        self.__pve = LED(pve)
        self.__pcn0 = Button(pcn0)
        self.__pcn1 = Button(pcn1)
        self.__pcn2 = Button(pcn2)
        self.__pcn3 = Button(pcn3)

        self.__pa = pa
        self.__pb = pb
        self.__pc = pc
        self.__pd = pd
        self.__pe = pe
        self.__pf = pf
        self.__pg = pg
        self.__ppd = ppd
        self.__type = type

        self.__afficheur = SevenSeg.SevenSeg(self.__pa,self.__pb,self.__pc,self.__pd,self.__pe,self.__pf,self.__pg,self.__ppd,self.__type)
        
        self.__pcn0.when_pressed = self.__check_buttons
        self.__pcn1.when_pressed = self.__check_buttons
        self.__pcn2.when_pressed = self.__check_buttons
        self.__pcn3.when_pressed = self.__check_buttons

        self.__pcn0.when_released = self.__check_buttons
        self.__pcn1.when_released = self.__check_buttons
        self.__pcn2.when_released = self.__check_buttons
        self.__pcn3.when_released = self.__check_buttons  


    def __levelIndication(self,lvl):
        if lvl==4:
            self.__showLevel(lvl)
            self.__pvr.off()
            self.__pve.on()
        else :
            self.__showLevel(lvl)
            self.__pvr.on()
    
    def __showLevel(self,lvl):
        if lvl == 1:
            self.__afficheur.Show1()
        elif lvl == 2:
            self.__afficheur.Show2()
        elif lvl == 3:
            self.__afficheur.Show3()
        elif lvl == 4:
            self.__afficheur.ShowH()
        elif lvl == 0:
            self.__afficheur.ShowL()

    def __check_buttons(self) :

        if self.__pcn0.is_pressed and self.__pcn1.is_pressed and self.__pcn2.is_pressed and self.__pcn3.is_pressed:
            self.__levelIndication(4)
        elif self.__pcn0.is_pressed and self.__pcn1.is_pressed and self.__pcn2.is_pressed:
            self.__levelIndication(3)
        elif self.__pcn0.is_pressed and self.__pcn1.is_pressed:
            self.__levelIndication(2)
        elif self.__pcn0.is_pressed:
            self.__levelIndication(1)
        else:
            self.__levelIndication(0)
            self.__pve.off()
            
    
    def alarmL(self) :
        self.__afficheur.FlasL()

    def alarmH(self) :
        self.__afficheur.FlasH()