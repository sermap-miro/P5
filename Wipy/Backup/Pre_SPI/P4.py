# -*- coding: utf-8 -*-


#UPDATE WIPY OEM:
# connect P2 to the ground
# connect power
# pulse connect the jumper SJ1 (Wipy Reset)
# start pycom update

Fichier_Depart = 'planning.txt'
#
# PION_TEMPS_ms = 2000
# #PLATINE_TEMPS_total = PION_TEMPS_ms + PLATINE_TEMPS_ms
# PLATINE_TEMPS_ms = 4000
#


#
# V_BATTERIE_FAIBLE = 22.3 # Volt
# Conversion_Volt_Lopy = 3.3/4095
# Facteur_Pont_Resistance_30V = 9.3




ALLUMER = True
ETEINT = False

Mirobot_Etat = ''

import gc

def Mem_Free():
    gc.collect()

import time #time.sleep


import machine


adc= machine.ADC()



from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

#
# #Entrée
# #BP = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
# ARRET_URGENCE = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
#
# #Sortie
# #BUZZER = machine.Pin('P21', mode=machine.Pin.OUT)#Version 3.3V
# BUZZER = machine.Pin('P19', mode=machine.Pin.OUT)#Version 3.3V
# BUZZER(False)

#LED = machine.Pin('P20', mode=machine.Pin.OUT)#Version 3.3V

#DAC

#DAC_1 = machine.DAC('P22')        # create a DAC object
#DAC_2 = machine.DAC('P21')   # create a DAC object #Version 3.3V => BUZZER

from wifi import Wifi_Init
#Wifi_Init()






#
# def Arret_Urgence(arg):
#     #for _ in range()
#     BUZZER(True)
#     time.sleep(1)
#     BUZZER(False)
#     time.sleep(0.1)
#     BUZZER(True)
#     time.sleep(0.1)
#     BUZZER(False)
#     ARRET_URGENCE.callback(machine.Pin.IRQ_RISING , None)
#
# ARRET_URGENCE.callback(machine.Pin.IRQ_RISING , Arret_Urgence)










#wlanConnection()
rtc = machine.RTC()


import pycom
pycom.heartbeat(False)

#### Relecture des paramètres de bases


###


import uos


from planning import Planificateur, planning_make,planning_time_adjust,planning_prochain_depart_valeur, planning, set_date, planning_save, planning_get


from machine import Timer
import machine



from machine import RTC
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))
RTC(datetime=(1970, 1, 1, 0, 0, 0, 0, None)) # <= cette date permettra ultérieurement
# de vérifier si le wipy a redémarrer depuis la dernière mise à jour de son horloge
# si la date de l'horloge du wipy < 2018 alors c'est qu'il est rebooté

gc.collect()

from mirobot2 import m


time.sleep(1)
#for _ in range(1000):
m.uart_PIC.write('U') # Auto Baud Rate


def PIC_Test(t=0.1, k=50):
    for _i in range(k):
        PIC_USEND(t)
        time.sleep(t)

def PIC_USEND(Temps_Attente=0.05):
    self.uart_PIC.write('\r')
    time.sleep(0.02)
    self.uart_PIC.write('a\r')
    time.sleep(Temps_Attente)
    self.uart_PIC.write('U')


try:
    _Fichier_Wifi_Nom = open('/flash/wifi_name.txt', "r")
    wifi_nom = _Fichier_Wifi_Nom.read()
    _Fichier_Wifi_Nom.close()

    if len(wifi_nom)>0:
        m.wifi_name = 'P5 - ' + wifi_nom
    else:
        raise MonException("Valeur du SSID vide")
        #m.wifi_name = 'P5'
except:
    m.wifi_name = 'P5'
    wifi_nom = 'Empty'

Wifi_Init(m.wifi_name)


m.stop()
m.bip(0.1)




import socket

def Signal_Sonore():
    m.bip(0.02)

