from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

from machine import RTC
from time import localtime, sleep
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))

from planning import planning_save

from commande import Send_Prgm, Write_Prgm

from AiCwebserver_CMD import Extract_Data, Planning_Record, Planning_Print_old, Planning_Print, Commande_Manuel, Execution_Programme, Execution_Calibration

from wifi import wlan

from gc import collect

def AiCWebserv(port):
    import socket
    #import time
    import gc
    #global web_requete_brute, web_requete
    #import Lib_Cmd_mirobot as Mirobot
    #Mirobot.pause()
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.bind(('', 80))
            s.bind(('', port))
            #s.listen(0)	# just queue up some requests
            s.listen(1)	# un seul autorisé
            #s.settimeout(3) # Problème de déconnexion a distance
            Tourne = 1
            _wifi = 0
            _CONVERSION_FACTOR_CAN_2_AMPERE = 5
            Facteur_Conversion_Ampere_2_CAN = 5
            while Tourne == 1:
                gc.collect()
                try:
                        m.web = 'Attente Connexion'
                        m.affiche(m.web)
                        #s.settimeout(1) # Problème de déconnexion a distance
                        conn = None
                        attente = 0
                        while conn is None:
                            conn, addr = s.accept()
                            attente += 1
                            m.web = 'Attente Connexion {}'.format(attente)
                            sleep(0.1)
                        m.web = 'Attente Requete'
                        m.affiche(m.web)
                        try:
                            conn.settimeout(1)
                            request = conn.recv(1024) # Ici semble se situe le problème web/déconnexion
                            conn.settimeout(None)
                            m.web = 'Requete Accept'
                        except:
                            m.web = 'Mauvaise Reception de la Requete'
                            m.web_debug = m.web
                            request = ''
                        #m.web = 'Accept'
                        m.affiche(m.web)
                        #m.web_requete_brute = request
                        conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: SERMAP\nContent-Type: text/html\n\n')
                        #request = str(request)
                        request = str(request.decode('utf8'))
                        #print('Request = {}'.format(request))
                        m.affiche(request)
                        #m.web_requete = request
                        #m.conn = conn
                        try:

                            requete = request[:request.find('HTTP')]
                        except:
                            requete = request
                        ib = requete.find('Val=')
                        ibvp = requete.find('Valp=')
                        ibe = requete.find('Etat')
                        ibh = requete.find('H=')
                        ibs = requete.find('Stat')
                        ibp = requete.find('Prgm')
                        ibm = requete.find('Manu')
                        ibi = requete.find('Info')
                        ibn = requete.find('Plan')
                        ib3 = requete.find('T3')
                        ibc = requete.find('Clock')
                        ibo = requete.find('Conf')
                        ibw = requete.find('Edit')
                        ibf = requete.find('Wifi')
                        ibfavicon = requete.find('favicon')
                        ibcalibration = requete.find('Calibration')
                        ibvc = requete.find('Valc=')
                        ibexit = requete.find('xit')
                        if ibexit > 0:
                            conn.send(bytes("P5 Web Access Closed", "ascii"))
                            Tourne = 0

                        elif ibcalibration > 0 :
                            print("Rafraîchissement calibration")
                            try:
                                with open('AiCmirobot_calibration.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_calibration.htm Failed!")

                        elif ibvc > 0 :
                            ie = request.find(' ', ibvc)
                            Val = request[ibvc+5:ie]
                            m.affiche('Valc={}'.format(Val))#Mirobot.Commande_List[Val])
                            m.affiche('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
                            # print('Valp={}'.format(Val))#Mirobot.Commande_List[Val])
                            # print('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
                            #Mirobot.Execute_Cmd(Val)
                            Execution_Calibration(Val)
                            conn.send(Val)
                        elif ibs > 0 :
                            conn.send(bytes("<p>", "ascii"))
                            #conn.send(bytes("Page Web P5: {}".format(request), "ascii"))
                            conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
                            #conn.send(bytes("<p>", "ascii"))
                        elif ibfavicon > 0 :#http://michaldul.com/python/sendfile/ # https://convertico.com/
                            #adb shell screencap -p /sdcard/screen.png
                            #adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png
                            #print('Favicon')
                            CHUNK_SIZE = 512
                            with open('favicon.ico', 'rb') as ico:
                                data = ico.read(CHUNK_SIZE)
                                while data:
                                    conn.send(bytes(data))
                                    data = ico.read(CHUNK_SIZE)
                                #conn.sendfile(ico, 0)
                            # with open('favicon.ico', 'rb') as ico:
                            #     conn.sendfile(ico, 0)
                            #conn.send(bytes("<p>", "ascii"))
                            #conn.send(bytes("Page Web P5: {}".format(request), "ascii"))
                            #conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
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
                            #conn.send(bytes('<a href="http://192.168.4.1/">Menu Principal</a>', "ascii"))
                            conn.send(bytes('<a href="/">Menu Principal</a>', "ascii"))
                        elif ibe > 0 or ibi > 0:
                            # _CONVERSION_FACTOR_CAN_2_AMPERE = 5
                            #conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))

                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_etat_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_etat_header.htm Failed!")

                            conn.send(bytes("<p>", "ascii"))
                            #conn.send(bytes("Page Web P5", "ascii"))
                            #conn.send(bytes(Mirobot.entete_HMI(*Mirobot.entete_T3(Entete=Mirobot.get_entete(MIR_ID=MIR_ID, ARM_ID=ARM_ID))), "ascii"))
                            conn.send(bytes("<p>", "ascii"))
                            #conn.send(bytes("Mise au point", "ascii"))
                            _statut_brut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name)
                            # #conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
                            # conn.send(bytes("<p>", "ascii"))
                            # #conn.send(bytes("Mise au point", "ascii"))
                            # conn.send(bytes('Version PIC: {}'.format(int(m.PIC_ASK('S').split()[-1])), "ascii"))
                            # conn.send(bytes("<p>", "ascii"))
                            # conn.send(bytes('Version Wipy: {}'.format(m.version), "ascii"))

                            #conn.send(bytes('<p>Etat P5: {}'.format(m.Etat), "ascii"))
                            #conn.send(bytes('<p>Erreur P5: {}'.format(m.Erreur), "ascii"))
                            try:
                                data = _statut_brut.split(' ')
                                _derniere_erreur = m.get_erreur(int(data[2],16))
                                if _derniere_erreur != 'NULL':
                                    conn.send(bytes('<p>Dernière alarme: {}'.format(m.get_erreur(int(data[2],16))), "ascii"))
                                conn.send(bytes('<p>Etat P5: {}'.format(m.get_etat(int(data[0],16))), "ascii"))
                                # self.ids['etat'].text = '{}'.format(m.get_etat_pic(int(data[0],16)))
                                conn.send(bytes('<p>Etat précédent P5: {}'.format(m.get_etat(int(data[1],16))), "ascii"))
                                # self.ids['etat_previous'].text = '{}'.format(m.get_etat_pic(int(data[1],16)))
                                # self.ids['alarme'].text = '{}'.format(m.get_erreur_pic(int(data[2],16)))
                                conn.send(bytes('<p>Pions: {}'.format(int(data[3],16)), "ascii"))

                                conn.send(bytes('<p>Batterie: {} V'.format(data[18]), "ascii"))



                                _etat_pion = int(data[11],16)
                                if _etat_pion == 1:
                                    conn.send(bytes('<p>Capteur pion: <font color="#000000">Metal Absent</font>', "ascii"))
                                else:
                                    conn.send(bytes('<p>Capteur pion: <font color="#0000ff">Metal Présent</font>', "ascii"))
                                _etat_capot = int(data[12],16)
                                if _etat_capot == 1:
                                    conn.send(bytes('<p>Capteur capot: <font color="#00ff00">En place</font>', "ascii"))
                                else:
                                    conn.send(bytes('<p>! Capteur capot: <font size="7" color="#ff0000">! En défaut !</font>', "ascii"))


                                _etat_arret_urgence = int(data[17],16)
                                if _etat_arret_urgence == 1:
                                    conn.send(bytes('<p>! Arrêt Urgence !: <font size="7" color="#ff0000">! En Urgence !</font>', "ascii"))
                                else:
                                    conn.send(bytes('<p>Arrêt Urgence: <font color="#00ff00">Position Normal</font>', "ascii"))


                                _etat_relais = int(data[13],16)
                                if _etat_relais == 1:
                                    conn.send(bytes('<p>Relais: Activé', "ascii"))
                                else:
                                    conn.send(bytes('<p>Relais: Désactivé', "ascii"))





                                # self.ids['nb_pion'].text = '{}'.format(int(data[3],16))
                                conn.send(bytes('<p>i Moteur 1: {}'.format(int(data[4],16)/_CONVERSION_FACTOR_CAN_2_AMPERE), "ascii"))
                                # self.ids['i_Moteur_1'].text = '{}'.format(int(data[4],16)/_CONVERSION_FACTOR_CAN_2_AMPERE)
                                conn.send(bytes('<p>i Moteur 2: {}'.format(int(data[5],16)/_CONVERSION_FACTOR_CAN_2_AMPERE), "ascii"))
                                # self.ids['i_Moteur_2'].text = '{}'.format(int(data[5],16)/_CONVERSION_FACTOR_CAN_2_AMPERE)
                                # #self.ids['consigne'].text = '{}'.format(int(data[6],16)/_CONVERSION_FACTOR_CAN_2_AMPERE)
                                conn.send(bytes('<p>Patinage: {} s'.format(int(data[7],16)), "ascii"))
                                # self.ids['nb_s_patinage'].text = '{}'.format(int(data[7],16))
                                conn.send(bytes('<p>Temps (Pion): {} ms'.format(int(data[8],16)*100), "ascii"))
                                # self.ids['nb_100ms_pion'].text = '{}'.format(int(data[8],16)*100)
                                conn.send(bytes('<p>Temps (Platine): {} ms'.format(int(data[9],16)*100), "ascii"))
                                # self.ids['nb_100ms_platine'].text = '{}'.format(int(data[9],16)*100)
                                conn.send(bytes('<p>Temps pelle: {} s'.format(int(data[10],16)), "ascii"))
                                # self.ids['nb_s_pelle'].text = '{}'.format(int(data[10],16))

                                #m.Nb_Seconde_Fonctionnement
                                #m.Nb_Seconde_Maintenance
                                if m.Nb_Seconde_Fonctionnement < 60:
                                    conn.send(bytes("<p>Temps de vol: {} s".format(m.Nb_Seconde_Fonctionnement), "ascii"))
                                else:
                                    if m.Nb_Seconde_Fonctionnement < 3600:
                                        conn.send(bytes("<p>Temps de vol: {:.2f} s".format(m.Nb_Seconde_Fonctionnement/60), "ascii"))
                                    else:
                                        conn.send(bytes("<p>Temps de vol: {:.2f} s".format(m.Nb_Seconde_Fonctionnement/3600), "ascii"))

                                # if m.Nb_Seconde_Maintenance < 60:
                                #     conn.send(bytes('<p>Dernière maintenance: {} s'.format(m.Nb_Seconde_Maintenance), "ascii"))
                                # else:
                                #     if m.Nb_Seconde_Maintenance < 3600:
                                #         conn.send(bytes('<p>Dernière maintenance: {:.2f} min'.format(m.Nb_Seconde_Maintenance/60), "ascii"))
                                #     else:
                                #         conn.send(bytes('<p>Dernière maintenance: {:.2f} h'.format(m.Nb_Seconde_Maintenance/3600), "ascii"))




                                _Version = ''
                                _Version += '{}'.format(int(data[15],16))
                                _Version += ':{}'.format(data[16])
                                conn.send(bytes('<p>Version: {}'.format(_Version), "ascii"))

                                #conn.send(bytes('<p>Wifi SSID: {}'.format(data[19:]), "ascii"))
                                #conn.send(bytes('<p>Wifi <a href="http://192.168.4.1/Wifi">SSID</a>: {}'.format(m.wifi_name), "ascii"))
                                conn.send(bytes('<p>Wifi <a href="/Wifi">SSID</a>: {}'.format(m.wifi_name), "ascii"))
                                try:
                                    if m.wifi_password != '':
                                        conn.send(bytes('<p>Wifi password: {}'.format(m.wifi_password), "ascii"))
                                except: #il n'y a pas de mot de passe enregistré
                                    pass
                                #from wifi import wlan
                                #print("wlan:")
                                #m.affiche('wlan:')
                                #print('{}'.format(wlan.ifconfig()[0]))
                                #if wlan.ifconfig()[0] != '0.0.0.0': #semble faire mal se rafraichir la page
                                #    conn.send(bytes('<p>Wifi ip: {}'.format(wlan.ifconfig()[0]), "ascii"))
                                conn.send(bytes('<p><p>Version PIC: {}'.format(int(m.PIC_ASK('S').split()[-1])), "ascii"))
                                conn.send(bytes('<p>Version Wipy: {}'.format(m.version), "ascii"))
                            except:
                                pass
                            #conn.send(bytes(Mirobot.statut_HMI(*Mirobot.statut_T3(Statut=Mirobot.get_statut(MIR_ID=MIR_ID, ARM_ID=ARM_ID))), "ascii"))
                        elif ib > 0 :
                            ie = request.find(' ', ib)
                            Val = request[ib+4:ie]
                            #print('Val={}'.format(Val))#Mirobot.Commande_List[Val])
                            m.affiche('Val={}'.format(Val))#Mirobot.Commande_List[Val])
                            #Mirobot.Execute_Cmd(Val)
                            Commande_Manuel(Val)
                            conn.send(Val)
                        elif ibvp > 0 :
                            ie = request.find(' ', ibvp)
                            Val = request[ibvp+5:ie]
                            m.affiche('Valp={}'.format(Val))#Mirobot.Commande_List[Val])
                            m.affiche('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
                            # print('Valp={}'.format(Val))#Mirobot.Commande_List[Val])
                            # print('Val {}  Val'.format(Val))#Mirobot.Commande_List[Val])
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
                        elif ib3 > 0 :
                            if request[0:4]=='POST':
                                print("POST Ok")
                            else:
                                print("POST ABSENT = > GET? = {}".format(request[0:2]))
                            conn.send(bytes("<p>", "ascii"))
                            #conn.send(bytes("Page Web P5: {}".format(request), "ascii"))
                            #conn.send(bytes('T3Plan\n', "ascii"))
                            #conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                            m.requete=request
                            Planning_Record(request=m.requete)

                            #conn.send(bytes("<p>", "ascii"))
                            #On affiche aussi le planning
                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_planning_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_planning_header.htm Failed!")

                            m.affiche("Avant Appel Planning_Print")
                            Planning_Print(conn)
                            m.affiche("Après Appel Planning_Print")


                            conn.send(bytes('</form></body></html>', "ascii"))

                        elif ibn > 0 :
                            m.affiche('Web Request={}'.format(request))
                            #request=request.decode('utf8')
                            #m.affiche('Web Request={}'.format(request))
                            #print(type(request))
                            print("Rafraîchissement n")
                            if request[0:3]=='GET':
                                print("GET Ok")
                            else:
                                print("GET ABSENT = > POST? = {}".format(request[0:2]))


                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_planning_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_planning_header.htm Failed!")

                            m.affiche("Avant Appel Planning_Print")
                            Planning_Print(conn)
                            m.affiche("Après Appel Planning_Print")


                            conn.send(bytes('</form></body></html>', "ascii"))
                            # try:
                            #     with open('AiCmirobot_planning.htm', 'r') as html:
                            #         #conn.send(html.read())
                            #         for line in html.readlines():
                            #             conn.send(line)
                            # except:
                            #     print("Envoi AiCmirobot_planning.htm Failed!")


                            #request=request.decode('utf8')
                            #request=request.encode('utf8')
                            #m.affiche('Web Request={}'.format(request))
                            #print("Rafraîchissement n")
                        #    _heure_actuelle = time.localtime()
                        #     _d = _heure_actuelle
                        #     data = 'set_date(annee={},mois={},jour={},heure={},minute={},seconde={})'.format(_d.tm_year, _d.tm_mon, _d.tm_mday, _d.tm_hour, _d.tm_min, _d.tm_sec)
                        elif ibc > 0 :
                            print("Rafraîchissement clock")
                            _clock_set = 0

                            if request[0:3]!='GET':
                                #print("POST = {}".format(request[0:2]))
                                print("POST = {}".format(request))
                                m.request = request
                                #conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                #conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                                try:
                                    _h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
                                    print('_h={}'.format(_h))
                                    #print('{}:_h={}'.format(_, _h))
                                    _m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
                                    #print('{}:_m={}'.format(_, _m))
                                    print('_m={}'.format(_m))
                                    _clock_set = 1

                                    RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                                except:
                                    pass





                            print("GET Ok")

                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_clock_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_clock_header.htm Failed!")

                            if _clock_set == 1:
                                conn.send(bytes('<p>Horloge mis à jour<p>', "ascii"))


                            conn.send(bytes('<input type="number" name="h1" value="{}" min="0" max="23">'.format(localtime()[3]), "ascii"))
                            conn.send(bytes('<input type="number" name="m1" value="{}" min="0" max="59">'.format(localtime()[4]), "ascii"))
                            #conn.send(bytes('<input type="number" name="m1" value="{}" min="0" max="59" step="5">'.format(localtime()[4]), "ascii"))

                            conn.send(bytes('</form></body></html>', "ascii"))
                            #else:
                                # print("GET ABSENT = > POST? = {}".format(request[0:2]))
                                # conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                # conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                                # try:
                                #     _h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
                                #     print('{}:_h={}'.format(_, _h))
                                #     _m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
                                #     print('{}:_m={}'.format(_, _m))
                                #
                                #     RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                                # except:
                                #     pass
                                # from machine import RTC
                                # from time import localtime
                                # RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))
                                # RTC(datetime=(1970, 1, 1, 0, 0, 0, 0, None)) # <= cette date permettra ultérieurement
                        elif ibo > 0 : #Configuration
                            print("Rafraîchissement conf")
                            _conf_set = 0
                            _statut_brut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name)
                            data = _statut_brut.split(' ')
                            if request[0:3]!='GET':
                                #print("POST = {}".format(request[0:2]))
                                print("POST = {}".format(request))
                                m.request = request
                                #conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                #conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                                try:


                                    _m = int(float(Extract_Data(_planning_brut=request, _type='m', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
                                    if 0<=_m<=255:
                                        m.Moteur_X_Consigne = _m
                                    _c = int(float(Extract_Data(_planning_brut=request, _type='c', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
                                    if 0<=_c<=255:
                                        m.Moteur_Z_Consigne = _c
                                    _s = int(float(Extract_Data(_planning_brut=request, _type='s', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
                                    if 0<=_s<=255:
                                        m.Moteur_Z_Limite_Courant = _s
                                    _b = int(float(Extract_Data(_planning_brut=request, _type='b', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
                                    if 0<=_b<=255:
                                        m.Moteur_Bequille_Consigne = _b

                                    _p = int(float(Extract_Data(_planning_brut=request, _type='p', _indice=1)))
                                    if 0<=_p<=255:
                                        m.PATINAGE_TEMPS_s = _p
                                    _i = int(float(Extract_Data(_planning_brut=request, _type='i', _indice=1))) / 100
                                    if 0<=_i<=255:
                                        m.PION_TEMPS_100ms = _i
                                    _l = int(float(Extract_Data(_planning_brut=request, _type='l', _indice=1))) / 100
                                    if 0<=_l<=255:
                                        m.PLATINE_TEMPS_100ms = _l
                                    _e = int(float(Extract_Data(_planning_brut=request, _type='e', _indice=1)))
                                    if 0<=_e<=255:
                                        m.Nb_Seconde_Pelle = _e
                                    # print('_h={}'.format(_h))
                                    # #print('{}:_h={}'.format(_, _h))
                                    # _m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
                                    # #print('{}:_m={}'.format(_, _m))
                                    # print('_m={}'.format(_m))
                                    # _clock_set = 1
                                    #
                                    # RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement

                                    _conf_set = 1
                                    m.PARAM_STORE()
                                    m.PIC_PARAM_UPDATE()
                                except:
                                    pass





                            print("GET Ok")

                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_conf_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_conf_header.htm Failed!")

                            if _conf_set == 1:
                                conn.send(bytes('<p>Configuration mis à jour<p>', "ascii"))

                            # conn.send(bytes('<p>Patinage (s): {}'.format(int(data[7],16)), "ascii"))
                            # conn.send(bytes('<p>Temps (Pion) (ms): {}'.format(int(data[8],16)*100), "ascii"))
                            # conn.send(bytes('<p>Temps (Platine) (ms): {}'.format(int(data[9],16)*100), "ascii"))
                            # conn.send(bytes('<p>Temps pelle (s): {}'.format(int(data[10],16)), "ascii"))

                            conn.send(bytes('<p>Consigne Moteur (A):<input type="number" name="m1" value="{}" min="0" max="50">'.format(m.Moteur_X_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))
                            conn.send(bytes('<p>Consigne Pelle (A):<input type="number" name="c1" value="{}" min="0" max="50">'.format(m.Moteur_Z_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))
                            conn.send(bytes('<p>Seuil Pelle (A):<input type="number" name="s1" value="{}" min="0" max="50">'.format(m.Moteur_Z_Limite_Courant/Facteur_Conversion_Ampere_2_CAN), "ascii"))
                            conn.send(bytes('<p>Consigne Bequille (A):<input type="number" name="b1" value="{}" min="0" max="50">'.format(m.Moteur_Bequille_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))

                            conn.send(bytes('<p>Patinage (s):<input type="number" name="p1" value="{}" min="0" max="500">'.format(int(data[7],16)), "ascii"))
                            conn.send(bytes('<p>Temps (Pion) (ms):<input type="number" name="i1" value="{}" min="0" max="3000">'.format(int(data[8],16)*100), "ascii"))
                            conn.send(bytes('<p>Temps (Platine) (ms):<input type="number" name="l1" value="{}" min="0" max="5000">'.format(int(data[9],16)*100), "ascii"))
                            conn.send(bytes('<p>Temps pelle (s):<input type="number" name="e1" value="{}" min="0" max="600">'.format(int(data[10],16)), "ascii"))

                            conn.send(bytes('</form></body></html>', "ascii"))
                            #else:
                                # print("GET ABSENT = > POST? = {}".format(request[0:2]))
                                # conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                # conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                                # try:
                                #     _h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
                                #     print('{}:_h={}'.format(_, _h))
                                #     _m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
                                #     print('{}:_m={}'.format(_, _m))
                                #
                                #     RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                                # except:
                                #     pass
                                # from machine import RTC
                                # from time import localtime
                                # RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))
                                # RTC(datetime=(1970, 1, 1, 0, 0, 0, 0, None)) # <= cette date permettra ultérieurement

                        elif ibm > 0 :
                            print("Rafraîchissement m")
                            try:
                                with open('AiCmirobot.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_p.htm Failed!")
                        # elif ibi > 0 :
                        #     print("Rafraîchissement i")
                        #
                        #     # if request[0:3]!='GET':
                        #     #     _nom = int(Extract_Data(_planning_brut=request, _type='n', _indice=1))
                        #
                        #     try:
                        #         with open('AiCmirobot_info.htm', 'r') as html:
                        #             #conn.send(html.read())
                        #             for line in html.readlines():
                        #                 conn.send(line)
                        #     except:
                        #         print("Envoi AiCmirobot_info.htm Failed!")
                        elif ibf > 0 :
                            _wifi=0
                            print("Rafraîchissement f")

                            if request[0:3]!='GET':
                                #m.request = request
                                print('request = {}'.format(request))
                                #_nom = 'unitialized'
                                conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                #conn.send(bytes('<p>nouveau nom = {}'.format(_nom), "ascii"))
                                #_wifi_reset = True if _planning_brut.find('&c1=')>0 else False
                                _wifi_name = Extract_Data(_planning_brut=request, _type='n', _indice=1)
                                _wifi_password = Extract_Data(_planning_brut=request, _type='p', _indice=1)
                                print('nom = {}'.format(_wifi_name))
                                print('password = {}'.format(_wifi_password))
                                if len(_wifi_name)>0:
                                    conn.send(bytes('<p>Se connecter au réseau "P5 - {}"'.format(_wifi_name), "ascii"))
                                else:
                                    conn.send(bytes('<p>Se connecter au réseau "P5" (accès libre)'.format(), "ascii"))
                                if len(_wifi_password)!=0:
                                    conn.send(bytes('<p>Mot de passe "{}"'.format(_wifi_password), "ascii"))
                                #conn.send(bytes('<p><a href="http://192.168.4.1/">Menu Principal</a>', "ascii"))
                                conn.send(bytes('<p><a href="/">Menu Principal</a>', "ascii"))
                                _wifi=1
                                conn.sendall('\n')
                                conn.close()
                                sleep(2)
                                #if _wifi_reset == False:
                                if len(_wifi_name) > 0:
                                    exec('wifi_nom = "{}"'.format(_wifi_name))
                                    with open("/flash/wifi_name.txt", "w+") as _f: _f.write('{}'.format(_wifi_name))
                                    with open("/flash/wifi_password.txt", "w+") as _f: _f.write('{}'.format(_wifi_password))
                                    exec('m.wifi_name = "P5 - {}"'.format(_wifi_name))
                                    exec('m.wifi_password = "{}"'.format(_wifi_password))
                                    #exec('Wifi_Init(_Nom_Wifi=m.wifi_name)')
                                else:
                                    #from uos import remove
                                    print('Wifi name = ""')
                                    with open("/flash/wifi_name.txt", "w+") as _f: _f.write('')
                                    exec('m.wifi_name = "P5"')
                                    exec('m.wifi_password = ""')
                                    #remove("/flash/wifi_name.txt")
                                #print('Wifi_Local()')
                                exec('Wifi_Local()')

                            else:
                                try:
                                    with open('AiCmirobot_wifi.htm', 'r') as html:
                                        #conn.send(html.read())
                                        for line in html.readlines():
                                            conn.send(line)
                                except:
                                    print("Envoi AiCmirobot_wifi.htm Failed!")
                        elif ibw > 0 :
                            _error = 0
                            print("Rafraîchissement Edit")

                            if request[0:3]!='GET':
                                print("GET ABSENT = > POST? = {}".format(request[0:2]))
                                #conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                                #conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))
                                try:
                                    #pass
                                    # _h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
                                    # print('{}:_h={}'.format(_, _h))
                                    # _m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
                                    # print('{}:_m={}'.format(_, _m))
                                    #
                                    # RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
                                    data = Extract_Data(_planning_brut=request, _type='d', _indice=1)
                                    _Prgm_Indice = Extract_Data(_planning_brut=request, _type='p', _indice=1)
                                    _type = Extract_Data(_planning_brut=request, _type='s', _indice=1)
                                    data = data.replace('%0A', '\n')
                                    data = data.replace('%0D', '\r')
                                    #m.data=data
                                    if _type == 'W':
                                        print('Write_Prgm({},{})'.format(_Prgm_Indice, data))
                                        try:
                                            Write_Prgm(_Prgm_Indice,data)
                                        except:
                                            _error = 1
                                            pass
                                    else:
                                        print('Voir({})'.format(_Prgm_Indice))
                                    #Write_Prgm(_Prgm_Indice, data)
                                    _prgm = _Prgm_Indice
                                except:
                                    pass
                            else:

                                _prgm ='1'




                            print("GET Ok")

                            try:
                                with open('AiCmirobot_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_header.htm Failed!")

                            try:
                                with open('AiCmirobot_edit_header.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_edit_header.htm Failed!")

                            # conn.send(bytes('<input type="number" name="h1" value="{}" min="0" max="23">'.format(localtime()[3]), "ascii"))
                            # conn.send(bytes('<input type="number" name="m1" value="{}" min="0" max="59" step="5">'.format(localtime()[4]), "ascii"))


                            if _error > 0:
                                conn.send(bytes("<p>Erreur lors de l'écriture du programme", "ascii"))
                            #conn.send(bytes('<p>Request (type={}) = {}'.format(type(request), request), "ascii"))

                            conn.send(bytes('<p><SELECT name="p1" size="1">', "ascii"))
                            for _option in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'Retour'):
                                conn.send(bytes('<OPTION{}>{}</OPTION>\n'.format('' if _option!=_prgm else ' selected=""', _option), "ascii"))

                            conn.send(bytes('</SELECT>\n', "ascii"))
                            conn.send(bytes('<p><TEXTAREA name="d1" rows=20 cols=80>', "ascii"))
                            conn.send(bytes('{}'.format(Send_Prgm(_prgm)), "ascii"))
                            conn.send(bytes('</TEXTAREA>', "ascii"))




                            conn.send(bytes('</form></body></html>', "ascii"))

                        else:
                            print("Rafraîchissement Menu Principal")
                            try:
                                #with open('AiCmirobot.htm', 'r') as html:
                                with open('AiCmirobot_menu_principal_begin.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_menu_principal_begin.htm Failed!")

                            conn.send(bytes('<H1><center>{}</center></H1>'.format(m.wifi_name), "ascii"))
                            try:
                                #with open('AiCmirobot.htm', 'r') as html:
                                with open('AiCmirobot_menu_principal_end.htm', 'r') as html:
                                    #conn.send(html.read())
                                    for line in html.readlines():
                                        conn.send(line)
                            except:
                                print("Envoi AiCmirobot_menu_principal_end.htm Failed!")



                        if _wifi==0:
                            conn.sendall('\n')
                            conn.close()
                        else:
                            _wifi=0

                except:
                      m.web = 'Except Reception'
                      m.affiche(m.web)
                      conn.close()
                      pass
                finally:
                      collect()

        except:
            m.web = 'Except Bind'
            m.affiche(m.web)
            m.web_debug = m.web # ne devrait pas arriver en théorie
            pass

        finally:
            sleep(1)

#gc.collect()
#AiCWebserv()
