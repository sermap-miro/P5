from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

from machine import RTC
from time import localtime, sleep
# RTC(datetime=(2017, 12, 13, 17, 14, 50, 0, None))

from planning import planning_save

from commande import Send_Prgm, Write_Prgm

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
        _Erreur = 0
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
        if _Erreur == 0:
            planning_save(_planning)
            exec('planning = planning_get()')
    except:
        pass

def Planning_Print_old(conn):
    m.affiche('Planning_Print planning.txt not exist')
    for _ in range(20):
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


def Planning_Print(conn):
    Fichier_Depart = 'planning.txt'
    m.affiche('Planning_Print2')
    _nombre_element_fichier_sauvegarde = 4
    m.affiche('Planning_Print3')
    #_planning = list()
    if True:
        m.affiche('Planning_Print planning.txt exist')
        with open('/flash/'+Fichier_Depart, 'r') as fichier_depart:
            _=0
            for depart in fichier_depart:
                depart=depart.strip()
                depart=depart.split(':')
                if len(depart)==_nombre_element_fichier_sauvegarde:
                    try:
                        _activation= True if ((depart[0]=='True') or (depart[0]=='1')) else False
                        _h = int(depart[1])
                        _m = int(depart[2])
                        _prgm = depart[3]
                        m.affiche("Envoi conn.send {} {} {} {}".format(_activation, _h, _m, _prgm))
                        conn.send(bytes('<tr>', "ascii"))
                        conn.send(bytes('<th scope="col">{0:02}</th>'.format(_+1), "ascii"))
                        conn.send(bytes('<th scope="col"><input class="case_1" type="number" name="h{0}" value="{1}" min="0" max="23" size="2"></th>'.format(_+1, _h), "ascii"))
                        conn.send(bytes('<th scope="col"><input class="case_1" type="number" name="m{0}" value="{1}" min="0" max="59" size="2"></th>'.format(_+1, _m), "ascii"))
                        conn.send(bytes('<th scope="col"><input type="checkbox" id="v{0}" name="c{0}"{1}/></th>'.format(_+1, '' if _activation==False else ' checked'), "ascii"))
                        conn.send(bytes('<th scope="col"><SELECT name="p{0}" size="1">'.format(_+1), "ascii"))
                        for _option in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'Standard', 'Pailleux', 'DVT', 'MultiTas'):
                            conn.send(bytes('<OPTION{}>{}</OPTION>'.format('' if _option!=_prgm else ' selected=""', _option), "ascii"))
                        conn.send(bytes('</SELECT></th>', "ascii"))
                        conn.send(bytes('</tr>', "ascii"))
                        _+=1
                    except:
                        pass
            conn.send(bytes('</tbody></table></form></div></div></div></main>', "ascii"))    

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
    
    
def Print_HTM(the_file,conn):
    try:
        with open(the_file, 'r') as html:
            for line in html.readlines():
                conn.send(bytes(line,"ascii"))
                m.affiche(line)
    except:
        print("Envoi {0} Failed!".format(the_file))
