import serial as controlador
#p34

#esto genera el canal de comunicacion y lo inicialiaza
arduino = controlador.Serial("COM5", baudrate=9600, timeout=1)

while True:
    accion  = input("Ingresa el valor de accion para el led:")
    arduino.write(accion.encode())#Encode es para caracteres a bytes y el decode de bytes a caracteres