SOCKET_DATA = ""
print_out = 0
print_out_data = ''
def Socket_Attente():
    global SOCKET_DATA
    global print_out
    global print_out_data
    #print_out = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8111))
    s.listen()
    while True:
        try:
            #LED_set(_VERT_CLAIR)
            if print_out == 1:
                print("Wait a connection...")
            (conn, addr) = s.accept()
            #m.bip(0.1)
            Signal_Sonore()
            #LED_set(_ROUGE)
            if print_out == 1:
                print("Got a connection from %s" % str(addr))
            conn.settimeout(4)
            cmd = conn.readline()
            if print_out == 1:
                print("cmd receive = {}".format(cmd))
                print("cmd[0] = {}".format(cmd[0]))
                print("cmd[1] = {}".format(cmd[1]))
            SOCKET_DATA = cmd
            #if cmd[0] == b'>':
            #print("cmd = " + str(cmd))
            #print("cmd[0] = " + str(cmd[0]))
            if cmd[0] == 62: #caractère ">"
                #exec(cmd[1:])
                #print(cmd[1:-1])
                #conn.sendall(b'Reception OK')
                if print_out == 1:
                    print('Envoi Statut: '+ m.STATUT_BRUT + "("+ str(len(m.STATUT_BRUT))+")")
                conn.sendall(m.STATUT_BRUT)
                conn.close()
            elif cmd[0] == 60: #caractère "<"
                if print_out == 1:
                    print('Envoi Planning')
                #print('Envoi Planning')
                conn.sendall('{}'.format(planning))
                conn.close()
            elif cmd[0] == 70: #caractère "F" #  echo -ne 'F1\nA\nB\nL\n' | nc 192.168.4.1 8111
                #_Prgm_Indice = cmd[1]
                #_Prgm_Indice = '{}'.format(cmd[1])
                _Prgm_Indice = chr(cmd[1])
                data = ''
                try:
                    data = conn.readall()
                    if print_out == 1:
                        print_out_data = 'Ecriture Prgm({}): data = "{}"'.format(_Prgm_Indice, data)
                    # while True:
                    #     _data = conn.readline() # conn.recv(4096)
                    #     if not _data: break
                    #     data += _data
                except:
                    data = ''
                    if print_out == 1:
                        print_out_data = 'Exception Ecriture Prgm({})'.format(_Prgm_Indice)
                print(print_out_data)
                Write_Prgm(_Prgm_Indice, data)
                conn.close()
            elif cmd[0] == 71: #caractère "G"
                # if cmd[1] == 82 : #caractère "R"
                #     _Prgm_Indice = 'R'
                # elif cmd[1] == 49 : #caractère "1"
                #     _Prgm_Indice = '1'
                # elif cmd[1] == 50: #caractère "2"
                #     _Prgm_Indice = '2'
                # elif cmd[1] == 51 : #caractère "3"
                #     _Prgm_Indice = '3'
                # elif cmd[1] == 52 : #caractère "4"
                #     _Prgm_Indice = '4'
                # elif cmd[1] == 53 : #caractère "5"
                #     _Prgm_Indice = '5'
                # elif cmd[1] == 54 : #caractère "6"
                #     _Prgm_Indice = '6'
                # elif cmd[1] == 55 : #caractère "7"
                #     _Prgm_Indice = '7'
                # elif cmd[1] == 56 : #caractère "8"
                #     _Prgm_Indice = '8'
                # elif cmd[1] == 57 : #caractère "9"
                #     _Prgm_Indice = '9'
                # else:
                #     _Prgm_Indice = '1'
                #data_to_send = ''
                _Prgm_Indice = chr(cmd[1])
                try:
                    data_to_send = Send_Prgm(_Prgm_Indice)
                except:
                    data_to_send = ''
                if print_out == 1:
                    print('Envoi Prgm({}): {}'.format(_Prgm_Indice, data_to_send))
                conn.sendall('{}'.format(data_to_send))

                conn.close()
            elif cmd[0] == 72: #caractère "H"
                if print_out == 1:
                    print('Envoi Horaire')
                conn.sendall('{}'.format(rtc.now()))
                conn.close()
            elif cmd[0] == 68: #caractère "D"
                if print_out == 1:
                    print('Envoi Date')
                conn.sendall('{},{}'.format(rtc.now(),planning))
                conn.close()
            elif cmd[0] == 83: #caractère "S"
                if print_out == 1:
                    print('Envoi Statut')
                #conn.sendall('{} {} {}'.format(m.PIC_ASK('S')[:-1].decode('utf8'), ARRET_URGENCE(), m.batterie()))
                conn.sendall('{} {} {} {} {}'.format(m.PIC_ASK('S')[:-1].decode('utf8'), m.version, ARRET_URGENCE(), m.batterie(), wifi_nom))
                conn.close()
            elif cmd[0] == 84: #caractère "T"
                if print_out == 1:
                    print('Envoi Etat')
                conn.sendall('{}'.format(m.PIC_ASK('s')[:-1].decode('utf8')))
                conn.close()
            else:
                #Ici il faut mettre la procédure qui vérifie la commande
                #et envoi un message de retour si nécessaire (ex: Statut)
                conn.close()
                if cmd is not None:
                    #print(cmd[:-1])
                    exec(cmd)
            #conn.close()
        except:
            pass
        gc.collect()

