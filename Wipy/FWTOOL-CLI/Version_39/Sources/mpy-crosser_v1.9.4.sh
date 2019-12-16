#!/bin/bash
mpy-cross AiCwebserver_CMD.py -o mpy-files/AiCwebserver_CMD.mpy
echo AiCwebserver_CMD.mpy done
mpy-cross AiCwebserver.py -o mpy-files/AiCwebserver.mpy
echo AiCwebserver.mpy done
mpy-cross commande.py -o mpy-files/commande.mpy
echo commande.mpy done
mpy-cross config.py -o mpy-files/config.mpy
echo config.mpy done
mpy-cross es.py -o mpy-files/es.mpy
echo es.mpy done
mpy-cross main_metlahome.py -o mpy-files/main_metlahome.mpy
echo main_metlahome.mpy done
mpy-cross mirobot2.py -o mpy-files/mirobot2.mpy
echo mirobot2.mpy done
mpy-cross P4.py -o mpy-files/P4.mpy
echo P4.mpy done
mpy-cross pion.py -o mpy-files/pion.mpy
echo pion.mpy done
mpy-cross wifi.py -o mpy-files/wifi.mpy
echo wifi.mpy done
mpy-cross planning.py -o mpy-files/planning.mpy
echo planning.mpy done