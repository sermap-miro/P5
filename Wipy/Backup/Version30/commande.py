# -*- coding: utf-8 -*-
#global m
from mirobot2 import m
import time
from pycom import nvs_set



from es import ARRET_URGENCE, BUZZER#, BUZZER_INPUT

#en cas d'alerte sur un programme
class Sortie_Prgm(Exception):

    def __init__(self,raison):
        self.raison = raison

    def __str__(self):
        return self.raison


_LIBRE = 0
_OCCUPER = 1
#from machine import Timer


_EXECUTION_IMPOSSIBLE = 2
_EXECUTION_OK = 1
_EXECUTION_ERREUR = 0

def Alarme():
    _thread.start_new_thread(m.alarme, ())

def Execution(Commande, Option=''):
    if Commande == 'A':
        if Option!='':
            return Avance(Pion=Option)
        else:
            return Avance()
    elif Commande == 'R':
        if Option!='':
            return Recule(Pion=Option)
        else:
            return Recule()
    elif Commande == 'P':
        if Option!='':
            return Pailleux(Pion=Option)
        else:
            return Pailleux()
    elif Commande == 'D':
        if Option!='':
            return DVT(Seconde=Option)
        else:
            return DVT()
    elif Commande == 'E':
        if Option!='':
            return DVT_recule(Seconde=Option)
        else:
            return DVT_recule()
    elif Commande == 'M':
        if Option!='':
            return Multitas(Patinage=Option)
        else:
            return Multitas()
    elif Commande == 'B':
        return Pelle_Baisse()
    elif Commande == 'L':
        return Pelle_Leve()
    elif Commande == 'O':
        if Option!='':
            return Orientation(Direction=Option)
        else:
            return Orientation()
    elif Commande == 'S':
        return Pause(Seconde=Option)
    elif Commande == 'I':
        return Interrupteur(Activation=Option)
    else:
        return _EXECUTION_IMPOSSIBLE
    #time.sleep(2)


def Cmd_Execution(Commande):
    if Commande[0] in {'A', 'R', 'P', 'D', 'E', 'M', 'S', 'I'}:
        try:
            valeur_option = int(Commande[1:])
            return Execution(Commande[0], valeur_option)
        except:
            return Execution(Commande[0])
    elif (Commande[0] == 'O'):
        if Commande[1:].strip() in {'G', 'D'} :
            return Execution(Commande[0], Commande[1:].strip())
        else:
            return Execution(Commande[0]) # par défault on tourne a gauche
    elif Commande[0] in {'B', 'L'}:
        return Execution(Commande[0])
    else:
        return _EXECUTION_IMPOSSIBLE

#Read_Prgm('Pailleux')

#chrono = machine.Timer.Chrono()

