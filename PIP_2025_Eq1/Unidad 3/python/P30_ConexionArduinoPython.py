import serial as controlador
#p34

#esto genera el canal de comunicacion y lo inicialiaza
arduino = controlador.Serial("COM7", baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline().decode().strip()
    if cadena != "":
        print(cadena)