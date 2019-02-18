from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

from machine import RTC
from time import localtime, sleep
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))

from planning import planning_save

from commande import Send_Prgm, Write_Prgm
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

# False:06:45:Standard
# True:14:25:8
# False:19:50:5
# False:08:10:2
# True:18:15:Pailleux
# True:20:30:DVT
# False:00:00:1
# False:00:00:1
# T3PlanRequest = b'POST /T3Plan HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://192.168.4.1/Plan\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 344\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\nh1=4&m1=0&c1=on&p1=1&h2=0&m2=4&p2=1&h3=0&m3=0&p3=1&h4=0&m4=0&c4=on&p4=1&h5=0&m5=0&p5=1&h6=0&m6=0&p6=1&h7=0&m7=0&p7=1&h8=0&m8=0&p8=1&h9=0&m9=0&p9=1&h10=0&m10=0&p10=1&h11=0&m11=0&p11=1&h12=0&m12=0&p12=1&h13=0&m13=0&p13=1&h14=0&m14=0&p14=1&h15=0&m15=0&p15=1&h16=0&m16=0&p16=1&h17=0&m17=0&p17=1&h18=0&m18=0&p18=1&h19=0&m19=0&p19=1&h20=0&m20=0&p20=1'
# #def planning_save(planning):
# def planning_save(planning):
#     #global planning
#     #on supprimer le fichier existant
#     Fichier_Depart = 'planning.txt'
#     if Fichier_Depart in uos.listdir('/flash'):
#         uos.remove('/flash/'+Fichier_Depart)
#     for depart in planning:
#         print(depart)
#         fichier_depart = open('/flash/'+Fichier_Depart, 'a')
#         #fichier_depart.write(depart+'\n')
#         fichier_depart.write('{}:{}:{}\n'.format(depart[1],depart[0],depart[2]))
#         fichier_depart.close()


# from AiCWebserver import Extract_Data, Planning_Record
# Planning_Record(str('POST /T3Plan HTTP/1.1 Host: 192.168.4.1 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3 Accept-Encoding: gzip, deflate Referer: http://192.168.4.1/Plan Content-Type: application/x-www-form-urlencoded Content-Length: 376 Connection: keep-alive Upgrade-Insecure-Requests: 1 h1=6&m1=45&p1=Standard&h2=14&m2=25&c2=on&p2=8&h3=19&m3=50&p3=5&h4=8&m4=10&p4=2&h5=18&m5=15&c5=on&p5=Pailleux&h6=20&m6=30&c6=on&p6=DVT&h7=0&m7=0&p7=1&h8=0&m8=0&p8=1&h9=0&m9=0&p9=1&h10=0&m10=0&p10=1&h11=0&m11=0&p11=1&h12=0&m12=0&p12=1&h13=0&m13=0&p13=1&h14=0&m14=0&p14=1&h15=0&m15=0&p15=1&h16=0&m16=0&p16=1&h17=0&m17=0&p17=1&h18=0&m18=0&p18=1&h19=0&m19=0&p19=1&h20=0&m20=0&p20=1'))

# Planning_Record(m.requete)

def Extract_Data(_planning_brut='', _type='h', _indice=1):
    _cellule_rechercher = '{}{}='.format(_type, _indice)
    recherche_debut = _planning_brut.find(_cellule_rechercher)
    if recherche_debut >= 0:
        _planning_brut = _planning_brut[recherche_debut+len(_cellule_rechercher):]
        recherche_fin = _planning_brut.find('&')
        if recherche_fin > 0 :
            _planning_brut = _planning_brut[0:recherche_fin]
        else:
            _planning_brut = _planning_brut[0:]

        return(_planning_brut)
    else:
        return ('')

def Planning_Record(request=''):
    _planning = list()
    try:
        ibe = request.find('h1=')
        _planning_brut = request[ibe:]
        #_planning_brut = request[ibe+4:]
        _Erreur = 0
        #_planning = list()
        #_Fichier_Planning_Data = ''
        for _ in range(20):
            try:
                _activation = True if _planning_brut.find('&c{0}='.format(_+1))>0 else False
                print('{}:_a={}'.format(_,_activation))
                _h = int(Extract_Data(_planning_brut=_planning_brut, _type='h', _indice=_+1))
                print('{}:_h={}'.format(_, _h))
                _m = int(Extract_Data(_planning_brut=_planning_brut, _type='m', _indice=_+1))
                print('{}:_m={}'.format(_, _m))
                _prgm = Extract_Data(_planning_brut=_planning_brut, _type='p', _indice=_+1)
                #m.affiche('')
                _planning.append((str(_h)+':'+str(_m), _activation, '{}'.format(_prgm)))
                print('{}:_a={},_h={},_m={},_p={}'.format(_,_activation, _h, _m, _prgm))
            except:
                _Erreur = 1
                print('erreur: {} => _a={},_h={},_m={},_p={}'.format(_,_activation, _h, _m, _prgm))
                pass
        #exec('planning = planning_get()')
        if _Erreur == 0:
            planning_save(_planning)
            exec('planning = planning_get()')
    except:
        pass

    # try:
    #     with open('AiCmirobot_header.htm', 'r') as html:
    #         #conn.send(html.read())
    #         for line in html.readlines():
    #             conn.send(line)
    # except:
    #     print("Envoi AiCmirobot_header.htm Failed!")
    #
    # try:
    #     with open('AiCmirobot_planning_header.htm', 'r') as html:
    #         #conn.send(html.read())
    #         for line in html.readlines():
    #             conn.send(line)
    # except:
    #     print("Envoi AiCmirobot_planning_header.htm Failed!")
    #
    # m.affiche("Avant Appel Planning_Print")
    # Planning_Print(conn)
    # m.affiche("Après Appel Planning_Print")
    #
    #
    # conn.send(bytes('</form></body></html>', "ascii"))



