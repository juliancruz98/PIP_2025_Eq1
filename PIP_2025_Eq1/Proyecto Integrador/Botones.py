import serial
import keyboard

arduino = serial.Serial('COM4', 9600, timeout=1)
last_direction = ""
botones_activos = set()  # Guardamos los botones que están presionados

while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode().strip()

        # --- DIRECCIONES (joystick) ---
        if line in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if line != last_direction:
                # Liberar teclas anteriores
                for key in ['w', 'a', 's', 'd']:
                    keyboard.release(key)

                if line == "UP":
                    keyboard.press('w')
                elif line == "DOWN":
                    keyboard.press('s')
                elif line == "LEFT":
                    keyboard.press('a')
                elif line == "RIGHT":
                    keyboard.press('d')

                last_direction = line

        elif line == "CENTRO":
            for key in ['w', 'a', 's', 'd']:
                keyboard.release(key)
            last_direction = "CENTRO"

        # --- BOTONES A y B (mantener presionados) ---
        elif line == "Z":
            if "z" not in botones_activos:
                keyboard.press("z")
                botones_activos.add("z")

        elif line == "Z_UP":
            keyboard.release("z")
            botones_activos.discard("z")

        elif line == "X":
            if "x" not in botones_activos:
                keyboard.press("x")
                botones_activos.add("x")

        elif line == "X_UP":
            keyboard.release("x")
            botones_activos.discard("x")

        # --- BOTONES Select y Start (solo pulsación rápida) ---
        elif line == "ENTER":
            if "enter" not in botones_activos:
                keyboard.press('enter')
                botones_activos.add("enter")
        elif line == "ENTER_UP":
            keyboard.release('enter')
            botones_activos.discard("enter")

        elif line == "BACKSPACE":
            if "backspace" not in botones_activos:
                keyboard.press('backspace')
                botones_activos.add("backspace")
        elif line == "BACKSPACE_UP":
            keyboard.release('backspace')
            botones_activos.discard("backspace")