from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT
from machine import RTC
from time import localtime, sleep
from planning import planning_save
from commande import Send_Prgm, Write_Prgm
from AiCwebserver_CMD import Extract_Data, Planning_Record, Commande_Manuel, Execution_Programme, Execution_Calibration,Rep_Server
from wifi import wlan
from gc import collect

HTML_HEADER_NOCACHE = 'HTTP/1.0 200 OK\r\n'
HTML_HEADER_NOCACHE += 'Connection: close\r\n'
HTML_HEADER_NOCACHE += '\r\n'

POST_HEADER = 'HTTP/1.0 200 OK\r\n'
POST_HEADER += 'Connection: close\r\n'


CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""
def AiCWebserv(port):
	
	import socket
	import gc
	m.gc = gc
	
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('192.168.4.1', port))
			s.listen(0)
			Tourne = 1
			_wifi = 0
			_CONVERSION_FACTOR_CAN_2_AMPERE = 5
			Facteur_Conversion_Ampere_2_CAN = 5
			while Tourne == 1:
				m.gc.collect()
				try:
						m.web = 'Attente Connexion'
						m.affiche(m.web)
						conn = None
						attente = 0
						while conn is None:
							conn, addr = s.accept()
							print(addr[0])
							attente += 1
							m.web = 'Attente Connexion {}'.format(attente)
							sleep(0.1)
						m.web = 'Attente Requete'
						m.affiche(m.web)
						try:
							conn.settimeout(1)
							request = conn.recv(2048)
							conn.settimeout(None)
							m.web = 'Requete Accept'
							request = str(request.decode('utf8'))
							m.affiche('request = {}'.format(request))
							m.affiche("requete = {}".format(request))
						except:
							m.web = 'Mauvaise Reception de la Requete = {}'.format(request)
							m.web_debug = m.web
							request = ''
						m.affiche(m.web)
						try:
							requete = request[:request.find('HTTP')]
						except:
							requete = request

						if request[0:4]=='POST' and request.find('Safari')>0 and request.find('Chrom')<=0:
							m.affiche('Requete 2 Attente (4 safari)')
							try:
								conn.settimeout(0.1)
								request2 = conn.recv(1024)
								conn.settimeout(None)
								m.web = 'Requete 2 Accept (4 safari)'
								m.affiche('request 2 (4 safari) avant decode = {}'.format(request2))
								request2 = str(request2.decode('utf8'))
								m.request2 = request2
								m.affiche('request 2 (4 safari) après decode = {}'.format(request2))
								request += request2
								m.affiche('request final = {}'.format(request))
							except:
								m.web = 'Mauvaise Reception de la Requete 2  (4 safari)= {}'.format(request2)
								m.web_debug = m.web
								request = '' 
						ib = requete.find('Val=')
						ibvp = requete.find('Valp=')
						ibh = requete.find('H=')
						ibs = requete.find('Stat')
						ib3 = requete.find('T3')
						ibc = requete.find('Clock')
						ibo = requete.find('Conf')
						ibw = requete.find('Edit')
						ibf = requete.find('Wifi')
				
						ibfavicon = requete.find('favicon')
						ibvc = requete.find('Valc=')
						ibexit = requete.find('xit')

						ibbootstrap_min_css = requete.find('bootstrap.min.css')
						ibmiro_css = requete.find('miro.min.css')
						ibmiroresponsive_css = requete.find('miro.responsive.css')
						
						ibbootstrap_bundle_min_js = requete.find('bootstrap.bundle.min.js')
						ibbootstrap_jquery_js = requete.find('jquery-3.3.1.min.js')
						ibmain_js = requete.find('main.min.js')
						
						ibinfo_json = requete.find('info.json')
						ibclock_json = requete.find('clock.json')
						ibconf_json = requete.find('conf.json')
						get_wifi_data = requete.find('wifi.json')
						
						ibl_white = requete.find('l_white.png')
						ibmiro_logo = requete.find('logo.png')
						sermap_png = requete.find('SERMAP.png')
						ok_png = requete.find('done.png')
						no_png = requete.find('clear.png')
						
						txt_p = requete.find('planning.txt')
						txt_1 = requete.find('1.txt')
						txt_2 = requete.find('2.txt')
						txt_3 = requete.find('3.txt')
						txt_4 = requete.find('4.txt')
						txt_5 = requete.find('5.txt')
						txt_6 = requete.find('6.txt')
						txt_7 = requete.find('7.txt')
						txt_8 = requete.find('8.txt')
						txt_9 = requete.find('9.txt')
						txt_Retour = requete.find('Retour.txt')
						Standard = requete.find('Standard.txt')
						Pailleux = requete.find('Pailleux.txt')
						DVT = requete.find('DVT.txt')
						MultiTas = requete.find('MultiTas.txt') 
						if ibexit > 0: #xit 
							conn.send(bytes("P5 Web Access Closed", "ascii"))
							Tourne = 0
						elif ibbootstrap_min_css > 0 : 
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('css'))
							with open('assets/css/bootstrap.min.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)

						elif txt_p > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/planning.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_1 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/1.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
							
						elif txt_2 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/2.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
							
						elif txt_3 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/3.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
							
						elif txt_4 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/4.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
							
						elif txt_5 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/5.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_6 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/6.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_7 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/7.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_8 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/8.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_9 > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/9.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif txt_Retour > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/Retour.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif Standard > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/Standard.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif DVT > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/DVT.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
						
									data = f.read(CHUNK_SIZE)
									
						elif Pailleux > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/Pailleux.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif MultiTas > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('txt'))
							with open('/flash/prgm/MultiTas.txt','rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmiro_css > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('cssa'))
							with open('assets/css/miro.min.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmiroresponsive_css > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('css'))
							with open('assets/css/miro.responsive.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif ibbootstrap_bundle_min_js > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('js'))
							with open('assets/js/bootstrap.bundle.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)	
						elif ibbootstrap_jquery_js > 0 :
							conn.sendall(Rep_Server('js'))
							CHUNK_SIZE = 512
							with open('assets/js/jquery-3.3.1.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif ibmain_js > 0 :
							conn.sendall(Rep_Server('jsc'))
							CHUNK_SIZE = 512
							with open('assets/js/main.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif ibinfo_json > 0 :
							conn.sendall(Rep_Server('json'))
							m.update_info()
							CHUNK_SIZE = 512
							
							with open('assets/json/info.json', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data :
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibclock_json > 0 :
							m.clk_up()
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('json'))
							with open('assets/json/clock.json', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data :
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)

						elif ibconf_json > 0 :
							conn.sendall(Rep_Server('processing'))
							m.update_conf()
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('json'))
							with open('assets/json/conf.json', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data :
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif get_wifi_data > 0:
							conn.sendall(Rep_Server('json'))
							CHUNK_SIZE = 512
							m.channel_wifi()
							with open('assets/json/wifi.json', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data :
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)

						elif ibmiro_logo > 0 :
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('logo'))
							with open('assets/img/logo.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
							
									
						elif ibl_white > 0 :
							conn.sendall(Rep_Server('logo'))
							CHUNK_SIZE = 512
							with open('assets/img/l_white.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif sermap_png > 0 :
							conn.sendall(Rep_Server('logo'))
							CHUNK_SIZE = 512
							with open('assets/img/SERMAP.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
						elif ok_png > 0 :
							conn.sendall(Rep_Server('logo'))
							CHUNK_SIZE = 512
							with open('assets/img/done.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif no_png > 0 :
							conn.sendall(Rep_Server('logo'))
							CHUNK_SIZE = 512
							with open('assets/img/clear.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibvc > 0 : #Commandes Calibration
							ie = request.find(' ', ibvc)
							Val = request[ibvc+5:ie]
							Execution_Calibration(Val)
							conn.sendall(POST_HEADER)
							conn.send(Val)
							
						elif ibs > 0 : #Commandes Info
							conn.sendall(Rep_Server('html'))
							conn.send(bytes("<p>", "ascii"))
							conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
							
						elif ibfavicon > 0 :#http://michaldul.com/python/sendfile/ # https://convertico.com/
							CHUNK_SIZE = 512
							conn.sendall(Rep_Server('ico'))
							with open('favicon.ico', 'rb') as ico:
								data = ico.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = ico.read(CHUNK_SIZE)
							
									
						elif ibh > 0 : #Réglage horloge
							ie = request.find(' ', ibh)
							Val = request[ibh+2:ie]
							m.affiche(Val)
							try:
								_h = int(Val)
								conn.send(bytes("<p>", "ascii"))
								conn.send(bytes("Mise à jour de l'horloge: Ok", "ascii"))
								conn.sendall(POST_HEADER)
							except:
								if Val.find(':')>0:
									try:
										_h = int(Val.split(':')[0])
										_m = int(Val.split(':')[1])
										_y = int(Val.split(':')[2])
										_mo = int(Val.split(':')[3])
										_d = int(Val.split(':')[4])
										m.affiche("Heure {}:{} Date {}/{}/{}".format(_h,_m,_d,_mo,_y))
										conn.sendall(POST_HEADER)
									except:
										_h = 12
										_m = 00
										_y = 2019
										_mo = 9
										_d = 10
										conn.send(bytes("<p>", "ascii"))
										conn.send(bytes("Mise à jour de l'horloge => Heure par défaut: 12h00", "ascii"))
										pass
							
							f_date = '/flash/assets/json/clock.json'
							try:
								with open(f_date,'w') as f:
									word = '{{"h" : {0}, "m" : {1} }}'.format(_h,_m)
									f.write(word)
								f.close()
							except:
								m.affiche("Impossible d'ouvrir le fichier clock.json en mode écriture ")		
							m.rtc = RTC(datetime=(_y, _mo, _d, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
							
						elif ib > 0 : #Val (Manuel_cmd(cmd))
							ie = request.find(' ', ib)
							Val = request[ib+4:ie]
							Commande_Manuel(Val)
							conn.sendall(POST_HEADER)
							conn.send(Val)
							
						elif ibvp > 0 : #Valp (Programme_cmd(cmd))
							ie = request.find(' ', ibvp)
							Val = request[ibvp+5:ie]
							Execution_Programme(Val)
							conn.sendall(POST_HEADER)
							conn.send(Val) 
							
						elif ib3 > 0 : #Page Planning apres enregistrement
							m.requete=request
							Planning_Record(request=m.requete)
							m.affiche("Les modifications ont été pris en compte")
							conn.sendall(POST_HEADER)
						elif ibc > 0 : # Page Horloge
							_clock_set = 0
							if request[0:3]!='GET':
								try:
									_h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
									m.affiche('_h={}'.format(_h))
									_m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
									m.affiche('_m={}'.format(_m))
									_clock_set = 1
									_y = int(Extract_Data(_planning_brut=request,_type='y', _indice=1))
									_mo = int(Extract_Data(_planning_brut=request,_type='m', _indice=0))
									_d = int(Extract_Data(_planning_brut=request,_type='d', _indice=1))
									

									m.rtc = RTC(datetime=(_y, _mo, _d, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
									conn.sendall(POST_HEADER)
								except:
									m.web_debug = 'Exception dans: Extraction Heure et Minute'
									m.affiche('m.web_debug = {}\nm.request = {}'.format(m.web_debug, m.request))
									pass
									
						elif ibo > 0 : # Page Configuration
							# _conf_set = 0
							# _statut_brut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name)
							# data = _statut_brut.split(' ')
							m.requete=request
							conn.sendall(Rep_Server('processing'))
							if request[0:3]!='GET':
								try:
									_m = int(float(Extract_Data(_planning_brut=request, _type='m', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									conn.sendall(Rep_Server('processing'))
									if 0<=_m<=255:
										m.Moteur_X_Consigne = _m
										m.affiche("CONF Moteur_X_Consigne = {} A".format(_m))
									_c = int(float(Extract_Data(_planning_brut=request, _type='c', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									conn.sendall(Rep_Server('processing'))
									if 0<=_c<=255:
										m.Moteur_Z_Consigne = _c
										m.affiche("CONF Consigne Z Moteur = {} A".format(_c))
									_s = int(float(Extract_Data(_planning_brut=request, _type='s', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									conn.sendall(Rep_Server('processing'))
									if 0<=_s<=255:
										m.Moteur_Z_Limite_Courant = _s
										m.affiche("CONF Mot_Z_Cou = {} A".format(_s))
									_b = int(float(Extract_Data(_planning_brut=request, _type='b', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									conn.sendall(Rep_Server('processing'))
									if 0<=_b<=255:
										m.Moteur_Bequille_Consigne = _b
										m.affiche("CONF Consigne Bequille = {} A".format(_b))
									_d = int(float(Extract_Data(_planning_brut=request, _type='d', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									conn.sendall(Rep_Server('processing'))
									if 0<=_d<=255:
										m.Moteur_Bequille_Limite_Courant = _d
										m.affiche("CONF Seuil Bequille = {} A".format(_d))
									_p = int(float(Extract_Data(_planning_brut=request, _type='p', _indice=1)))
									conn.sendall(Rep_Server('processing'))
									if 0<=_p<=255:
										m.PATINAGE_TEMPS_s = _p
										m.affiche("CONF Temps Patinage = {} ".format(_p))
									_i = int(float(Extract_Data(_planning_brut=request, _type='i', _indice=1))) / 100
									conn.sendall(Rep_Server('processing'))
									if 0<=_i<=255:
										m.PION_TEMPS_100ms = _i
										m.affiche("CONF Temps Pions = {} ms".format(_i))
									_l = int(float(Extract_Data(_planning_brut=request, _type='l', _indice=1))) / 100
									conn.sendall(Rep_Server('processing'))
									if 0<=_l<=255:
										m.PLATINE_TEMPS_100ms = _l
										m.affiche("CONF Temps Platine = {} ms".format(_l))
									_e = int(float(Extract_Data(_planning_brut=request, _type='e', _indice=1)))
									if 0<=_e<=255:
										m.Nb_Seconde_Pelle = _e
										m.affiche("CONF Secondes Pelle = {} s".format(_e))
									# _conf_set = 1
									
									m.PARAM_STORE()
									m.PIC_PARAM_UPDATE()
									m.update_conf()
									m.affiche('Mise a jour des configurations réussie')
									conn.sendall(POST_HEADER)
								except:
									pass
						elif ibf > 0 : #Page Wifi
							_wifi=0
							m.affiche("Rafraîchissement f")
							if request[0:3]!='GET':
								conn.sendall(POST_HEADER)
								_wifi_name = Extract_Data(_planning_brut=request, _type='n', _indice=1)
								_wifi_password = Extract_Data(_planning_brut=request, _type='p', _indice=1)
								_wifi_channel = Extract_Data(_planning_brut=request, _type='c', _indice=1)
								m.affiche('nom = {}'.format(_wifi_name))
								m.affiche('password = {}'.format(_wifi_password))
								try:
									_wifi_channel = int(_wifi_channel)
									m.affiche('channel = {}'.format(_wifi_channel))
								except:
									_wifi_channel = 7
									m.affiche('except => channel = {}'.format(_wifi_channel))
								_wifi=1
								conn.close()
								sleep(2)
								if len(_wifi_name) > 0:
									exec('wifi_nom = "{}"'.format(_wifi_name))
									with open("/flash/wifi_name.txt", "w+") as _f: _f.write('{}'.format(_wifi_name))
									with open("/flash/wifi_password.txt", "w+") as _f: _f.write('{}'.format(_wifi_password))
									with open("/flash/wifi_channel.txt", "w+") as _f: _f.write('{}'.format(_wifi_channel))
									exec('m.wifi_name = "P5 - {}"'.format(_wifi_name))
									exec('m.wifi_password = "{}"'.format(_wifi_password))
									exec('m.wifi_channel = {}'.format(_wifi_channel))
								else:
									m.affiche('Wifi name = ""')
									with open("/flash/wifi_name.txt", "w+") as _f: _f.write('')
									exec('m.wifi_name = "P5"')
									exec('m.wifi_password = ""')

									with open("/flash/wifi_channel.txt", "w+") as _f: _f.write('{}'.format(_wifi_channel))
									exec('m.wifi_channel = {}'.format(_wifi_channel))
								exec('Wifi_Local()')
						elif ibw > 0 : #Page Edit
							_error = 0
							if request[0:3]!='GET':
								m.affiche("GET ABSENT = > POST? = {}".format(request[0:2]))
								try:
									data = Extract_Data(_planning_brut=request, _type='d', _indice=1)
									_Prgm_Indice = Extract_Data(_planning_brut=request, _type='p', _indice=1)
									_type = Extract_Data(_planning_brut=request, _type='s', _indice=1)
									#https://cachefly.zendesk.com/hc/en-us/articles/215068626-How-to-format-URLs-that-have-special-characters-in-the-filename-
									data = data.replace('%0A', '\n')
									data = data.replace('%0D', '\r')
									data = data.replace('%09', '\t')
									data = data.replace('%23', '#')
									data = data.replace('%22', '"')
									data = data.replace('%25', '%')
									data = data.replace('%26', '&')
									data = data.replace('%28', '(')
									data = data.replace('%29', ')')
									data = data.replace('%21', '!')
									data = data.replace('%2A', '*')
									data = data.replace('%2F', '/')
									data = data.replace('%2D', '-')
									data = data.replace('%2E', '.')
									data = data.replace('%2C', ',')
									data = data.replace('%3F', '?')
									data = data.replace('%3B', ';')
									data = data.replace('%5B', '[')
									data = data.replace('%5C', '\\')
									data = data.replace('%5D', ']')
									data = data.replace('%7B', '{')
									data = data.replace('%7C', "|")
									data = data.replace('%A6', "|")
									data = data.replace('%7D', '}')
									data = data.replace('%5E', '^')
									data = data.replace('%3B', ';')
									data = data.replace('%3D', '=')
									data = data.replace('%3E', '>')
									data = data.replace('%3C', '<')
									data = data.replace('%3A', ':')
									data = data.replace('%40', '@')
									data = data.replace('+', ' ')
									data = data.replace('%27', "'")
									data = data.replace('%C3%A0', 'à')
									data = data.replace('%C3%A8', 'è')
									data = data.replace('%C3%A9', 'é')
									data = data.replace('%C3%AA', 'ê')
									data = data.replace('%C3%AB', 'ë')
									if _type == 'W':
										try:
											Write_Prgm(_Prgm_Indice,data)
											conn.sendall(POST_HEADER)
										except:
											conn.sendall(Rep_Server("500"))
											_error = 1
											pass
									_prgm = _Prgm_Indice
								except:
									pass
							try:
								with open('index.html', 'r') as html:
									for line in html.readlines():
										conn.send(bytes(line,"ascii"))
								html.close()
							except:
								m.affiche("Ouverture de index.html impossible!")
						else: #Menu Principal
							m.affiche('Rafraîchissement Menu Principal (else): requete = {}'.format(request))		
							conn.sendall(Rep_Server('html'))
							if len(request)>0:
								try:
									with open('index.html', 'r') as html:
										for line in html.readlines():
											conn.send(bytes(line,"ascii"))
									html.close()
								except:
									m.affiche("Ouverture de index.html impossible")		   
						if _wifi==0:
							conn.sendall('\n')
							conn.close()
						else:
							_wifi=0
				except:
					try:
						conn.close()
					except:
						pass
					m.web = 'Except Reception'
					m.affiche(m.web)
					pass
				finally:
					collect()
		except:
			m.web = 'Except Bind'
			m.affiche(m.web)
			m.web_debug = m.web # ne devrait pas arriver en théorie
			pass