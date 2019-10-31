
from machine import Timer
import machine
#from mirobot2 import Mirobot


CAPTEUR_PION = machine.Pin('P19', mode=machine.Pin.IN, pull=None)

#PION_TEMPS_ms = 2000 # Debug
PION_TEMPS_ms = 100 # valeur réel de test
#PLATINE_TEMPS_total = PION_TEMPS_ms + PLATINE_TEMPS_ms
#PLATINE_TEMPS_ms = 4000 # Debug
PLATINE_TEMPS_ms = 2000 # valeur réel de test


class Capteur_Pion_Alarm:

    #def __init__(self, mirobot, temps_detection=PION_TEMPS_ms, etat_initial='Metal'):
    def __init__(self, mirobot, temps_detection=PION_TEMPS_ms, etat_initial=None):
        """Genere une alarme a la frequence passer en parametre"""
        self.Etat = 1
        self.mirobot = mirobot
        self.etat_initial = etat_initial if etat_initial is not None else 'Metal'
        self.mirobot.Capteur_Pion = self.etat_initial
        #self.turn = 0
        #self.action = self.Mirobot_start if action is None else action
        #self.tour_a_faire = 50
        # if temps_echantillonnage == 'Infinie':
        self.alarm = Timer.Alarm(self.action , ms=temps_detection, periodic=False)
        #self.__alarm = Timer.Alarm(self.Mirobot_start, s=sleep_seconde, periodic=False)
        # else:
        #     self.tour_a_faire = int(temps_echantillonnage*frequence_echantillonnage)
        #     self.__alarm = Timer.Alarm(self._Clock_ADC_handler, us=int(1e6/frequence_echantillonnage), periodic=True)

    def stop(self):
        self.Etat = 0
        self.alarm.cancel()
        del(self.alarm)
        #self.__alarm.callaback(None)

    def action(self, alarm):
        #global verification_platine
        #print(globals())
        #print('verification_pion' in globals())
        if CAPTEUR_PION() == 1:
            if self.etat_initial == 'Metal':
                self.mirobot.Capteur_Pion = 'Pion'
                self.mirobot.PION = 1
                self.mirobot.Capteur_Pion_Nb_Evenement += 1
                print("Détection Pion")
                verification_platine = Capteur_Pion_Alarm(self.mirobot, temps_detection=PLATINE_TEMPS_ms,  etat_initial=self.mirobot.Capteur_Pion)
            elif self.etat_initial == 'Pion':
                self.mirobot.Capteur_Pion = 'Platine'
                self.mirobot.PLATINE = 1
                #self.mirobot.stop()
                self.mirobot.stop(cause=self.mirobot.Etat_List['E']) # 'Platine'
                self.mirobot.Capteur_Pion_Evenement = 0
                print("Détection Platine")
                #print("Etat du capteur Pion: " + self.mirobot.Capteur_Pion)
        else:
            #self.mirobot.Nb_Signal_Pion = 0
            #On rend la main au trigger du capteur de Pion
            self.mirobot.Capteur_Pion_Evenement = 0
            print("Etat définitif retenu du capteur Pion: " + self.mirobot.Capteur_Pion)
        self.stop()

#
# Nb_Signal_Pion = 0
# def Pion_Incremente(arg):
#     m.Capteur_Pion = 'Metal'
#     Nb_Signal_Pion += 1
#     verification_pion = Capteur_Pion_Alarm()
#     #verification_pion = Capteur_Pion_Alarm(temps_detection=PION_TEMPS_ms,  etat_initial=m.Capteur_Pion)
#
#
# CAPTEUR_PION.callback(machine.Pin.IRQ_RISING, Pion_Incremente)


#PATINAGE_TEMPS_s = 20
#PATINAGE_TEMPS_s = 90

PATINAGE_TEMPS_s = 50 # modif du 17 avril

# PION_TEMPS_ms = 2000
# #PLATINE_TEMPS_total = PION_TEMPS_ms + PLATINE_TEMPS_ms
# PLATINE_TEMPS_ms = 4000


class Patinage_Detection:

        def __init__(self, mirobot, temps_anti_patinage=PATINAGE_TEMPS_s):
            """Genere une alarme a la frequence passer en parametre"""
            #print("Patinage_Detection ACTIVER")
            #self.Etat = 1
            self.mirobot = mirobot
            self.temps_anti_patinage = temps_anti_patinage
            self.activation = 0
            #self.turn = 0
            #self.action = self.Mirobot_start if action is None else action
            #self.tour_a_faire = 50
            # if temps_echantillonnage == 'Infinie':
            #self.alarm = Timer.Alarm(self.action , s=temps_anti_patinage, periodic=True)
            #self.__alarm = Timer.Alarm(self.Mirobot_start, s=sleep_seconde, periodic=False)
            # else:
            #     self.tour_a_faire = int(temps_echantillonnage*frequence_echantillonnage)
            #     self.__alarm = Timer.Alarm(self._Clock_ADC_handler, us=int(1e6/frequence_echantillonnage), periodic=True)

        def start(self):
            if self.activation == 1:
                self.stop()
            self.activation = 1
            print("Patinage_Detection ACTIVER")
            self.alarm = Timer.Alarm(self.action , s=self.temps_anti_patinage, periodic=True)

        def stop(self):
            if self.activation == 1:
                self.activation = 0
                print("Patinage_Detection DéSACTIVER")
                #self.Etat = 0
                self.alarm.cancel()
                del(self.alarm)
            #self.__alarm.callaback(None)

        def action(self, alarm):
            #global verification_platine
            #print(globals())
            #print('verification_pion' in globals())
            if self.mirobot.Etat == self.mirobot.Etat_List['8'] or self.mirobot.Etat == self.mirobot.Etat_List['9']: #avance ou recule
                #if not( self.mirobot.Capteur_Pion == 'Pion' or self.mirobot.Capteur_Pion == 'Platine'):
                if not( self.mirobot.PION ):
                    print("PATINAGE DETECTER")
                    self.mirobot.stop(cause=self.mirobot.Etat_List['7']) # 'Patinage'
                    self.stop()
                else:
                    self.mirobot.PION = 0
                    print("Detection Patinage executer: PAS DE PATINAGE DETECTER")
            else:
                self.mirobot.PION = 0
                print("Detection Patinage hors fonctionnement 'Avance' ou 'Recule'")
                self.stop()
            # if CAPTEUR_PION() == 1:
            #     if self.etat_initial == 'Metal':
            #         self.mirobot.Capteur_Pion = 'Pion'
            #         print("Etat du capteur Pion: " + self.mirobot.Capteur_Pion)
            #         verification_platine = Capteur_Pion_Alarm(self.mirobot, temps_detection=PLATINE_TEMPS_ms,  etat_initial=self.mirobot.Capteur_Pion)
            #     elif self.etat_initial == 'Pion':
            #         self.mirobot.Capteur_Pion = 'Platine'
            #         self.mirobot.stop()
            #         print("Etat du capteur Pion: " + self.mirobot.Capteur_Pion)
            # else:
            #     self.mirobot.Nb_Signal_Pion = 0
            #     print("Etat du capteur Pion: " + self.mirobot.Capteur_Pion)
            #self.stop()
