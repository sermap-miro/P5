from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT

from machine import RTC
from time import localtime, sleep
from config import Batt_Mean 
from planning import planning_save

from commande import Send_Prgm, Write_Prgm
import ujson
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
				print(_planning_brut)
				return(_planning_brut)
		else:
			return ('')
	except:
		return ('')

def Rep_Server(type=''):
	if (type == 'html'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "03a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
		text += '\r\n'
	elif (type == 'js'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: max-age=2678400\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
		text += 'Server: SERMAP\r\n'
		text += "Content-Security-Policy: default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self';\r\n"
		text += 'Content-Type: application/javascript; charset=utf-8\r\n'
		text += '\r\n'
	elif (type == 'jsc'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: no-store, no-cache, must-revalidate, private \r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "33a64df551425fcc55e4df2a148795d9f25f89de"\r\n'
		text += 'Server: SERMAP\r\n'
		text += "Content-Security-Policy: default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self';\r\n"
		text += 'Content-Type: application/javascript; charset=utf-8\r\n'
		text += '\r\n'
	elif (type == 'css'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: max-age=2678400\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "43a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
		text += 'Server: SERMAP\r\n'
		text += 'Content-Type: text/css\r\n'
		text += '\r\n'
	elif (type == 'cssa'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Cache-Control: no-store, no-cache, must-revalidate, private \r\n'
		text += 'Cache-Control: max-age=2678400\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "43a64df551425fcc55e4d42a148795d9f25ffdd4"\r\n'
		text += 'Server: SERMAP\r\n'
		text += 'Content-Type: text/css\r\n'
		text += '\r\n'
	elif (type == 'logo'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: max-age=2678400\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "53a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
		text += 'Server: SERMAP\r\n'
		text += 'Content-Type: image/png\r\n'
		text += '\r\n'
	elif (type == 'ico'):
		text = 'HTTP/1.0 200 OK\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: max-age=2678400\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "63a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
		text += 'Server: SERMAP\r\n'
		text += 'Content-Type: image/x-icon\r\n'
		text += '\r\n'
	elif (type == 'json'):
		text = 'HTTP/1.0 201 Created\r\n'
		text +='Connection : close\r\n'
		text +='Cache-Control:no-cache, no-store, private\r\n'
		text +='Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text +='ETag: "63a64df551425fcd57e4d42aff8795d9f25f89d5"\r\n'
		text += 'Server : SERMAP\r\n'
		text += 'Content-Type : application/json\r\n'
		text += '\r\n'
	elif (type == 'txt'):
		text =  'HTTP/1.0 201 	Created\r\n'
		text += 'Connection: close\r\n'
		text += 'Cache-Control: no-store, no-cache, private\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'ETag: "63a64df551425fcc55e4d42a148795d9f25f89d5"\r\n'
		text += 'Server: SERMAP\r\n'
		text += 'Content-Type: text\r\n'
		text += '\r\n'
	elif (type == 'processing'):
		text =  'HTTP/1.0 102 Processing\r\n'
		text += 'Connection: keep-alive\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'Server: SERMAP\r\n'
		text += '\r\n'
	elif (type == '500'):
		text =  'HTTP/1.0 102 Internal Server Error\r\n'
		text += 'Connection: close\r\n'
		text += 'Last-Modified: {} {} {} {}:{}:{} GMT\r\n'.format(m.rtc.now()[2],m.get_month(m.rtc.now()[1]),m.rtc.now()[0],m.rtc.now()[3],m.rtc.now()[4],m.rtc.now()[5])
		text += 'Server: SERMAP\r\n'
		text += '\r\n'
	else:
		print("Rep_Server : L'extension du fichier n'est pas connu")
		return ''
	return (text)

def Planning_Record(request=''):
	_planning = list()
	try:
		ibe = request.find('c1=')
		_planning_brut = request[ibe:]
		_Erreur = 0
		m.bug_michel = request
		print('Function Planning_Record  =====> =====>====>')
		for _ in range(20):
			
			try:
				#print('erreur: {} => _a={},_h={},_m={},_p={}'.format(_,_activation, _h, _m, _prgm))
				print('data a extraire = {}'.format(_))
				_activation = Extract_Data(_planning_brut=_planning_brut, _type='c', _indice=_+1)
				print('{}:_a={}'.format(_,_activation))
				_h = int(Extract_Data(_planning_brut=_planning_brut, _type='h', _indice=_+1))
				print('{}:_h={}'.format(_, _h))
				_m = int(Extract_Data(_planning_brut=_planning_brut, _type='m', _indice=_+1))
				print('{}:_m={}'.format(_, _m))
				_prgm = Extract_Data(_planning_brut=_planning_brut, _type='p', _indice=_+1)
				#print('')
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
			print('Function Planning_Record : Enregistrement terminé')
	except:
		pass
	

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
	try:
		with open(m.calib_json,"r") as f:
			m.d_calib = ujson.load(f)
		f.close()
	except:
		print('Unable to open calib.json')
	#print('Execution Programme Indice = {}'.format(Indice))
	try:
		Indice = int(Indice)
	except:
		Indice = 0
	if (Indice == 1):
		exec("m.batterie_10_v=Batt_Mean(m);m.PARAM_STORE();")
		m.d_calib["10V"] = Batt_Mean(m)
	elif (Indice == 2):
		exec("m.batterie_30_v=Batt_Mean(m);m.PARAM_STORE();")
		m.d_calib["30V"] = Batt_Mean(m)
	elif (Indice == 4):
		exec("m.PIC_LED(1); m.LED(True);m.PIC_SEND('R1');")
	elif (Indice == 5):
		exec("m.PIC_LED(0); m.LED(False);m.PIC_SEND('R0');")
	elif (Indice == 6):
		exec("RTC(datetime=(2020, 1, 1, 0, 0, 0, 0, None))")
	elif (Indice == 3):
		for _ in range (10):
			exec("Signal_Sonore()")
			sleep(0.1)
	j = ujson.dumps(m.d_calib)
	try:
		with open(m.calib_json,"w") as f:
			f.write(j)
		f.close()
	except: 
		print('Unable to write on files')