def Read_Prgm(Prgm_Indice):
    #Prgm_Indice = int('{}'.format(Prgm_Indice))
    if ARRET_URGENCE() == 1:# Si le capteur d'ouverture capot n'est pas en place on ne lance pas le programme
        return 1
    m.get_statut_PIC()
    if m.Etat == 'Bloquer Définitivement':
        print("Le mirobot n'est pas disponible à executer des commandes")
        return 0 #on autorise pas le prochain départ
    _Prgm_Indice = Prgm_Indice
    try:
        with open('/flash/prgm/{}.txt'.format(_Prgm_Indice)) as Fichier:
            try:
                m.Run_Prgm = 1 #on déclare le mirobot en instance d'execution de programme
                for ligne in Fichier:
                    print(ligne)
                    Resultat=_EXECUTION_IMPOSSIBLE
                    try:
                        ligne = ligne.split('#')[0]
                        if len(ligne)>0:
                            if ligne[0] in {'A', 'R', 'P', 'D', 'E', 'I', 'M', 'B', 'L', 'O', 'S'}:
                                if m.Run_Prgm == 1:
                                    #Chrono Start
                                    # m.chrono.start()
                                    Resultat=Cmd_Execution(ligne)
                                    # m.chrono.stop()
                                    # m.Nb_Seconde_Fonctionnement += m.chrono.read()
                                    # m.Nb_Seconde_Maintenance += m.chrono.read()
                                    # nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
                                    # nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
                                    #m.Chrono_Store(Fonctionnement=m.Nb_Seconde_Fonctionnement, Maintenance=m.Nb_Seconde_Maintenance)
                                else:
                                    Resultat=_EXECUTION_IMPOSSIBLE
                            else:
                                Resultat=_EXECUTION_IMPOSSIBLE
                        # else:
                        #     Resultat=_EXECUTION_IMPOSSIBLE
                    except:
                        pass
                    if Resultat == _EXECUTION_ERREUR:
                        #print("Erreur d'execution du programme on sort de tout")
                        raise MonException("Erreur d'execution du programme on sort de tout")
            except:
                print("Erreur de fonctionnement => lecture du programme abandonné")
                if (_Prgm_Indice!= 'Retour') and (m.Run_Prgm == 1):
                    print("Tentative de retour")
                    m.PIC_SEND('e\x00') # RAZ du robot
                    Resultat_Execution = Read_Prgm('Retour')
                    if Resultat_Execution == 1:
                        print("Le mirobot a réussi a effectuer son retour")
                        m.Run_Prgm = 0
                        return 1 #on autorise le prochain départ
                    else:
                        print("Le mirobot n'a pas réussi à rentré")
                        #m.PIC_SEND('e\x4D') # Etat bloquer definitivement
                        #m.alarme()
                        Alarme()
                        m.Run_Prgm = 0
                        return 0 #on autorise pas le prochain départ
                else:
                    m.Run_Prgm = 0
                    return 0 #on autorise pas le prochain départ (car on était justement en train d'effectuer le retour)
    except:
        print("Erreur de lecture du programme")
    m.Run_Prgm = 0
    return 1

#Write_Prgm(5, 'A\nL\nR\nB\n')
#def Write_Prgm(Data_From_Socket):
def Write_Prgm(Prgm_Indice, Data_From_Socket):
    #Data_From_Socket = Data_From_Socket.split(':')
    #Prgm_Indice = Data_From_Socket[0]
    #Data_From_Socket = Data_From_Socket[1:]
    if Prgm_Indice in {'r', 'R', 'Retour'}:
        Prgm_Indice = 'Retour'
    with open('/flash/prgm/{}.txt'.format(Prgm_Indice), 'w') as Fichier:
        Fichier.write(Data_From_Socket)

#Send_Prgm('1')
#def Write_Prgm(Data_From_Socket):
def Send_Prgm(Prgm_Indice):
    #Data_From_Socket = Data_From_Socket.split(':')
    #Prgm_Indice = Data_From_Socket[0]
    #Data_From_Socket = Data_From_Socket[1:]
    if Prgm_Indice in{'r', 'R'}:
        Prgm_Indice = 'Retour'
    try:
        with open('/flash/prgm/{}.txt'.format(Prgm_Indice)) as Fichier:
            return Fichier.read()
    except:
        return '\n'

def Interrupteur(Activation=0):
    m.PIC_SEND('R{}'.format(1 if Activation==1 else 0))
    return _EXECUTION_OK


def Avance(Pion=0):
    m.PIC_PARAM_UPDATE()
    m.chrono.start()
    m.avance(Reset=1, Nb_Pion=Pion)
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    m.chrono.stop()
    m.Nb_Seconde_Fonctionnement += m.chrono.read()
    m.Nb_Seconde_Maintenance += m.chrono.read()
    m.chrono.reset()
    nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
    nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR


def Recule(Pion=0):
    m.PIC_PARAM_UPDATE()
    m.chrono.start()
    m.recule(Reset=1, Nb_Pion=Pion)
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    m.chrono.stop()
    m.Nb_Seconde_Fonctionnement += m.chrono.read()
    m.Nb_Seconde_Maintenance += m.chrono.read()
    m.chrono.reset()
    nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
    nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR

