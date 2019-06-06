from mirobot2 import m
from es import ARRET_URGENCE #, BUZZER, BUZZER_INPUT
from machine import RTC
from time import localtime, sleep
from planning import planning_save
from commande import Send_Prgm, Write_Prgm
from AiCwebserver_CMD import Extract_Data, Planning_Record, Planning_Print_old, Planning_Print, Commande_Manuel, Execution_Programme, Execution_Calibration, Print_HTM
from wifi import wlan
from gc import collect

HTML_HEADER = 'HTTP/1.0 200 OK\r\n'
HTML_HEADER += 'Connection: close\r\n'
HTML_HEADER += 'Last-Modified: Fri, 1 Jan 2019 23:42:00 GMT\r\n'
HTML_HEADER += 'ETag: "03a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
HTML_HEADER += '\r\n'

HTML_HEADER_NOCACHE = 'HTTP/1.0 200 OK\r\n'
HTML_HEADER_NOCACHE += 'Connection: close\r\n'
HTML_HEADER_NOCACHE += '\r\n'

JAVASCRIPT_HEADER = 'HTTP/1.0 200 OK\r\n'
JAVASCRIPT_HEADER += 'Connection: close\r\n'
JAVASCRIPT_HEADER += 'Cache-Control: max-age=2678400, public\r\n'
JAVASCRIPT_HEADER += 'Last-Modified: Fri, 1 Jan 2019 23:42:00 GMT\r\n'
JAVASCRIPT_HEADER += 'ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
JAVASCRIPT_HEADER += 'Server: SERMAP\r\n'
JAVASCRIPT_HEADER += "Content-Security-Policy: default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self';\r\n"
JAVASCRIPT_HEADER += 'Content-Type: application/javascript; charset=utf-8\r\n'
JAVASCRIPT_HEADER += '\r\n'

CSS_HEADER = 'HTTP/1.0 200 OK\r\n'
CSS_HEADER += 'Connection: close\r\n'
CSS_HEADER += 'Cache-Control: max-age=2678400, public\r\n'
CSS_HEADER += 'Last-Modified: Fri, 1 Jan 2019 23:42:00 GMT\r\n'
CSS_HEADER += 'ETag: "43a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
CSS_HEADER += 'Server: SERMAP\r\n'
CSS_HEADER += 'Content-Type: text/css\r\n'
CSS_HEADER += '\r\n'

LOGO_HEADER = 'HTTP/1.0 200 OK\r\n'
LOGO_HEADER += 'Connection: close\r\n'
LOGO_HEADER += 'Cache-Control: max-age=2678400, public\r\n'
LOGO_HEADER += 'Last-Modified: Fri, 1 Jan 2019 23:42:00 GMT\r\n'
LOGO_HEADER += 'ETag: "53a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
LOGO_HEADER += 'Server: SERMAP\r\n'
LOGO_HEADER += 'Content-Type: image/png\r\n'
LOGO_HEADER += '\r\n'


ICO_HEADER = 'HTTP/1.0 200 OK\r\n'
ICO_HEADER += 'Connection: close\r\n'
ICO_HEADER += 'Cache-Control: max-age=2678400, public\r\n'
ICO_HEADER += 'Last-Modified: Fri, 1 Jan 2019 23:42:00 GMT\r\n'
ICO_HEADER += 'ETag: "63a64df551425fcc55e4d42a148795d9f25f89d4"\r\n'
ICO_HEADER += 'Server: SERMAP\r\n'
ICO_HEADER += 'Content-Type: image/x-icon\r\n'
ICO_HEADER += '\r\n'


POST_HEADER = 'HTTP/1.0 200 OK\r\n'
POST_HEADER += 'Connection: close\r\n'


CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""
def AiCWebserv(port):
	head = 'head.htm'
	header = 'header.htm'
	footer = 'footer.htm'
	
	import socket
	import gc
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('', port))
			s.listen(0)#
			Tourne = 1
			_wifi = 0
			_CONVERSION_FACTOR_CAN_2_AMPERE = 5
			Facteur_Conversion_Ampere_2_CAN = 5
			while Tourne == 1:
				gc.collect()
				try:
						m.web = 'Attente Connexion'
						m.affiche(m.web)
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
							request = conn.recv(2048)
							conn.settimeout(None)
							m.web = 'Requete Accept'
							request = str(request.decode('utf8'))
							m.affiche('request = {}'.format(request))
							print("requete = {}".format(request))
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
						ibbootstrap_min_css = requete.find('bootstrap.min.css')
						ibmiro_css = requete.find('miro.css')
						ibmiroresponsive_css = requete.find('miro.responsive.css')
						ibbootstrap_bundle_min_js = requete.find('bootstrap.bundle.min.js')
						ibbootstrap_jquery_js = requete.find('jquery-3.3.1.min.js')
						ibmain_js = requete.find('main.min.js')
						ibmiro_logo = requete.find('logo.png')
						if ibexit > 0: #xit 
							conn.send(bytes("P5 Web Access Closed", "ascii"))
							Tourne = 0
						elif ibbootstrap_min_css > 0 : 
							CHUNK_SIZE = 512
							conn.sendall(CSS_HEADER)
							with open('assets/css/bootstrap.min.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmiro_css > 0 :
							CHUNK_SIZE = 512
							conn.sendall(CSS_HEADER)
							with open('assets/css/miro.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmiroresponsive_css > 0 :
							CHUNK_SIZE = 512
							conn.sendall(CSS_HEADER)
							with open('assets/css/miro.responsive.css', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)

						elif ibbootstrap_bundle_min_js > 0 :
							conn.sendall(JAVASCRIPT_HEADER)
							CHUNK_SIZE = 512
							with open('assets/js/bootstrap.bundle.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibbootstrap_jquery_js > 0 :
							conn.sendall(JAVASCRIPT_HEADER)
							CHUNK_SIZE = 512
							with open('assets/js/jquery-3.3.1.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmain_js > 0 :
							conn.sendall(JAVASCRIPT_HEADER)
							CHUNK_SIZE = 512
							with open('assets/js/main.min.js', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibmiro_logo > 0 :
							conn.sendall(LOGO_HEADER)
							CHUNK_SIZE = 512
							with open('assets/img/logo.png', 'rb') as f:
								data = f.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = f.read(CHUNK_SIZE)
									
						elif ibcalibration > 0 : #Page Calibration
							conn.sendall(HTML_HEADER)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('calibration.htm',conn)
							Print_HTM(footer,conn)
						elif ibvc > 0 : #Commandes Calibration
							ie = request.find(' ', ibvc)
							Val = request[ibvc+5:ie]
							Execution_Calibration(Val)
							conn.sendall(POST_HEADER)
							conn.send(Val)
							
						elif ibs > 0 : #Commandes Info
							conn.sendall(HTML_HEADER)
							conn.send(bytes("<p>", "ascii"))
							conn.send(bytes('{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name), "ascii"))
							
						elif ibfavicon > 0 :#http://michaldul.com/python/sendfile/ # https://convertico.com/
							CHUNK_SIZE = 512
							conn.sendall(ICO_HEADER)
							with open('favicon.ico', 'rb') as ico:
								data = ico.read(CHUNK_SIZE)
								while data:
									conn.send(bytes(data))
									data = ico.read(CHUNK_SIZE)
									
						elif ibh > 0 : #Réglage horloge
							ie = request.find(' ', ibh)
							Val = request[ibh+2:ie] 
							conn.sendall(HTML_HEADER) 
							try:
								_h = int(Val)
								conn.send(bytes("<p>", "ascii"))
								conn.send(bytes("Mise à jour de l'horloge: Ok", "ascii"))
							except:
								if Val.find(':')>0:
									try:
										_h = int(Val.split(':')[0])
										_m = int(Val.split(':')[1])

										conn.send(bytes("<p>", "ascii"))
										conn.send(bytes("Mise à jour de l'horloge: Ok", "ascii"))
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
							conn.send(bytes('<a href="/">Menu Principal</a>', "ascii"))
							
						elif ibe > 0 or ibi > 0: # Page Information
							conn.sendall(HTML_HEADER_NOCACHE)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM("info.htm",conn)
	
							conn.send(bytes("<div class='table-responsive'><table class='table'>", "ascii"))
							_statut_brut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name)
							try:
								data = _statut_brut.split(' ')
								_derniere_erreur = m.get_erreur(int(data[2],16))
								if _derniere_erreur != 'NULL':
									conn.send(bytes('<tr><td>Dernière alarme</td><td class="text-right">{}'.format(m.get_erreur(int(data[2],16))), "ascii"))
								conn.send(bytes('<tr><td>Etat P5</td><td class="text-right">{}'.format(m.get_etat(int(data[0],16))), "ascii"))
								conn.send(bytes('<tr><td>Etat précédent P5</td><td class="text-right">{}'.format(m.get_etat(int(data[1],16))), "ascii"))
								conn.send(bytes('<tr><td>Pions</td><td class="text-right">{}'.format(int(data[3],16)), "ascii"))
								conn.send(bytes('<tr><td>Batterie</td><td class="text-right">{} V'.format(data[18]), "ascii"))
								_etat_pion = int(data[11],16)
								if _etat_pion == 1:
									conn.send(bytes('<tr><td>Capteur pion</td><td class="text-right"><span class="badge badge-dark">Metal Absent</span>', "ascii"))
								else:
									conn.send(bytes('<tr><td>Capteur pion</td><td class="text-right"><span class="badge badge-primary">Metal Présent</span>', "ascii"))

								_etat_capot = int(data[12],16)
								if _etat_capot == 1:
									conn.send(bytes('<tr class="table-success"><td>Capteur capot</td><td class="text-right"><span class="badge badge-success">En place</span>', "ascii"))
								else:
									conn.send(bytes('<tr class="table-danger"><td>Capteur capot</td><td class="text-right"><span class="badge badge-danger">En défaut</span>', "ascii"))


								_etat_arret_urgence = int(data[17],16)
								if _etat_arret_urgence == 1:
									conn.send(bytes('<tr class="table-danger"><td>Arrêt Urgence</td><td class="text-right"><span class="badge badge-danger">En Urgence</span>', "ascii"))
								else:
									conn.send(bytes('<tr class="table-success"><td>Arrêt Urgence</td><td class="text-right"><span class="badge badge-success">Position Normal</span>', "ascii"))
								_etat_relais = int(data[13],16)
								if _etat_relais == 1:
									conn.send(bytes('<tr><td>Relais</td><td class="text-right">Activé', "ascii"))
								else:
									conn.send(bytes('<tr><td>Relais</td><td class="text-right">Désactivé', "ascii"))
								conn.send(bytes('<tr><td>i Moteur 1</td><td class="text-right">{}'.format(int(data[4],16)/_CONVERSION_FACTOR_CAN_2_AMPERE), "ascii"))
								conn.send(bytes('<tr><td>i Moteur 2</td><td class="text-right">{}'.format(int(data[5],16)/_CONVERSION_FACTOR_CAN_2_AMPERE), "ascii"))
								conn.send(bytes('<tr><td>Patinage</td><td class="text-right">{} s'.format(int(data[7],16)), "ascii"))
								conn.send(bytes('<tr><td>Temps (Pion)</td><td class="text-right">{} ms'.format(int(data[8],16)*100), "ascii"))
								conn.send(bytes('<tr><td>Temps (Platine)</td><td class="text-right">{} ms'.format(int(data[9],16)*100), "ascii"))
								conn.send(bytes('<tr><td>Temps pelle</td><td class="text-right">{} s'.format(int(data[10],16)), "ascii"))
								if m.Nb_Seconde_Fonctionnement < 60:
									conn.send(bytes('<tr><td>Temps de vol</td><td class="text-right">{} s'.format(m.Nb_Seconde_Fonctionnement), "ascii"))
								else:
									if m.Nb_Seconde_Fonctionnement < 3600:
										conn.send(bytes('<tr><td>Temps de vol</td><td class="text-right">{:.2f} min'.format(m.Nb_Seconde_Fonctionnement/60), "ascii"))
									else:
										conn.send(bytes('<tr><td>Temps de vol</td><td class="text-right">{:.2f} h'.format(m.Nb_Seconde_Fonctionnement/3600), "ascii"))
								_Version = ''
								_Version += '{}'.format(int(data[15],16))
								_Version += ':{}'.format(data[16])
								conn.send(bytes('<tr><td>Version PIC/Wipy</td><td class="text-right">{}'.format(_Version), "ascii"))
								conn.send(bytes('<tr><td>Temps démarrage</td><td class="text-right">{:.2f} s'.format(m.startup_time), "ascii"))
								conn.send(bytes('<tr><td>Wifi <a href="/Wifi">SSID</a></td><td class="text-right">{}'.format(m.wifi_name), "ascii"))
								if hasattr(m, 'wifi_password'):
									if m.wifi_password != '':
										conn.send(bytes('<tr><td>Wifi password</td><td class="text-right">{}'.format(m.wifi_password), "ascii"))
								conn.send(bytes('</table></div></div></div></div></main>\n', "ascii"))				   
								Print_HTM(footer,conn)
							except:
								pass
								
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
							
						elif ibp > 0 : #Page Programme 
							conn.sendall(HTML_HEADER)
							try:
								with open('head.htm', 'r') as html:
									for line in html.readlines():
										conn.send(bytes(line,"ascii"))
							except:
									print("Ouvertude de head.htm impossible!")
							try:
								with open('header.htm', 'r') as html:
									for line in html.readlines():
										conn.send(bytes(line,"ascii"))
							except:
									print("Ouvertude de header.htm impossible!")
							try:
								with open('programme.htm', 'r') as html:
									for line in html.readlines():
										conn.send(bytes(line,"ascii"))
							except:
									print("Ouvertude de programme.htm impossible!")
							try:
								with open('footer.htm', 'r') as html:
									for line in html.readlines():
										conn.send(bytes(line,"ascii"))
							except:
									print("Ouvertude de footer.htm impossible!")
						elif ib3 > 0 : # Page Planning apres enregistrement
							conn.sendall(HTML_HEADER)
							conn.send(bytes("<p>", "ascii"))
							m.requete=request
							Planning_Record(request=m.requete)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('planning.htm',conn)
							Planning_Print(conn)
							Print_HTM(footer,conn)
						elif ibn > 0 : # Page Planning, ouverture depuis le menu principal
							conn.sendall(HTML_HEADER)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('planning.htm',conn)
							Planning_Print(conn)
							Print_HTM(footer,conn)
						elif ibc > 0 : # Page Horloge
							_clock_set = 0
							if request[0:3]!='GET':
								try:
									_h = int(Extract_Data(_planning_brut=request, _type='h', _indice=1))
									print('_h={}'.format(_h))
									_m = int(Extract_Data(_planning_brut=request, _type='m', _indice=1))
									print('_m={}'.format(_m))
									_clock_set = 1

									RTC(datetime=(2018, 1, 1, _h, _m, 0, 0, None)) # <= cette date permettra ultérieurement
								except:
									m.web_debug = 'Exception dans: Extraction Heure et Minute'
									print('m.web_debug = {}\nm.request = {}'.format(m.web_debug, m.request))
									pass
							conn.sendall(HTML_HEADER)
							
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('clock.htm',conn)

							if _clock_set == 1:
								conn.send(bytes('<p>Horloge mis à jour<p><br><br>', "ascii"))
							conn.send(bytes('<input class="form-control col-6" type="number" name="h1" value="{}" min="0" max="23">'.format(localtime()[3]), "ascii"))
							conn.send(bytes('<input class="form-control col-6" type="number" name="m1" value="{}" min="0" max="59"</form></div></div></div></main>'.format(localtime()[4]), "ascii"))
							Print_HTM(footer,conn)
						elif ibo > 0 : # Page Configuration
							_conf_set = 0
							_statut_brut = '{} {} {} {} {}'.format(m.PIC_ASK('S'), m.version, ARRET_URGENCE(), m.batterie(), m.wifi_name)
							data = _statut_brut.split(' ')
							if request[0:3]!='GET':
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
									_d = int(float(Extract_Data(_planning_brut=request, _type='d', _indice=1))) * Facteur_Conversion_Ampere_2_CAN
									if 0<=_d<=255:
										m.Moteur_Bequille_Limite_Courant = _d

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
									_conf_set = 1
									m.PARAM_STORE()
									m.PIC_PARAM_UPDATE()
								except:
									pass
							conn.sendall(HTML_HEADER)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('configuration.htm',conn)
							if _conf_set == 1:
								conn.send(bytes('<p>Configuration mis à jour<p>', "ascii"))
							conn.send(bytes('<p>Consigne Moteur (A):<input type="number" name="m1" value="{}" min="0" max="50">'.format(m.Moteur_X_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))
							conn.send(bytes('<p>Consigne Pelle (A):<input type="number" name="c1" value="{}" min="0" max="50">'.format(m.Moteur_Z_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))
							conn.send(bytes('<p>Seuil Pelle (A):<input type="number" name="s1" value="{}" min="0" max="50">'.format(m.Moteur_Z_Limite_Courant/Facteur_Conversion_Ampere_2_CAN), "ascii"))
							conn.send(bytes('<p>Consigne Bequille (A):<input type="number" name="b1" value="{}" min="0" max="50">'.format(m.Moteur_Bequille_Consigne/Facteur_Conversion_Ampere_2_CAN), "ascii"))
							conn.send(bytes('<p>Seuil Bequille (A):<input type="number" name="d1" value="{}" min="0" max="50">'.format(m.Moteur_Bequille_Limite_Courant/Facteur_Conversion_Ampere_2_CAN), "ascii"))
							conn.send(bytes('<p>Patinage (s):<input type="number" name="p1" value="{}" min="0" max="500">'.format(int(data[7],16)), "ascii"))
							conn.send(bytes('<p>Temps (Pion) (ms):<input type="number" name="i1" value="{}" min="0" max="3000">'.format(int(data[8],16)*100), "ascii"))
							conn.send(bytes('<p>Temps (Platine) (ms):<input type="number" name="l1" value="{}" min="0" max="5000">'.format(int(data[9],16)*100), "ascii"))
							conn.send(bytes('<p>Temps pelle (s):<input type="number" name="e1" value="{}" min="0" max="600">'.format(int(data[10],16)), "ascii"))
							conn.send(bytes('</form></div></div></div></main>', "ascii"))
							Print_HTM(footer,conn)

						elif ibm > 0 : #Page Manuel
							print("Rafraîchissement m")
							conn.sendall(HTML_HEADER)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('manuel.htm',conn)
							Print_HTM(footer,conn)

						elif ibf > 0 : #Page Wifi
							_wifi=0
							print("Rafraîchissement f")
							if request[0:3]!='GET':
								conn.send(bytes('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />', "ascii"))
								_wifi_name = Extract_Data(_planning_brut=request, _type='n', _indice=1)
								_wifi_password = Extract_Data(_planning_brut=request, _type='p', _indice=1)
								_wifi_channel = Extract_Data(_planning_brut=request, _type='c', _indice=1)
								print('nom = {}'.format(_wifi_name))
								print('password = {}'.format(_wifi_password))
								try:
									_wifi_channel = int(_wifi_channel)
									print('channel = {}'.format(_wifi_channel))
								except:
									_wifi_channel = 7
									print('except => channel = {}'.format(_wifi_channel))
								if len(_wifi_name)>0:
									conn.send(bytes('<p>Se connecter au réseau "P5 - {}"'.format(_wifi_name), "ascii"))
								else:
									conn.send(bytes('<p>Se connecter au réseau "P5" (accès libre)'.format(), "ascii"))
								if len(_wifi_password)!=0:
									conn.send(bytes('<p>Mot de passe "{}"'.format(_wifi_password), "ascii"))
								conn.send(bytes('<p><a href="/">Menu Principal</a>', "ascii"))
								_wifi=1
								conn.sendall('\n')
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
									print('Wifi name = ""')
									with open("/flash/wifi_name.txt", "w+") as _f: _f.write('')
									exec('m.wifi_name = "P5"')
									exec('m.wifi_password = ""')

									with open("/flash/wifi_channel.txt", "w+") as _f: _f.write('{}'.format(_wifi_channel))
									exec('m.wifi_channel = {}'.format(_wifi_channel))
								exec('Wifi_Local()')

							else:
								Print_HTM(head,conn)
								Print_HTM(header,conn)
								Print_HTM("wifi.htm",conn)
								Print_HTM(footer,conn)
						elif ibw > 0 : #Page Edit
							_error = 0

							if request[0:3]!='GET':
								print("GET ABSENT = > POST? = {}".format(request[0:2]))
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
										except:
											_error = 1
											pass
									_prgm = _Prgm_Indice
								except:
									pass
							else:
								_prgm ='1'
							conn.sendall(HTML_HEADER)
							Print_HTM(head,conn)
							Print_HTM(header,conn)
							Print_HTM('edit.htm',conn)
							if _error > 0:
								conn.send(bytes("<p>Erreur lors de l'écriture du programme", "ascii"))
							conn.send(bytes('<p><SELECT name="p1" size="1" class="custom-select">', "ascii"))
							for _option in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'Retour'):
								conn.send(bytes('<OPTION{}>{}</OPTION>\n'.format('' if _option!=_prgm else ' selected=""', _option), "ascii"))
							conn.send(bytes('</SELECT>\n', "ascii"))
							conn.send(bytes('<p><TEXTAREA class="form-control" name="d1" rows=20 cols=80>', "ascii"))
							conn.send(bytes('{}'.format(Send_Prgm(_prgm)), "ascii"))
							conn.send(bytes('</TEXTAREA>', "ascii"))
							conn.send(bytes('</form></div></div></div></main>', "ascii"))
							Print_HTM(footer,conn)
						else: #Menu Principal
							m.affiche('Rafraîchissement Menu Principal (else): requete = {}'.format(request))		
							conn.sendall(HTML_HEADER)
							if len(request)>0:
								try:
									with open('head.htm', 'r') as html:
										for line in html.readlines():
											conn.send(bytes(line,"ascii"))
								except:
									print("Ouvertude de head.htm impossible!")										
								try:
									with open("header_mp.htm", 'r') as html:
										
										for line in html.readlines():
											if str('<p id="clock"></p>') in line:										   
												conn.send(bytes('<form action="/Clock" method="post" id="clock"><span class="badge badge-primary">Heure {} : {}:{}</span>'.format(m.wifi_name, localtime()[3], localtime()[4]), "ascii"))
												conn.send(bytes('<input type="hidden" id="h1" name="h1" value="{}" min="0" max="23">'.format(localtime()[3]), "ascii"))
												conn.send(bytes('<input type="hidden" id="m1" name="m1" value="{}" min="0" max="59">'.format(localtime()[4]), "ascii"))
												conn.send(bytes('</form>', "ascii"))
											conn.send(line)
								except:
									print("Envoi AiCmirobot_menu_principal_begin.htm Failed!")
								try:
									with open('menu_principal.htm', 'r') as html:
										for line in html.readlines():
											conn.send(bytes(line,"ascii"))
								except:
									print("Ouvertude de menu_principal.htm impossible!")
								try:
									with open('footer.htm', 'r') as html:
										for line in html.readlines():
											conn.send(bytes(line,"ascii"))
								except:
									print("Ouvertude de footer.htm impossible!")							   
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
