from test_OOP_temp import TempSensor
from oop_lcd1 import IspisNaLCD

temp_senzor = TempSensor()
ispis = IspisNaLCD()

while (True):
        #LOADING VISUALISATION
        ispis.setPisi("##            ","",0.05)
        ispis.setPisi("  ##          ","",0.05)
        ispis.setPisi("    ##        ","",0.05)
        ispis.setPisi("      ##      ","",0.05)
        ispis.setPisi("        ##    ","",0.05)
        ispis.setPisi("          ##  ","",0.05)
        ispis.setPisi("            ##","",0.05)
        ispis.setPisi("","##            ",0.05)
        ispis.setPisi("","  ##          ",0.05)
        ispis.setPisi("","    ##        ",0.05)
        ispis.setPisi("","      ##      ",0.05)
        ispis.setPisi("","        ##    ",0.05)
        ispis.setPisi("","          ##  ",0.05)
        ispis.setPisi("","            ##",0.05)
        rez=temp_senzor.getRez()
        ispis.setPisi("Temp: {0[1]}".format(rez)+chr(223)+"C" , "Vlaga: {0[0]} %".format(rez),3)
