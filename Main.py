import Cuve 
from time import sleep
class Main:

    #Constructeur
    def __init__(self):
        self.cuve = Cuve.Cuve(pve=2, pvr=27, pcn0=22, pcn1=5, pcn2=6, pcn3=19, 
                         pa=24, pb=9, pc=10, pd=11, pe=12, pf=13, pg=17, ppd=1, type=False)

if __name__ == "__main__":
    Main()
