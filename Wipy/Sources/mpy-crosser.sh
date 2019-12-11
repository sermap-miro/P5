#!/bin/bash
mpy-cross AiCwebserver_CMD.py -o lib/AiCwebserver_CMD.mpy
echo AiCwebserver_CMD.mpy done
mpy-cross AiCwebserver.py -o lib/AiCwebserver.mpy
echo AiCwebserver.mpy done
mpy-cross commande.py -o lib/commande.mpy
echo commande.mpy done
mpy-cross config.py -o lib/config.mpy
echo config.mpy done
mpy-cross es.py -o lib/es.mpy
echo es.mpy done
mpy-cross main_metlahome.py -o lib/main_metlahome.mpy
echo main_metlahome.mpy done
mpy-cross mirobot2.py -o lib/mirobot2.mpy
echo mirobot2.mpy done
mpy-cross P4.py -o lib/P4.mpy
echo P4.mpy done
mpy-cross pion.py -o lib/pion.mpy
echo pion.mpy done
mpy-cross wifi.py -o lib/wifi.mpy
echo wifi.mpy done
mpy-cross planning.py -o lib/planning.mpy
echo planning.mpy done