#!/bin/bash
mpy-cross AiCwebserver_CMD.py -o ./AiCwebserver_CMD.mpy
mpy-cross AiCwebserver.py -o ./AiCwebserver.mpy
mpy-cross commande.py -o ./commande.mpy
mpy-cross config.py -o ./config.mpy
mpy-cross es.py -o ./es.mpy
mpy-cross main_metlahome.py -o ./main_metlahome.mpy
mpy-cross mirobot2.py -o ./mirobot2.mpy
mpy-cross P4.py -o ./P4.mpy
mpy-cross pion.py -o ./pion.mpy
mpy-cross wifi.py -o ./wifi.mpy
mpy-cross planning.py -o ./planning.mpy