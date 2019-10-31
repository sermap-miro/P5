#!/bin/bash
mpy-cross AiCwebserver_CMD.py -o lib/AiCwebserver_CMD.mpy
mpy-cross AiCwebserver.py -o lib/AiCwebserver.mpy
mpy-cross commande.py -o lib/commande.mpy
mpy-cross config.py -o lib/config.mpy
mpy-cross es.py -o lib/es.mpy
#mpy-cross main_metlahome.py -o lib/main_metlahome.mpy
mpy-cross mirobot2.py -o lib/mirobot2.mpy
mpy-cross P4.py -o lib/P4.mpy
mpy-cross pion.py -o lib/pion.mpy
mpy-cross wifi.py -o lib/wifi.mpy
mpy-cross planning.py -o lib/planning.mpy
