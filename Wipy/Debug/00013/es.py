
import machine


#Entrée
#BP = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
# ARRET_URGENCE = machine.Pin('P17', mode=machine.Pin.IN, pull=None)
ARRET_URGENCE = machine.Pin('P17', mode=machine.Pin.IN, pull=machine.Pin.PULL_DOWN)

#Sortie
#BUZZER = machine.Pin('P21', mode=machine.Pin.OUT)#Version 3.3V
BUZZER = machine.Pin('P19', mode=machine.Pin.OUT)#Version 3.3V
BUZZER(False)


#AV_1 = machine.Pin('P9', mode=machine.Pin.OUT)
#BUZZER_INPUT = machine.Pin('P9', mode=machine.Pin.IN, pull=None)
#BUZZER_INPUT = machine.Pin('P8', mode=machine.Pin.IN, pull=None) # pour SPI

#
# from machine import SPI
# #SPI  pins.
# #SPI_CS   = 'P23'
# SPI_MOSI = 'P10'
# SPI_MISO = 'P11'
# SPI_CLK  = 'P9'
#
#
#
# # SPI_LOW  = 0
# # SPI_HIGH = 1
# #
# # spi_cs = Pin(SPI_CS, mode = Pin.OUT)
# # spi_cs.value(SPI_HIGH)
# #spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=2000000, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))
#
# #spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=100000, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))
# spi = SPI(0, mode=SPI.MASTER, polarity=0, phase=0, baudrate=57600, pins=(SPI_CLK, SPI_MOSI, SPI_MISO))

# this uses the SPI non-default pins for CLK, MOSI and MISO (``P19``, ``P20`` and ``P21``)
#spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P19','P20','P21'))

#
# spi.write(bytes([0x56, 0x34, 0x37]))
# spi.write(bytes([0x56, 0x34, 0x34, 0x37]))
# spi.write(bytes([0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]))
#
#
# #spi.write(bytes([0x53, 0x13])) # "SOmega"
# spi.write(bytes([0x53, 0x0d])) # "S\r"
# spi.write(bytes([0x54])) # "T"
#
# spi.read(4)
#
#
#
#
# spi.write(bytes([0x30]))
# time.sleep(0.1)
# spi.write(bytes([0x31]))
# time.sleep(0.1)
# spi.write(bytes([0x32]))
# time.sleep(0.1)
# spi.write(bytes([0x33]))
# time.sleep(0.1)
# spi.write(bytes([0x34]))
# time.sleep(0.1)
# spi.write(bytes([0x35]))
# time.sleep(0.1)
# spi.write(bytes([0x36]))
# time.sleep(0.1)
# spi.write(bytes([0x37]))
# time.sleep(0.1)
# spi.write(bytes([0x38]))
# time.sleep(0.1)
# spi.write(bytes([0x39]))
# time.sleep(0.1)