def Pailleux(Pion=4):
    m.PIC_PARAM_UPDATE()
    if Avance(Pion=Pion) and m.Run_Prgm == 1:
        m.get_statut_PIC()
        if m.Etat == 'Platine':
            return _EXECUTION_OK
        if Pelle_Leve() and m.Run_Prgm == 1:
            #m.recule(Reset=1, Nb_Seconde=30)
            nb_seconde_max_avant_defaut = 60 #180 minutes
            m.chrono.start()
            m.recule(Reset=1, Nb_Seconde=7, option_triple=1, option_pailleux=1)
            #m.recule(Reset=1, Nb_Seconde=10, option_triple=1)
            while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                nb_seconde_max_avant_defaut -= 1
                time.sleep(1)
            m.chrono.stop()
            m.Nb_Seconde_Fonctionnement += m.chrono.read()
            m.Nb_Seconde_Maintenance += m.chrono.read()
            m.chrono.reset()
            nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
            nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
            if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                if Pelle_Baisse()!=1 and m.Run_Prgm == 0:
                    return _EXECUTION_ERREUR
                # if Pelle_Baisse():
                #
                # else:
                #     return _EXECUTION_ERREUR
            else:
                return _EXECUTION_ERREUR
        else:
            return _EXECUTION_ERREUR
    else:
        return _EXECUTION_ERREUR
    m.get_statut_PIC()
    while 1:
        if Avance(Pion=Pion+1) and m.Run_Prgm == 1:
            m.get_statut_PIC()
            if m.Etat == 'Platine':
                return _EXECUTION_OK
            elif m.Etat == 'ALARME':
                return _EXECUTION_ERREUR
            if Pelle_Leve() and m.Run_Prgm == 1:
                nb_seconde_max_avant_defaut = 60 #180 minutes
                m.chrono.start()
                m.recule(Reset=1, Nb_Seconde=7, option_triple=1, option_pailleux=1)
                #m.recule(Reset=1, Nb_Seconde=10, option_triple=1)
                while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                    nb_seconde_max_avant_defaut -= 1
                    time.sleep(1)
                m.chrono.stop()
                m.Nb_Seconde_Fonctionnement += m.chrono.read()
                m.Nb_Seconde_Maintenance += m.chrono.read()
                m.chrono.reset()
                nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
                nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
                if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                    if Pelle_Baisse()!=1 and m.Run_Prgm == 0:
                        return _EXECUTION_ERREUR
                    # if Pelle_Baisse():
                    #
                    # else:
                    #     return _EXECUTION_ERREUR
                else:
                    return _EXECUTION_ERREUR
            else:
                return _EXECUTION_ERREUR
        else:
            return _EXECUTION_ERREUR





def DVT_recule(Seconde=4):
    m.PIC_PARAM_UPDATE()
    m.chrono.start()
    m.recule(Reset=1, Nb_Seconde=Seconde)
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    m.chrono.stop()
    m.Nb_Seconde_Fonctionnement += m.chrono.read()
    m.Nb_Seconde_Maintenance += m.chrono.read()
    m.chrono.reset()
    nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
    nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR
    #pass



def DVT(Seconde=4):
    m.PIC_PARAM_UPDATE()
    m.chrono.start()
    m.avance(Reset=1, Nb_Seconde=Seconde)
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    m.chrono.stop()
    m.Nb_Seconde_Fonctionnement += m.chrono.read()
    m.Nb_Seconde_Maintenance += m.chrono.read()
    m.chrono.reset()
    nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
    nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR
    #pass

