## Windows
-----
### Requis pour installer un fichier binaire dans le P5
###### - [git bash](https://gitforwindows.org/)
###### - [fwtool-cli](https://docs.pycom.io/advance/cli/)
###### - (Optional) [Atom](https://atom.io/) ou [Visual Studio Code](https://code.visualstudio.com/Download)

-----

### Installer une image P5 sur le module W01

##### Version 39
-----
##### Sur Windows
###### Pour installer le binaire vous devez vous rendre sur P5/Wipy/FWTOOL-CLI/Version_39/win
###### Avant cela, vérifiez que vous avez votre câble FTDI avec vous et branché sur le module W01.
###### Cliquez sur B6.bat
-----
#### Sur Linux
###### Pour installer le binaire vous devez vous rendre sur P5/Wipy/FWTOOL-CLI/Version_39/linux
###### Avant cela, vérifiez que vous avez votre câble FTDI avec vous et branché sur le module W01.
```
sh Create_Binary_Linux_V39.sh
```


-----
###### L'installation se fera en 3 étapes :
###### - Suppression totale des éléments dans le Wipy
###### - Installation du fichier binaire wipy (v1.18.r1)
###### - Installation de la version 39.2
###### Une fois l'installation terminée, redemarrez le module (En coupant l'alimention ou en contactant le bloc SJ1, sur la carte qui est au dessus du Wipy W01)
###### Vous devriez voir la LED3 s'allumer.

