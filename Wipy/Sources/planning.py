# -*- coding: utf-8 -*-

planning = list()
from machine import RTC
import machine

import uos


rtc = machine.RTC()


from machine import Timer
import machine

class Planificateur:


    #def __init__(self, mirobot, sleep_seconde=1, action=None):
    def __init__(self, mirobot):
        """Genere une alarme a la frequence passer en parametre"""
        #self.turn = 0
        #self.action = self.Mirobot_cycle_standard if action is None else action
        self.action = self.Mirobot_start # if action is None else action
        #self.procedure = pass
        #self.tour_a_faire = 50
        # if temps_echantillonnage == 'Infinie':
        #self.alarm = Timer.Alarm(self.Mirobot_start , s=sleep_seconde, periodic=False)
        self.mirobot = mirobot
        self.seconde = 0
        self.activation = 0
        self.allow_to_fly = 0
        #self.__alarm = Timer.Alarm(self.Mirobot_start, s=sleep_seconde, periodic=False)
        # else:
        #     self.tour_a_faire = int(temps_echantillonnage*frequence_echantillonnage)
        #     self.__alarm = Timer.Alarm(self._Clock_ADC_handler, us=int(1e6/frequence_echantillonnage), periodic=True)

    #def start(self, procedure, sleep_seconde=1):
    def start(self, sleep_seconde=1):
        #self.procedure = procedure
        if self.activation == 1:
            self.stop()
        else:
            self.activation = 1
        if sleep_seconde == 0:
            sleep_seconde = 1
        self.seconde = sleep_seconde
        self.alarm = Timer.Alarm(self.action, s=self.seconde, periodic=False)

    def stop(self):
        if self.activation==1:
            self.activation=0
            self.alarm.cancel()
            del(self.alarm)
        #self.__alarm.callaback(None)

    def Mirobot_start(self, alarm):
        #self.mirobot.start()
        #cycle_standard()
        self.allow_to_fly = 1
        #self.procedure()
        self.stop()

    def Mirobot_cycle_standard(self, alarm):
        #self.mirobot.start()
        #cycle_standard()
        #self.allow_to_fly = 1
        self.stop()




def planning_make(h,m,n=10,prgm=1):
    _planning = list()
    for _ in range(n):
        _planning.append(('{:02}:{:02}'.format(h,m+_),1,'{}'.format(prgm)))
    return _planning

# planning=planning_make(16,30,n=10)
# planning=planning_make(16,40,n=2)


#set_date(annee=2018,mois=12,jour=10,heure=12,minute=12,seconde=45)


def set_date(annee=2017,mois=12,jour=13,heure=12,minute=0,seconde=0):
    global planning
    _annee = annee if 2017 <= annee <= 2117 else 2017
    _mois = mois if 1 <= mois <= 12 else 12
    _jour = jour if 1 <= jour <= 31 else 13
    _heure = heure if 0 <= heure <= 23 else 12
    _minute = minute if 0 <= minute <= 59 else 0
    _seconde = seconde if 0 <= seconde <= 59 else 0
    _date_ancienne = rtc.now()
    _heure_ancienne = _date_ancienne[3]
    _minute_ancienne = _date_ancienne[4]
    #heure réelle - heure antérieure
    _diff_min = (_heure * 60 + _minute) - (_heure_ancienne * 60 + _minute_ancienne)
    planning = planning_time_adjust(planning, _diff_min)
    RTC(datetime=(_annee, _mois, _jour, _heure, _minute, _seconde, 0, None))
    _date_update = rtc.now()
    print('Heure antérieure: {}'.format(_date_ancienne))
    print('Heure mis à jour: {}'.format(_date_update))



#planning=list()
#planning=planning_get()
#planning
#heure réelle - heure antérieure
#_diff_min = (_heure * 60 + _minute) - (_heure_ancienne * 60 + _minute_ancienne)
def planning_time_adjust(planning, diff_en_min):
    #global planning
    #print('planning = {}'.format(planning))
    _planning = list()
    for depart in planning:
        _activation = depart[1]
        _prgm = depart[2]
        depart=depart[0].split(':')
        _h = int(depart[0])
        _m = int(depart[1])
        depart_en_min_ancien = _h * 60 + _m
        depart_en_min_actuelle = depart_en_min_ancien + diff_en_min
        if depart_en_min_actuelle < 0 :
            depart_en_min_actuelle = 24*60 + depart_en_min_actuelle
        #_planning.append(str(_h)+':'+str(_m))
        _h_actuelle = '{:04.1f}'.format(depart_en_min_actuelle/60)
        _h_actuelle = _h_actuelle[0:2]
        _m_actuelle = '{:02.0f}'.format(depart_en_min_actuelle%60)
        _planning.append(('{}:{}'.format(_h_actuelle, _m_actuelle), _activation, '{}'.format(_prgm)))
        print('ancienne heure ({:02.0f}:{:02.0f}) => nouvelle heure ({}:{})'.format(_h, _m, _h_actuelle, _m_actuelle))
    return _planning


