# -*- coding: utf-8 -*-

from machine import Timer
chrono = Timer.Chrono()
chrono.start()


from wifi import Wifi_Init, Wifi_Perso, Wifi_Connect, Wifi_Local, Wifi_Lock, Wifi_Connect, Wipy_Server_Init

Wipy_Server_Init()
Wifi_Perso()

from gc import collect, mem_free

import time #time.sleep

import machine

rtc = machine.RTC()

from pycom import nvs_set, nvs_get

from planning import Planificateur, planning_make,planning_time_adjust,planning_prochain_depart_valeur, planning, set_date, planning_save, planning_get


from machine import Timer
import machine


from machine import RTC
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))
RTC(datetime=(1970, 1, 1, 0, 0, 0, 0, None)) # <= cette date permettra ultérieurement
# de vérifier si le wipy a redémarrer depuis la dernière mise à jour de son horloge
# si la date de l'horloge du wipy < 2018 alors c'est qu'il est rebooté

collect()

from mirobot2 import m


time.sleep(1)

m.stop()
m.bip(0.1)


from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT



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
                _Statut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_nom)
                if print_out == 1:
                    print('Envoi Statut = {}'.format(_Statut))
                conn.sendall(_Statut)
                conn.close()
            elif cmd[0] == 84: #caractère "T"
                if print_out == 1:
                    print('Envoi Etat')
                #conn.sendall('{}'.format(m.PIC_ASK('s')[:-1].decode('utf8')))
                conn.sendall('{}'.format(m.PIC_ASK('s')))
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
        collect()

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

planificateur = Planificateur(m)

check_fly_Indicator = 0
def check_fly():
    global check_fly_Indicator
    global planificateur
    global allow_to_fly
    while True:
        check_fly_Indicator = 1
        if allow_to_fly == 1:
            allow_to_fly = 0
            Resultat_Execution = Read_Prgm(prgm_planifier)
            allow_to_fly = 0
        planifie_prochain_cycle()
        collect()
        time.sleep(0.4)

import _thread


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


m.bip(0.1)

from commande import Interrupteur, DVT_recule, Avance, Recule,Pailleux, DVT, Multitas, Pelle_Baisse, Pelle_Leve, Orientation, Pause, Read_Prgm, Write_Prgm, Send_Prgm, Cmd_Execution, Execution, Alarme


planning = planning_get()

# Chrono_Store(0,0) # Reset des compteurs
# Chrono_Store(m.Nb_Seconde_Fonctionnement,0) # Reset du compteur Maintenance
# Chrono_Store(Maintenance=0) # Reset du compteur Maintenance
def Chrono_Store(Fonctionnement=m.Nb_Seconde_Fonctionnement, Maintenance=m.Nb_Seconde_Maintenance):
    m.Nb_Seconde_Fonctionnement = Fonctionnement
    m.Nb_Seconde_Maintenance = Maintenance
    nvs_set('TPS', int(Fonctionnement))
    nvs_set('TMA', int(Maintenance))

#### Relecture des paramètres de bases
Memory_Value = nvs_get('TPS') # Seconde de fonctionnement Total
if Memory_Value is not None:
    m.Nb_Seconde_Fonctionnement = Memory_Value
Memory_Value = nvs_get('TMA') # Seconde depuis la dernier maintenance
if Memory_Value is not None:
    m.Nb_Seconde_Maintenance = Memory_Value


Memory_Value = nvs_get('PAT')
if Memory_Value is not None:
    m.PATINAGE_TEMPS_s = Memory_Value
Memory_Value = nvs_get('MXC')
if Memory_Value is not None:
    m.Moteur_X_Consigne = Memory_Value
Memory_Value = nvs_get('MZC')
if Memory_Value is not None:
    m.Moteur_Z_Consigne = Memory_Value
Memory_Value = nvs_get('MZS')
if Memory_Value is not None:
    m.Moteur_Z_Limite_Courant = Memory_Value
Memory_Value = nvs_get('MBC')
if Memory_Value is not None:
    m.Moteur_Bequille_Consigne = Memory_Value
Memory_Value = nvs_get('NSP')
if Memory_Value is not None:
    m.Nb_Seconde_Pelle = Memory_Value
Memory_Value = nvs_get('IT1')
if Memory_Value is not None:
    m.PION_TEMPS_100ms = Memory_Value
Memory_Value = nvs_get('LT1')
if Memory_Value is not None:
    m.PLATINE_TEMPS_100ms = Memory_Value


Memory_Value = nvs_get('BV1')
if Memory_Value is not None:
    m.batterie_10_v = Memory_Value / 10
Memory_Value = nvs_get('BV3')
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
                    if rtc.now()[0] < 2017:
                        m.bip(0.1)
                    time.sleep(0.1)
                if rtc.now()[0] < 2017:
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

from config import Batt_Mean # batterie_reg_a, batterie_reg_b


#_thread.start_new_thread(Check_Clock(), ())


#import AiCwebserver
#AiCwebserver.AiCWebserv()

from AiCwebserver import AiCWebserv


####_thread.start_new_thread(AiCwebserver.AiCWebserv, ())
_thread.start_new_thread(AiCWebserv, (80,))
#m.web_thread = _thread.start_new_thread(AiCWebserv, (0,))


collect()

#Check_Clock()
_thread.start_new_thread(Check_Clock, ())

collect()




time.sleep(0.7)
m.PIC_LED(1)
m.bip(0.1)
m.PIC_LED(1)
m.PIC_LED(1)
time.sleep(1)
m.bip(0.1)
time.sleep(0.01)
m.PIC_LED(0)

chrono.stop()
m.startup_time = chrono.read()
#del(chrono)