def Attente_Prochaine_Verification_Depart(Temps_Attente=30):
    global allow_to_fly
    while((allow_to_fly == 0) and (Temps_Attente>0)):
        Temps_Attente -= 1
        time.sleep(1)



depart_planifier = 0
prgm_planifier = 0
allow_to_fly = 0
def planifie_prochain_cycle():
    global planificateur
    global depart_planifier
    global prgm_planifier
    global allow_to_fly
    #_prochain_depart_en_s = planning_prochain_depart(planning)
    (_prochain_depart_en_s, _prgm_planifier) = planning_prochain_depart_valeur(planning)
    #planificateur.allow_to_fly = 0
    if _prochain_depart_en_s is not None:
        print("Il reste {} s (= {:2.1f} min = {:2.1f} h ) d'attente pour le prochain départ (programme {})".format(_prochain_depart_en_s, _prochain_depart_en_s/60.0, _prochain_depart_en_s/3600.0, _prgm_planifier))
        #planificateur.start(sleep_seconde=_prochain_depart_en_s)
        depart_planifier = 1
        if(_prochain_depart_en_s > 30):
            #time.sleep(30)
            Attente_Prochaine_Verification_Depart(30)
        elif(_prochain_depart_en_s > 15):
            #time.sleep(10)
            Attente_Prochaine_Verification_Depart(10)
        else:
            print('Départ dans {}'.format(_prochain_depart_en_s))
            time.sleep(_prochain_depart_en_s)
            allow_to_fly = 1
            prgm_planifier = _prgm_planifier
    else:
        depart_planifier = 0
        print("Pas de départ activé dans le planning actuel (réveil dans 30 s)")
        #time.sleep(30)
        Attente_Prochaine_Verification_Depart(30)
    #planificateur.start(m, sleep_seconde=planning_prochain_depart())

def cycle_retour():
    global prgm_planifier
    global allow_to_fly
    prgm_planifier = 'retour'
    #planificateur.allow_to_fly = 1
    allow_to_fly = 1

def cycle_standard():
    global prgm_planifier
    global allow_to_fly
    prgm_planifier = 'Standard'
    #planificateur.allow_to_fly = 1
    allow_to_fly = 1
    #Read_Prgm(1)


# def cycle_pelle():
#     Read_Prgm(1)


#planning=planning_make(17,16,n=20)

#planning=list()

# Capteur_Activer()

planificateur = Planificateur(m)

check_fly_Indicator = 0
def check_fly():
    global check_fly_Indicator
    global planificateur
    global allow_to_fly
    while True:
        check_fly_Indicator = 1
        if allow_to_fly == 1:
            # if planificateur.allow_to_fly == 1:
            #     planificateur.allow_to_fly = 0
            allow_to_fly = 0
            Resultat_Execution = Read_Prgm(prgm_planifier)
            allow_to_fly = 0
            #cycle_standard()
            #cycle_pelle()
            #planifie_prochain_cycle()
        #if depart_planifier == 0
        #print("Nouvelle vérification de départ dans 1 min")
        planifie_prochain_cycle()
        gc.collect()
        time.sleep(0.4)

#planifie_prochain_cycle()


import _thread
# #check_fly()
# #Socket_Attente()
# #_thread.start_new_thread(th_func, (i + 1, i))
#


Thread_Check_Fly = 0

def start_Check_Fly():
    global Thread_Check_Fly
    global planificateur
    if Thread_Check_Fly == 0:
        Thread_Check_Fly = 1
        planificateur.allow_to_fly = 0
        _thread.start_new_thread(check_fly, ())