def Planning_Print_old(conn):
    m.affiche('Planning_Print planning.txt not exist')
    for _ in range(20):
        #conn.send(bytes("""
        conn.send(bytes('<div>', "ascii"))
        conn.send(bytes('{0:02}'.format(_+1), "ascii"))
        conn.send(bytes('<input type="number" name="h{0}" value="0" min="0" max="23">'.format(_+1), "ascii"))
        conn.send(bytes('<input type="number" name="m{0}" value="0" min="0" max="59">'.format(_+1), "ascii"))
        conn.send(bytes('<input type="checkbox" id="v{0}" name="c{0}"/>'.format(_+1), "ascii"))
        conn.send(bytes('<SELECT name="p{0}" size="1">'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>1'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>2'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>3'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>4'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>5'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>6'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>7'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>8'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>9'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>Standard'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>Pailleux'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>DVT'.format(_+1), "ascii"))
        conn.send(bytes('<OPTION>MultiTas'.format(_+1), "ascii"))
        conn.send(bytes('</SELECT>'.format(_+1), "ascii"))
        conn.send(bytes('</div>\n'.format(_+1), "ascii"))
        #""".format(_+1), "ascii"))


def Planning_Print(conn):
    # conn.send(bytes('</form></body></html>', "ascii"))
    # m.affiche('Planning_Print')
    # m.affiche('Planning_Print')
    # m.affiche('Planning_Print')
    # m.affiche('Planning_Print')
    # m.affiche('Planning_Print')
    # m.affiche('Planning_Print')
    #conn.send(bytes('ABCDEFGHIJ'.format(_+1, _h, _m, _activation, _prgm), "ascii"))
    #conn.send(bytes('Depart Planning_Print', "ascii"))
    Fichier_Depart = 'planning.txt'
    m.affiche('Planning_Print2')
    _nombre_element_fichier_sauvegarde = 4
    m.affiche('Planning_Print3')
    #_planning = list()
    if True:
    # if not Fichier_Depart in uos.listdir('/flash'):
    #     m.affiche('Planning_Print planning.txt not exist')
    #     for _ in range(20):
    #         conn.send(bytes("""
    #         <div>
    #         {0:02}
    #         <input type="number" name="h{0}" value="0" min="0" max="23">
    #         <input type="number" name="m{0}" value="0" min="0" max="59">
    #         <input type="checkbox" id="v{0}" name="c{0}"/>
    #         <SELECT name="p{0}" size="1">
    #         <OPTION>1
    #         <OPTION>2
    #         <OPTION>3
    #         <OPTION>4
    #         <OPTION>5
    #         <OPTION>6
    #         <OPTION>7
    #         <OPTION>8
    #         <OPTION>9
    #         <OPTION>Standard
    #         <OPTION>Pailleux
    #         <OPTION>DVT
    #         <OPTION>MultiTas
    #         </SELECT>
    #         </div>
    #         """.format(_+1), "ascii"))
    #
    # else:
        m.affiche('Planning_Print planning.txt exist')
        with open('/flash/'+Fichier_Depart, 'r') as fichier_depart:
            _=0
            for depart in fichier_depart:
                #d=depart
                #print(depart)
                depart=depart.strip()
                depart=depart.split(':')
                #if len(depart)==4:
                if len(depart)==_nombre_element_fichier_sauvegarde:
                    try:
                        #_activation= int(bool(depart[0]))
                        #_activation= 1 if ((depart[0]=='True') or (depart[0]==1)) else 0
                        _activation= True if ((depart[0]=='True') or (depart[0]=='1')) else False
                        _h = int(depart[1])
                        _m = int(depart[2])
                        _prgm = depart[3]
                        #_planning.append((str(_h)+':'+str(_m), _activation, '{}'.format(_prgm)))
                        m.affiche("Envoi conn.send {} {} {} {}".format(_activation, _h, _m, _prgm))
                        #conn.send(bytes('Dans boucle Planning_Print', "ascii"))
                        #conn.send(bytes("""
                        conn.send(bytes('<div>\n', "ascii"))
                        conn.send(bytes('{0:02}'.format(_+1), "ascii"))
                        conn.send(bytes('<input type="number" name="h{0}" value="{1}" min="0" max="23">'.format(_+1, _h), "ascii"))
                        conn.send(bytes('<input type="number" name="m{0}" value="{1}" min="0" max="59">'.format(_+1, _m), "ascii"))
                        conn.send(bytes('<input type="checkbox" id="v{0}" name="c{0}"{1}/>'.format(_+1, '' if _activation==False else ' checked'), "ascii"))
                        conn.send(bytes('<SELECT name="p{0}" size="1">'.format(_+1), "ascii"))
                        for _option in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'Standard', 'Pailleux', 'DVT', 'MultiTas'):
                            conn.send(bytes('<OPTION{}>{}</OPTION>'.format('' if _option!=_prgm else ' selected=""', _option), "ascii"))
                        # conn.send(bytes('<OPTION>1</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>2</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>3</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION selected="">4</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>5</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>6</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>7</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>8</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>9</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>Standard</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>Pailleux</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>DVT</OPTION>', "ascii"))
                        # conn.send(bytes('<OPTION>MultiTas</OPTION>', "ascii"))

                        conn.send(bytes('</SELECT>', "ascii"))
                        conn.send(bytes('</div>', "ascii"))
                        _+=1
                        #""".format(_+1, _h, _m, _activation, _prgm), "ascii"))

                    except:
                        pass
            #_planning.append(depart.strip())
        #return _planning


