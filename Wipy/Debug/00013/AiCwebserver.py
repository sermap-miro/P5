from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

from machine import RTC
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))


#import AiCwebserver
#AiCwebserver.AiCWebserv()

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(8)">Cycle(Standard)</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(1)">Avant</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(6)">Lever Pelle</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(4)">Sort(Bequille)</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(7)">STOP</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(3)">Rentre(Bequille)</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(9)">Cycle(Retour)</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(2)">Arriere</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(5)">Baisser Pelle</button></div>


def Commande_Manuel(Indice):
    print('Commande Manuel Indice = {}'.format(Indice))
    try:
        Indice = int(Indice)
    except:
        Indice = 0
    exec("Signal_Sonore()")
    if (Indice == 1):
        exec('cycle_standard()')
    elif (Indice == 2):
        exec('m.avance()')
    elif (Indice == 3):
        exec('m.pelle(1)')
    elif (Indice == 4):
        exec('m.sort_la_bequille()')
    elif (Indice == 5):
        exec('m.bloque()')
    elif (Indice == 6):
        exec('m.rentre_la_bequille()')
    elif (Indice == 7):
        exec('cycle_retour()')
    elif (Indice == 8):
        exec('m.recule()')
    elif (Indice == 9):
        exec('m.pelle(0)')


#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(1)">1</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(2)">2</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(3)">3</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(4)">4</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(5)">5</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(6)">6</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(7)">7</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(8)">8</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(9)">9</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(10)">Standard</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(11)">Pailleux</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(12)">DVT</button></div>

#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(13)">MultiTas</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(14)">Retour</button></div>
#    <div class="column small-centered"><button class="button 150px-width" onclick="Send_Command(15)">STOP</button></div>


def Execution_Programme(Indice):
    exec("Signal_Sonore()")
    print('Execution Programme Indice = {}'.format(Indice))
    try:
        Indice = int(Indice)
    except:
        Indice = 0
    if (Indice == 1):
        exec("prgm_planifier = '1';allow_to_fly = 1;")
    elif (Indice == 2):
        exec("prgm_planifier = '2';allow_to_fly = 1;")
    elif (Indice == 3):
        exec("prgm_planifier = '3';allow_to_fly = 1;")
    elif (Indice == 4):
        exec("prgm_planifier = '4';allow_to_fly = 1;")
    elif (Indice == 5):
        exec("prgm_planifier = '5';allow_to_fly = 1;")
    elif (Indice == 6):
        exec("prgm_planifier = '6';allow_to_fly = 1;")
    elif (Indice == 7):
        exec("prgm_planifier = '7';allow_to_fly = 1;")
    elif (Indice == 8):
        exec("prgm_planifier = '8';allow_to_fly = 1;")
    elif (Indice == 9):
        exec("prgm_planifier = '9';allow_to_fly = 1;")
    elif (Indice == 10):
        exec("prgm_planifier = 'Standard';allow_to_fly = 1;")
    elif (Indice == 11):
        exec("prgm_planifier = 'Pailleux';allow_to_fly = 1;")
    elif (Indice == 12):
        exec("prgm_planifier = 'DVT';allow_to_fly = 1;")
    elif (Indice == 13):
        exec("prgm_planifier = 'MultiTas';allow_to_fly = 1;")
    elif (Indice == 14):
        exec("prgm_planifier = 'Retour';allow_to_fly = 1;")
    elif (Indice == 15):
        exec("m.bloque();")