start_Check_Fly()

_thread.start_new_thread(Socket_Attente, ())
#_thread.start_new_thread(check_fly, ())
#Thread_Check_Fly = 1


def Arret_Urgence(arg):
    m.bloque()
    time.sleep(1)
    m.bloque()
    m.reset()
#     # if ARRET_URGENCE() == 1: # il y a un probleme
#     #     m.bloque()
#     # else:
#     #     m.bip(1)


# def Arret_Urgence_Activation(arg):
#     global ARRET_URGENCE
#     m.bloque()
#     ARRET_URGENCE.callback(machine.Pin.IRQ_LOW_LEVEL, None)
#     ARRET_URGENCE.callback(machine.Pin.IRQ_LOW_LEVEL, Arret_Urgence_Desactivation)
#
#
# def Arret_Urgence_Desactivation(arg):
#     global ARRET_URGENCE
#     ARRET_URGENCE.callback(machine.Pin.IRQ_HIGH_LEVEL, None)
#     ARRET_URGENCE.callback(machine.Pin.IRQ_HIGH_LEVEL, Arret_Urgence_Activation)
#     #m.bloque()

#ARRET_URGENCE.callback(machine.Pin.IRQ_RISING | machine.Pin.IRQ_HIGH_LEVEL, Arret_Urgence)

ARRET_URGENCE.callback(machine.Pin.IRQ_RISING , Arret_Urgence)
#ARRET_URGENCE.callback(machine.Pin.IRQ_FALLING , Arret_Urgence)
#ARRET_URGENCE.callback(machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, Arret_Urgence)
# ARRET_URGENCE.callback(machine.Pin.IRQ_HIGH_LEVEL, Arret_Urgence_Activation)
# if ARRET_URGENCE() == 1:
#     ARRET_URGENCE.callback(machine.Pin.IRQ_LOW_LEVEL, Arret_Urgence_Desactivation)
# else:
#     ARRET_URGENCE.callback(machine.Pin.IRQ_HIGH_LEVEL, Arret_Urgence_Activation)

# ARRET_URGENCE.callback(machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, Arret_Urgence)

# def Buzzer_Input(arg):
#     if BUZZER_INPUT() == 1:
#         BUZZER(True)
#         #time.sleep(1)
#         #BUZZER(False)
#     else:
#         BUZZER(False)
#
# #ARRET_URGENCE.callback(machine.Pin.IRQ_RISING | machine.Pin.IRQ_HIGH_LEVEL, Arret_Urgence)
#
# BUZZER_INPUT.callback(machine.Pin.IRQ_RISING |machine.Pin.IRQ_FALLING , Buzzer_Input)
#
# m.uart_PIC.write('\r') # Seconde Initialisation de la comm avec le PIC
# m.uart_PIC.write('\r') # Seconde Initialisation de la comm avec le PIC
m.bip(0.1)

from commande import Avance, Recule,Pailleux, DVT, Multitas, Pelle_Baisse, Pelle_Leve, Orientation, Pause, Read_Prgm, Write_Prgm, Send_Prgm, Cmd_Execution, Execution, Alarme


planning = planning_get()

# Chrono_Store(0,0) # Reset des compteurs
# Chrono_Store(m.Nb_Seconde_Fonctionnement,0) # Reset du compteur Maintenance
# Chrono_Store(Maintenance=0) # Reset du compteur Maintenance
def Chrono_Store(Fonctionnement=m.Nb_Seconde_Fonctionnement, Maintenance=m.Nb_Seconde_Maintenance):
    m.Nb_Seconde_Fonctionnement = Fonctionnement
    m.Nb_Seconde_Maintenance = Maintenance
    pycom.nvs_set('TPS', int(Fonctionnement))
    pycom.nvs_set('TMA', int(Maintenance))

#### Relecture des paramètres de bases
Memory_Value = pycom.nvs_get('TPS') # Seconde de fonctionnement Total
if Memory_Value is not None:
    m.Nb_Seconde_Fonctionnement = Memory_Value
Memory_Value = pycom.nvs_get('TMA') # Seconde depuis la dernier maintenance
if Memory_Value is not None:
    m.Nb_Seconde_Maintenance = Memory_Value


