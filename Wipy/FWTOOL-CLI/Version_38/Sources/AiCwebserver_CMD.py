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
    try:
        _cellule_rechercher = '{}{}='.format(_type, _indice)
        recherche_debut = _planning_brut.find(_cellule_rechercher)
        if recherche_debut >= 0:
            _planning_brut = _planning_brut[recherche_debut+len(_cellule_rechercher):]
            recherche_fin = _planning_brut.find('&')
            if recherche_fin > 0 :
                _planning_brut = _planning_brut[0:recherche_fin]
            else:
                _planning_brut = _planning_brut[0:]
            if _planning_brut[0] == '&':
                return ('')
            else:
                return(_planning_brut)
        else:
            return ('')
    except:
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
        m.bug_michel = request
        for _ in range(20):
            try:
                #print('erreur: {} => _a={},_h={},_m={},_p={}'.format(_,_activation, _h, _m, _prgm))
                print('data a extraire = {}'.format(_))
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
            except Exception as Erreur:
                _Erreur = 1
                print('erreur: {} => _a={},_h={},_m={},_p={}'.format(_,_activation, _h, _m, _prgm))
                print('erreur = {}'.format(Erreur)) # Erreur
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
                        conn.send(bytes('<tr>', "ascii"))
                        conn.send(bytes('<th scope="col">{0:02}</th>'.format(_+1), "ascii"))
                        conn.send(bytes('<th scope="col"><input type="number" name="h{0}" value="{1}" min="0" max="23"></th>'.format(_+1, _h), "ascii"))
                        conn.send(bytes('<th scope="col"><input type="number" name="m{0}" value="{1}" min="0" max="59"></th>'.format(_+1, _m), "ascii"))
                        conn.send(bytes('<th scope="col"><input type="checkbox" id="v{0}" name="c{0}"{1}/></th>'.format(_+1, '' if _activation==False else ' checked'), "ascii"))
                        conn.send(bytes('<th scope="col"><SELECT name="p{0}" size="1">'.format(_+1), "ascii"))
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

                        conn.send(bytes('</SELECT></th>', "ascii"))
                        conn.send(bytes('</tr>', "ascii"))
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
