import serial as controlador
#p34

#esto genera el canal de comunicacion y lo inicialiaza
arduino = controlador.Serial("COM7", baudrate=9600, timeout=1)

lectura=0
tot_lectura=22

datos= []
while lectura<tot_lectura:
    cadena = arduino.readline().decode().strip()
    if cadena != " ":
        print(cadena)
        datos.append(cadena)
        lectura+=1


datos=[int(i) for i in datos]
print(datos)