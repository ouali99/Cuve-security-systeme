from gpiozero import Button, LED
from time import sleep
from signal import pause
import SevenSeg

class Cuve :
    #Constructeur
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

        #__afficheur de type SevenSeg(relation de composition avec la class SevenSeg)
        self.__afficheur = SevenSeg.SevenSeg(self.__pa,self.__pb,self.__pc,self.__pd,self.__pe,self.__pf,self.__pg,self.__ppd,self.__type)
        
        #initialisation de l'affichage
        self.__pvr.on()
        self.alarmL()
        self.__afficheur.ShowL()

        # Configuration des evenement
        self.__pcn0.when_pressed = self.__updateState
        self.__pcn1.when_pressed = self.__updateState
        self.__pcn2.when_pressed = self.__updateState
        self.__pcn3.when_pressed = self.__updateState

        self.__pcn0.when_released = self.__updateState
        self.__pcn1.when_released = self.__updateState
        self.__pcn2.when_released = self.__updateState
        self.__pcn3.when_released = self.__updateState  


    #Methode pour le niveau de la cuve
    def __StateIndication(self,state):
        if state==4:
            self.__ShowState(state)
            self.__pvr.off()
            self.__pve.on()
            self.alarmH()
        else :
            self.__ShowState(state)
            self.__pvr.on()

    #Methode pour l'affichage du niveau(state)
    def __ShowState(self,state):
        if state == 1:
            self.__afficheur.Show1()
        elif state == 2:
            self.__afficheur.Show2()
        elif state == 3:
            self.__afficheur.Show3()
        elif state == 4:
            self.__afficheur.ShowH()
        elif state == 0:
            self.__afficheur.ShowL()
            self.alarmL()
            self.__afficheur.ShowL()

    #methode pour gerer l'etat des boutons
    def __updateState(self) :
        if self.__pcn0.is_pressed and self.__pcn1.is_pressed and self.__pcn2.is_pressed and self.__pcn3.is_pressed:
            self.__StateIndication(4)
        elif self.__pcn0.is_pressed and self.__pcn1.is_pressed and self.__pcn2.is_pressed:
            self.__StateIndication(3)
        elif self.__pcn0.is_pressed and self.__pcn1.is_pressed:
            self.__StateIndication(2)
        elif self.__pcn0.is_pressed:
            self.__StateIndication(1)
        else:
            self.__StateIndication(0)            
            self.__pve.off()
            
    
    def alarmL(self) :
        self.__afficheur.FlasL(True)

    def alarmH(self) :
        self.__afficheur.FlasH(False)

