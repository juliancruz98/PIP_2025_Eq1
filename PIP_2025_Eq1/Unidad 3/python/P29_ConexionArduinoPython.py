import serial as controlador

#esto genera el canal de comunicacion y lo inicialiaza
arduino = controlador.Serial("COM7", baudrate=9600, timeout=1)