def AiCWebserv():
    import socket
    #import time
    import gc
    #import Lib_Cmd_mirobot as Mirobot
    #Mirobot.pause()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(0)	# just queue up some requests
    Tourne = 1
    while Tourne == 1:
        gc.collect()
        try:
                conn, addr = s.accept()
                request = conn.recv(1024)
                conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: SERMAP\nContent-Type: text/html\n\n')
                request = str(request)
                ib = request.find('Val=')
                ibvp = request.find('Valp=')
                ibe = request.find('Etat')
                ibh = request.find('H=')
                ibs = request.find('Stat')
                ibp = request.find('Prgm')
                ibm = request.find('Manu')
                ibi = request.find('Info')
                ibexit = request.find('xit')
                if ibexit > 0:
                    conn.send(bytes("P5 Web Access Closed", "ascii"))
                    Tourne = 0
                elif ibs > 0 :
                    conn.send(bytes("<p>", "ascii"))
                    #conn.send(bytes("Page Web P5: {}".format(request), "ascii"))
                    conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
                    #conn.send(bytes("<p>", "ascii"))
                elif ibh > 0 :
                    #conn.send(bytes("<p>", "ascii"))
                    #conn.send(bytes("Page Web P5: {}".format(request), "ascii"))

                    ie = request.find(' ', ibh)
                    Val = request[ibh+2:ie]
                    # print('Valp={}'.format(Val))#Mirobot.Commande_List[Val])
                    # print('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
                    # #Mirobot.Execute_Cmd(Val)
                    # Execution_Programme(Val)

                    conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                    try:
                        _h = int(Val)
                        conn.send(bytes("<p>", "ascii"))
                        conn.send(bytes("Mise à jour de l'horloge: Ok", "ascii"))
                        #RTC(datetime=(2018, 9, 25, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                    except:

                        if Val.find(':')>0:
                            try:
                                _h = int(Val.split(':')[0])
                                _m = int(Val.split(':')[1])

                                conn.send(bytes("<p>", "ascii"))
                                conn.send(bytes("Mise à jour de l'horloge: Ok", "ascii"))
                                #RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                            except:

                                _h = 12
                                _m = 00

                                conn.send(bytes("<p>", "ascii"))
                                conn.send(bytes("Mise à jour de l'horloge => Heure par défaut: 12h00", "ascii"))
                                pass
                    RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement

                    conn.send(bytes("<p>", "ascii"))
                    conn.send(bytes('Nouvelle Heure = {}'.format(_h), "ascii"))
                    conn.send(bytes("<p>", "ascii"))
                    conn.send(bytes('Nouvelle Minute = {}'.format(_m), "ascii"))
                    conn.send(bytes("<p>", "ascii"))
                    conn.send(bytes('<a href="http://192.168.4.1/">Menu Principal</a>', "ascii"))
                elif ibe > 0 :
                    conn.send(bytes("<p>", "ascii"))
                    conn.send(bytes("Page Web P5", "ascii"))
                    #conn.send(bytes(Mirobot.entete_HMI(*Mirobot.entete_T3(Entete=Mirobot.get_entete(MIR_ID=MIR_ID, ARM_ID=ARM_ID))), "ascii"))
                    conn.send(bytes("<p>", "ascii"))
                    #conn.send(bytes("Mise au point", "ascii"))
                    conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
                    conn.send(bytes("<p>", "ascii"))
                    #conn.send(bytes("Mise au point", "ascii"))
                    conn.send(bytes('Version PIC: {}'.format(int(m.PIC_ASK('S').split()[-1])), "ascii"))
                    conn.send(bytes("<p>", "ascii"))
                    conn.send(bytes('Version Wipy: {}'.format(m.version), "ascii"))
                    #conn.send(bytes(Mirobot.statut_HMI(*Mirobot.statut_T3(Statut=Mirobot.get_statut(MIR_ID=MIR_ID, ARM_ID=ARM_ID))), "ascii"))
                elif ib > 0 :
                    ie = request.find(' ', ib)
                    Val = request[ib+4:ie]
                    print('Val={}'.format(Val))#Mirobot.Commande_List[Val])
                    #Mirobot.Execute_Cmd(Val)
                    Commande_Manuel(Val)
                    conn.send(Val)
                elif ibvp > 0 :
                    ie = request.find(' ', ibvp)
                    Val = request[ibvp+5:ie]
                    print('Valp={}'.format(Val))#Mirobot.Commande_List[Val])
                    print('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
                    #Mirobot.Execute_Cmd(Val)
                    Execution_Programme(Val)
                    conn.send(Val)
                elif ibp > 0 :
                    print("Rafraîchissement p")
                    try:
                        with open('AiCmirobot_p.htm', 'r') as html:
                            #conn.send(html.read())
                            for line in html.readlines():
                                conn.send(line)
                    except:
                        print("Envoi AiCmirobot_p.htm Failed!")
                elif ibm > 0 :
                    print("Rafraîchissement m")
                    try:
                        with open('AiCmirobot.htm', 'r') as html:
                            #conn.send(html.read())
                            for line in html.readlines():
                                conn.send(line)
                    except:
                        print("Envoi AiCmirobot_p.htm Failed!")
                elif ibi > 0 :
                    print("Rafraîchissement i")
                    try:
                        with open('AiCmirobot_info.htm', 'r') as html:
                            #conn.send(html.read())
                            for line in html.readlines():
                                conn.send(line)
                    except:
                        print("Envoi AiCmirobot_info.htm Failed!")
                else:
                    print("Rafraîchissement Menu Principal")
                    try:
                        #with open('AiCmirobot.htm', 'r') as html:
                        with open('AiCmirobot_menu_principal.htm', 'r') as html:
                            #conn.send(html.read())
                            for line in html.readlines():
                                conn.send(line)
                    except:
                        print("Envoi AiCmirobot_menu_principal.htm Failed!")
                conn.sendall('\n')
                conn.close()
        except:
              pass

#gc.collect()
#AiCWebserv()