Memory_Value = pycom.nvs_get('PAT')
if Memory_Value is not None:
    m.PATINAGE_TEMPS_s = Memory_Value
Memory_Value = pycom.nvs_get('MXC')
if Memory_Value is not None:
    m.Moteur_X_Consigne = Memory_Value
Memory_Value = pycom.nvs_get('MZC')
if Memory_Value is not None:
    m.Moteur_Z_Consigne = Memory_Value
Memory_Value = pycom.nvs_get('MZS')
if Memory_Value is not None:
    m.Moteur_Z_Limite_Courant = Memory_Value
Memory_Value = pycom.nvs_get('MBC')
if Memory_Value is not None:
    m.Moteur_Bequille_Consigne = Memory_Value
Memory_Value = pycom.nvs_get('NSP')
if Memory_Value is not None:
    m.Nb_Seconde_Pelle = Memory_Value
Memory_Value = pycom.nvs_get('IT1')
if Memory_Value is not None:
    m.PION_TEMPS_100ms = Memory_Value
Memory_Value = pycom.nvs_get('LT1')
if Memory_Value is not None:
    m.PLATINE_TEMPS_100ms = Memory_Value

#Calibration Batterie
# Memory_Value = pycom.nvs_get('BRA')
# if Memory_Value is not None:
#     m.batterie_reg_a = Memory_Value
# Memory_Value = pycom.nvs_get('BRB')
# if Memory_Value is not None:
#     m.batterie_reg_b = Memory_Value
Memory_Value = pycom.nvs_get('BV1')
if Memory_Value is not None:
    m.batterie_10_v = Memory_Value / 10
Memory_Value = pycom.nvs_get('BV3')
if Memory_Value is not None:
    m.batterie_30_v = Memory_Value / 10



m.PIC_PARAM_UPDATE()
###



def Check_Clock():
    _sec = 0
    while rtc.now()[0] < 2017:
        if _sec == 28: # environ toutes les 30 secondes
            _sec = 0
            for _ in range(4):
                for __ in range(4):
                    m.bip(0.1)
                    time.sleep(0.1)
                m.bip(1)
                time.sleep(0.4)
        time.sleep(1)
        _sec += 1

#_thread.start_new_thread(Check_Clock(), ())

time.sleep(0.7)
m.PIC_LED(1)
m.bip(0.1)
m.PIC_LED(1)
m.PIC_LED(1)
time.sleep(1)
m.bip(0.1)
time.sleep(0.01)#nécessaire ou sinon la led ne s'allume pas!
m.PIC_LED(0)

time.sleep(5)

Check_Clock()

gc.collect()


from config import Batt_Mean # batterie_reg_a, batterie_reg_b


#_thread.start_new_thread(Check_Clock(), ())


#import AiCwebserver
#AiCwebserver.AiCWebserv()

from AiCwebserver import AiCWebserv


#_thread.start_new_thread(AiCwebserver.AiCWebserv, ())
_thread.start_new_thread(AiCWebserv, ())


time.sleep(0.7)
m.PIC_LED(1)
m.bip(0.1)
m.PIC_LED(1)
m.PIC_LED(1)
time.sleep(1)
m.bip(0.1)
time.sleep(0.01)
m.PIC_LED(0)

time.sleep(5)



# for _ in range(10):
#     m.PIC_ASK('E{}'.format(_))
#m.PIC_ASK('E{}'.format(0))
#print_out = 1
#m.print_out = 1

# planning=planning_make(17,12,n=2)
# planning=planning_make(8,10,n=2)
#
# prochaine_action = OneShoot(sleep_seconde=planning_prochain_depart(), action=Mirobot_start)
#
# prochaine_action = OneShoot(sleep_seconde=2, action=Mirobot_start)
# prochaine_action = OneShoot(sleep_seconde=2)


#
# from machine import WDT
# wdt = WDT(timeout=2000)  # enable it with a timeout of 2 seconds
# wdt.feed()

# import pycom
#
# pycom.nvs_set('temp', 25)
# pycom.nvs_set('count', 10)
#
# pulses = pycom.nvs_get('count')
# pycom.nvs_erase(key)
# pycom.nvs_erase_all()

#gc.mem_free() => 2518928
