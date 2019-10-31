#!/bin/bash
../linux/mpy-cross_littlefs AiCwebserver_CMD.py -o lib/AiCwebserver_CMD.mpy
../linux/mpy-cross_littlefs AiCwebserver.py -o lib/AiCwebserver.mpy
../linux/mpy-cross_littlefs commande.py -o lib/commande.mpy
../linux/mpy-cross_littlefs config.py -o lib/config.mpy
../linux/mpy-cross_littlefs es.py -o lib/es.mpy
#../linux/mpy-cross_littlefs main_metlahome.py -o lib/main_metlahome.mpy
../linux/mpy-cross_littlefs memory.py -o lib/memory.mpy
../linux/mpy-cross_littlefs mirobot2.py -o lib/mirobot2.mpy
../linux/mpy-cross_littlefs P4.py -o lib/P4.mpy
../linux/mpy-cross_littlefs pion.py -o lib/pion.mpy
../linux/mpy-cross_littlefs wifi.py -o lib/wifi.mpy
../linux/mpy-cross_littlefs planning.py -o lib/planning.mpy