#def Multitas(Patinage=15):
def Multitas(Patinage=150):#Modif du 18 avril
    try:
        if int(Patinage) == 0 :
            Patinage = 150
        Patinage = int(Patinage/10) #Modif du 18 Avril le temps n'est plus en seconde, mais en centaine de milliseconde
        if(Patinage<0) or (Patinage> 25):
            raise MonException("Valeur du Patinage pour le multitas non régulière")
    except:
        Patinage = 15
    m.PIC_PARAM_UPDATE()
    _patinage_temps_s = m.PATINAGE_TEMPS_s # ne semble plus(/pas) nécessaire
    m.PIC_SEND('P1{:03d}'.format(Patinage))
    time.sleep(0.04)
    m.PIC_SEND('P3{:03d}'.format(Patinage*10)) # Modif du 18 avril cf Quentin Temps de détection platine équivalent à celui du patinage (pour les bourrins avec le P5)
    m.chrono.start()
    m.avance(Reset=1, Nb_Pion=0, option_multitas=1)
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy() == _OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    m.chrono.stop()
    m.Nb_Seconde_Fonctionnement += m.chrono.read()
    m.Nb_Seconde_Maintenance += m.chrono.read()
    m.chrono.reset()
    nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
    nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
    m.PIC_PARAM_UPDATE() #on remet les paramètres par defaut
    #refresh_statut()
    m.affiche('Multitas: m.Etat={}, m.Erreur={}, m.Run_Prgm'.format(m.Etat, m.Erreur, m.Run_Prgm))
    m.get_statut_PIC()
    m.affiche('Multitas: m.Etat={}, m.Erreur={}, m.Run_Prgm'.format(m.Etat, m.Erreur, m.Run_Prgm))
    #if m.Etat == 'Platine' or m.Etat == 'Inactif' or (m.Etat == 'Alarme' and m.Erreur == 'Patinage'):
    if m.Etat == 'Platine' or (m.Etat == 'Inactif' and m.Erreur == 'Patinage') and m.Run_Prgm == 1:
    #'Bloquer'
    #if m.Etat in {'Platine', 'Inactif', 'Bloquer'} and m.Run_Prgm == 1:
        time.sleep(0.1)
        if m.Erreur == 'Patinage':
            m.affiche('Multitas => Etat Patinage => OK')
            m.reset()
        else:
            m.affiche('Multitas => Etat Platine => OK')
        return _EXECUTION_OK
    else:
        m.affiche('Multitas => Erreur')
        m.affiche('Multitas: m.Etat={}, m.Erreur={}, m.Run_Prgm'.format(m.Etat, m.Erreur, m.Run_Prgm))
        return _EXECUTION_ERREUR

def Pelle_Baisse():
    m.PIC_PARAM_UPDATE()
    m.baisse_la_pelle()
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR

def Pelle_Leve():
    m.PIC_PARAM_UPDATE()
    m.leve_la_pelle()
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    #time.sleep(1)
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        return _EXECUTION_OK
    else:
        return _EXECUTION_ERREUR

def Orientation(Direction='G'):
    m.PIC_PARAM_UPDATE()
    #Gauche = 0, Droite = 1
    if (Direction == 'G') or (Direction == 0):
        Direction = 'G'
    elif(Direction == 'D') or (Direction == 1):
        Direction = 'D'
    m.sort_la_bequille()
    nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
    while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        nb_seconde_max_avant_defaut -= 1
        time.sleep(1)
    if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
        m.chrono.start()
        if Direction == 'G':
            m.avance(Reset=1, Nb_Seconde=m.Nb_Seconde_Bequille_Mvt)
        else:
            m.recule(Reset=1, Nb_Seconde=m.Nb_Seconde_Bequille_Mvt)
        nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
        while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
            nb_seconde_max_avant_defaut -= 1
            time.sleep(1)
        m.chrono.stop()
        m.Nb_Seconde_Fonctionnement += m.chrono.read()
        m.Nb_Seconde_Maintenance += m.chrono.read()
        m.chrono.reset()
        nvs_set('TPS', int(m.Nb_Seconde_Fonctionnement))
        nvs_set('TMA', int(m.Nb_Seconde_Maintenance))
        if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
            m.rentre_la_bequille()
            nb_seconde_max_avant_defaut = 180 * 60 #180 minutes
            while m.check_busy()==_OCCUPER and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                nb_seconde_max_avant_defaut -= 1
                time.sleep(1)
            if m.libre() == _EXECUTION_OK and nb_seconde_max_avant_defaut > 0 and m.Run_Prgm == 1:
                return _EXECUTION_OK
            else:
                return _EXECUTION_ERREUR
        else:
            return _EXECUTION_ERREUR
    else:
        return _EXECUTION_ERREUR

def Pause(Seconde=4):
    m.PIC_PARAM_UPDATE()
    time.sleep(Seconde)
    return _EXECUTION_OK