#     for _ in range(20):
#         f.write("""
# <div>
# {0:02}
# <input type="number" name="h{0}" value="0" min="0" max="23">
# <input type="number" name="m{0}" value="0" min="0" max="59">
# <input type="checkbox" id="v{0}" name="c{0}"/>
# <SELECT name="p{0}" size="1">
# <OPTION>1
# <OPTION>2
# <OPTION>3
# <OPTION>4
# <OPTION>5
# <OPTION>6
# <OPTION>7
# <OPTION>8
# <OPTION>9
# <OPTION>Standard
# <OPTION>Pailleux
# <OPTION>DVT
# <OPTION>MultiTas
# </SELECT>
# </div>
# """.format(_+1))













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


def Execution_Calibration(Indice):
    exec("Signal_Sonore()")
    #print('Execution Programme Indice = {}'.format(Indice))
    try:
        Indice = int(Indice)
    except:
        Indice = 0
    if (Indice == 1):
        exec("m.batterie_10_v=Batt_Mean(m);m.PARAM_STORE();")
    elif (Indice == 2):
        exec("m.batterie_30_v=Batt_Mean(m);m.PARAM_STORE();")
    elif (Indice == 4):
        exec("m.PIC_LED(1); m.LED(True);m.PIC_SEND('R1');")
    elif (Indice == 5):
        exec("m.PIC_LED(0); m.LED(False);m.PIC_SEND('R0');")
    elif (Indice == 6):
        exec("RTC(datetime=(2018, 1, 1, 0, 0, 0, 0, None))")
    elif (Indice == 3):
        for _ in range (10):
            exec("Signal_Sonore()")
            sleep(0.1)



def AiCWebserv():
    import socket
    #import time
    import gc
    #global web_requete_brute, web_requete
    #import Lib_Cmd_mirobot as Mirobot
    #Mirobot.pause()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(0)	# just queue up some requests
    Tourne = 1
    _wifi = 0
    _CONVERSION_FACTOR_CAN_2_AMPERE = 5
    Facteur_Conversion_Ampere_2_CAN = 5
    while Tourne == 1:
        gc.collect()
        try:
                conn, addr = s.accept()
                request = conn.recv(1024)
                #m.web_requete_brute = request
                conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: SERMAP\nContent-Type: text/html\n\n')
                #request = str(request)
                request = str(request.decode('utf8'))
                #print('Request = {}'.format(request))
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
                    conn.send(bytes('<a href="http://192.168.4.1/">Menu Principal</a>', "ascii"))
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
                        conn.send(bytes('<p>Wifi <a href="http://192.168.4.1/Wifi">SSID</a>: {}'.format(m.wifi_name), "ascii"))

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
                        print('request = {}'.format(request))
                        #_nom = 'unitialized'
                        conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
                        #conn.send(bytes('<p>nouveau nom = {}'.format(_nom), "ascii"))
                        _wifi_name = Extract_Data(_planning_brut=request, _type='n', _indice=1)
                        print('nom = {}'.format(_wifi_name))
                        conn.send(bytes('<p>Se connecter au réseau "= P5 - {}"'.format(_wifi_name), "ascii"))
                        conn.send(bytes('<p><a href="http://192.168.4.1/">Menu Principal</a>', "ascii"))
                        _wifi=1
                        conn.sendall('\n')
                        conn.close()
                        #time.sleep(4)
                        exec('wifi_nom = "{}"'.format(_wifi_name))
                        with open("/flash/wifi_name.txt", "w+") as _f: _f.write('{}'.format(_wifi_name))
                        exec('m.wifi_name = "P5 - {}"'.format(_wifi_name))
                        exec('Wifi_Init(_Nom_Wifi=m.wifi_name)')

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
              pass

#gc.collect()
#AiCWebserv()
