#!/bin/bash

mpy-cross AiCwebserver_CMD.py
mv  AiCwebserver_CMD.mpy ./MPYFILES
mpy-cross AiCwebserver.py 
mv AiCwebserver.mpy ./MPYFILES
mpy-cross commande.py 
mv commande.mpy ./MPYFILES
mpy-cross config.py 
mv config.mpy  ./MPYFILES
mpy-cross es.py 
mv es.mpy ./MPYFILES
mpy-cross main_metlahome.py 
mv main_metlahome.mpy ./MPYFILES
mpy-cross mirobot2.py 
mv mirobot2.mpy ./MPYFILES
mpy-cross P4.py 
mv P4.mpy ./MPYFILES
mpy-cross pion.py 
mv pion.mpy ./MPYFILES
mpy-cross wifi.py 
mv wifi.mpy ./MPYFILES