def planning_get():
    Fichier_Depart = 'planning.txt'
    _nombre_element_fichier_sauvegarde = 4
    _planning = list()
    if not Fichier_Depart in uos.listdir('/flash'):
        return _planning
    #fichier_depart = open('/flash/'+Fichier_Depart, 'r')
    with open('/flash/'+Fichier_Depart, 'r') as fichier_depart:
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
                    _planning.append((str(_h)+':'+str(_m), _activation, '{}'.format(_prgm)))
                except:
                    pass
        #_planning.append(depart.strip())
    return _planning

#def planning_save(planning):
def planning_save(planning):
    #global planning
    #on supprimer le fichier existant
    Fichier_Depart = 'planning.txt'
    if Fichier_Depart in uos.listdir('/flash'):
        uos.remove('/flash/'+Fichier_Depart)
    for depart in planning:
        print(depart)
        fichier_depart = open('/flash/'+Fichier_Depart, 'a')
        #fichier_depart.write(depart+'\n')
        fichier_depart.write('{}:{}:{}\n'.format(depart[1],depart[0],depart[2]))
        fichier_depart.close()


#def planning_prochain_depart(planning):
def planning_prochain_depart(planning):
    #global planning
    if not planning: #(not planning or len(planning)==0):
        return None
    #retourne le nombre de seconde avant le prochaine depart
    _planning = list()
    for depart in planning:
        _prgm = depart[2]
        depart=depart[0].split(':')
        _h = int(depart[0])
        _m = int(depart[1])
        #print('{:02}:{:02}'.format(_h,_m))
        _planning.append(_h*3600+_m*60)
    _planning.sort()
    date_now = rtc.now()
    date_h = int(date_now[3])
    date_m = int(date_now[4])
    date_s = date_h * 3600 + date_m * 60 + int(date_now[5])
    #si la date actuelle est plus importante que le dernier départs
    #cela veut dire que le prochain départ se situe le jour suivant
    #on ajoute donc la valeur d'un jour en seconde au _planning actuelle
    if date_s > _planning[-1]:
        print('Demain')
        _planning = [depart+24*3600 for depart in _planning]
    for depart in _planning:
        if depart >= date_s:
            countdown = depart - date_s
            #print('Reste {} s avant le prochaine départ ({} min ou {} h)'.format(countdown,countdown/60,countdown/3600))
            return countdown

#_planning = planning_prochain_depart()



#def planning_prochain_depart(planning):
def planning_prochain_depart_valeur(planning):
    #global planning
    if not planning: #(not planning or len(planning)==0):
        return (None, None)
    #retourne le nombre de seconde avant le prochaine depart
    _planning = list()
    for depart in planning:
        _activation = depart[1]
        _prgm = depart[2]
        depart=depart[0].split(':')
        _h = int(depart[0])
        _m = int(depart[1])
        #print('{:02}:{:02}'.format(_h,_m))
        if _activation == True:
            _planning.append((_h*3600+_m*60, _prgm))
        #_planning.append((str(_h)+':'+str(_m), _activation, '{}'.format(_prgm)))
    if _planning == list():
        return (None, None)
    _planning.sort()
    date_now = rtc.now()
    date_h = int(date_now[3])
    date_m = int(date_now[4])
    date_s = date_h * 3600 + date_m * 60 + int(date_now[5])
    #si la date actuelle est plus importante que le dernier départs
    #cela veut dire que le prochain départ se situe le jour suivant
    #on ajoute donc la valeur d'un jour en seconde au _planning actuelle
    if date_s > _planning[-1][0]:
        print('Demain')
        #_planning = [depart+24*3600 for depart in _planning]
        date_s -= 24*3600
        #return
    for depart in _planning:
        if depart[0] >= date_s:
            countdown = depart[0] - date_s
            #print('Reste {} s avant le prochaine départ ({} min ou {} h)'.format(countdown,countdown/60,countdown/3600))
            return countdown, depart[1] #renvoi le nombre de seconde restant avant le démarrage du programme contenu dans depart[1]


#planning = planning_get()
