# P5

Source du programme pour le pic 18F4431 et le wipy du P5

#Wipy
Le numéro de version doit bien être mis à jour dans le fichier mirobot2.py pour correspondre à la version affiché:
self.version = x


# Version 39.1 - 39.2:
###### Réajustement automatique de la boite de dialogue
```
$.fn.atcenter = function () {
    this.css({
        'margin-top': -this.height() / 2 + "px",
        'margin-left': -this.width() / 2 + "px",
    })
}
```
###### Indicateur de connexion
 Partie en JS :
```
function linked(connected){
    var Lscreen = window.innerWidth;
    if (!connected){
    
        if (Lscreen < 1200){
            document.getElementById("etat_co").innerHTML = "Non connecté";
        }
        else{
            document.getElementById("etat_co").innerHTML = "";  
        }
        document.getElementById("thetitle").innerHTML = "Non connecté";
        }
    else {
        if (Lscreen < 1200){
            document.getElementById("etat_co").innerHTML = nom_wifi;
            }
        else{
            document.getElementById("etat_co").innerHTML = "";
            }
        document.getElementById("thetitle").innerHTML = nom_wifi;
}
}
```

###### Mot de passe pour le calibrage

#Version 39:
###### Mise en place Méthode MVC
###### Serveur se contentant d'envoyer quelques données
###### Echange de données via JSON
###### Utilisation JQuery
###### Dynamisation du site web
###### Suppression de la mise en cache
###### Affichage d'une seule page internet
###### Changement dynamique via main.min.js comportant les pages html.
###### Graphisme revu

#Version 38:
###### Reprise du graphisme de VT-Design(Bootstrap)
###### Correction graphique VT-Design 
###### En tête et Bas de page mis en commun sur tout le site
###### Compabtibilité sur smarthphone, PC, tablettes


#Version 37:
###### Equivalent à version 36

#Version 36:
###### Modification du fichier html correspondant à l'index du site web, pour utiliser un seul bouton de mise à jour de l'horloge

#Version 35:
###### Ajout dans la mémoire "dur" du P5 le nombre de collision capot autorisé avant mise en défaut.

#Version 34:
###### Correction d'un bug dans le fichier commande.py: il n'y avait pas l'import du Thread pour le threading de l'alarme

#Version 33:
###### Ajout du verrou de fonctionnement, plus une commande disponible sur le port 8111 qui renvoi :
```
elif cmd[0] == 80: #caractère "P"
    elif cmd[0] == 80: #caractère "P"
        _Statut = '{} {} {}'.format(m.Run_Prgm, prgm_planifier, m.verrou)
```
###### Fichiers modifiés: main.py (P4.py), mirobot2.py, AiCwebserver.py
    

#Version 32:
###### Tentative de compréhension du défaut de la page de configuration de l'horloge depuis les naviguateurs SAFARI
###### En fait SAFARI ne semble pas envoyé les datas dans sa réponse par un POST
 ```
 request_safari = 'POST /Clock HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2\r\nContent-Length: 9\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nOrigin: http://192.168.4.1\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: http://192.168.4.1/Clock\r\nAccept-Language: fr-FR\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
  request_firefox = 'POST /Clock HTTP/1.1\r\nHost: 192.168.4.1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nReferer: http://192.168.4.1/Clock\r\nConnection: keep-alive\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 9\r\n\r\nh1=3&m1=9'
 ```
######     Il en résulte que SAFARI envoi bel et bien les datas du POST, seulement, il le fait dans un second segment TCP, cela nous oblige à écouter de nouveau la socket s'il s'agit d'un POST d'un navigateur SAFARI
=> cela résoud le problème de SAFARI sur ordinateur, mais pas sur iPhone.

#Version 31: # 13 Novembre 2018
###### Si calibration se passe mal alors on ne recoit plus de statut du P5, dans la fonction batterie une exception à été ajouté qui fait que lorsque la mesure de la batterie se passe mal (par exemple avec une division par zéro) alors on affiche une tension nulle.
###### Ajout d'un seuil pour la béquille (Limite courant)

#Version 30:
###### Problème des commentaires dans l'édition des programmes => le caractère dièse ("#") apparait sous la forme %23 le caractère espace apparait sous la forme d'un plus ("+")

#Version 29:
###### Ajout du paramètre de channel pour le wifi

#Version 28:
###### Temps de vol affichage en fonction s/min/h: correction du bug qui affiche la mauvaise valeurs dans les informations:
 ca affichait toujours l'unité en seconde!

#Version 27:
###### Temps de démarrage dans le menu Information: 14,19 secondes

#Version 26:
###### Mesure du temps de démarrage avec son affichage dans la page information

#Version 25:
###### m.request émis de nouveau si mauvaise écoute de la requete <= abandonné, ne résolvait pas le problème avec chrome

#Version 24:
###### s.listen(0) dans AiCwebserver.py

#Version 23:
###### Wifi_Connect (temps de pause de 4 seconde pour laisser au wipy le temps de se connecter)

#Version 22:
###### Réduction en taille de main.py => pour un upgrade plus rapide

#Version 21:
###### L'application P4 n'était plus compatible pour la remonté du Statut (à cause de la nouvelle facon d'accéder au paramétrage du Wifi), cela est modifier en conséquence

#Version 20:
###### Suppression de print dans AiCwebserver.py

#Version 19:
###### Version compilé pour le wipy

#Version 18:
###### Amélioration de l'application pour la mise à jour du Wipy (problème d'utf-8 entre python 2.7 et 3.x). (Il y a peut etre des problèmes sur les versions précédentes de par ce fait la... qui pourtant n'existait pas auparavant! Bizarre)

#Version 17:
###### Ajout du password pour le wifi
###### Modification des liens du site internet pour que ca pointe en local et non en fixant l'adresse ip (dans le cas éventuel ou le wipy viendrait se connecter a un réseau wifi existant)

#Version 16:
###### Bug accès site web avec déconnexion: https://forum.pycom.io/topic/1747/urequests-with-ussl-causes-an-oserror/4
###### Fermeture de la socket dans tous les cas => socket.close() et gc.collect() pour vider le collecteur python


#Version 15:
###### Ajout de l'icone du site web embarqué
###### Ajout de la commande Interrupteur qui permet d'activer ou de désactiver le relais
###### Ajout du temps de fonctionnement et de maintenance sur la page Information


#Version 14: version en fonctionnement au Tilleret


#Version 9:
###### Ajout de nouveau intitulé d'alarme:
```
9 : 'Overload_Cap_1_1'
10 : 'Overload_Cap_1_3'
```



#Version 6:
#18 Avril

##### Multitas:
###### Le paramètre dans les programmes concernant le nombre de seconde de patinage est désormais le nombre de centaine de milliseconde
###### Comme Quentin l'a proposé, lorsque le mirobot est en multitas, on défini le temps de platine égal au temps de patinage passé en paramètre


#Version 7:
#14 Juin

###### Vérification de l'horloge au démarrage du lopy
###### Comptage des heures de fonctionnement