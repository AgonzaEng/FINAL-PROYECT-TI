# PROGRAMA PARA SISTEMATIZAR EL MENU DE UN RESTAURANTE

import time

desayuno = 0
almuerzo = 0
cena = 0

nombre_restaurante = """

    █▀▀ █▀▀ █▄░█ ▀█▀ █▀█ ▄▀█ █░░
    █▄▄ ██▄ █░▀█ ░█░ █▀▄ █▀█ █▄▄

                ᴰᴱ ⱽᴵᴸᴸᴬ

"""

def mostrar_menu_principal():
    print(nombre_restaurante)
    time.sleep(2)
    print("=========================================")
    print("****************** 𝐌𝐄𝐍𝐔 ******************")
    print("=========================================")
    print("A / DESAYUNO")
    print("B / ALMUERZO")
    print("C / CENA")
    print("-----------------------------------------")
    print("D / PAGAR Y SALIR")
    print("E / CANCELAR")
    print("=========================================\n")

def mostrar_menu_desayuno():
    print("\n=========================================")
    print("============== DESAYUNO =================")
    print("=========================================")
    print("A | Café | S/ 4.50")
    print("B | Capuchino | S/ 5.00")
    print("C | Chocolate | S/ 5.00")
    print("D | Jugo de fresas | S/ 7.00")
    print("E | Jugo de especial | S/ 8.00")
    print("F | Jugo de papaya | S/ 7.00")
    print("G | Pan con chicharrón | S/ 6.00")
    print("H | Pan con jamón y queso | S/ 6.00")
    print("I | Pan con pavo | S/ 6.00")
    print("J | Tamal de pollo | S/ 5.00")
    print()
    print("Z | Volver al menú principal")
    print("=========================================\n")

def mostrar_menu_almuerzo():
    print("\n=========================================")
    print("============== ALMUERZO =================")
    print("=========================================")
    print("A | Causa | S/ 6.00")
    print("B | Papa rellena | S/ 5.00")
    print("C | Arroz con pollo | S/ 9.00")
    print("D | Chanfainita | S/ 8.00")
    print("E | Tallarín saltado | S/ 9.00")
    print("F | Lomo saltado | S/ 12.00")
    print("G | Seco con frejoles | S/ 10.00")
    print("H | Pescado frito | S/ 10.00")
    print()
    print("Z | Volver al menú principal")
    print("=========================================\n")

def mostrar_menu_cena():
    print("\n=========================================")
    print("================= CENA ==================")
    print("=========================================")
    print("A | Caldo de gallina | S/ 7.50")
    print("B | Caldo de mote | S/ 7.50")
    print("C | Salchipapas | S/ 8.00")
    print("D | Broaster | S/ 10.00")
    print("E | Pollo a la parrilla | S/ 10.00")
    print("F | Chaufa | S/ 9.00")
    print("G | Mostrito | S/ 10.00")
    print("H | Bistec a lo pobre | S/ 12.00")
    print()
    print("Z | Volver al menú principal")
    print("=========================================\n")

while True:
    mostrar_menu_principal()
    eleccion = input("Elige una opción del menú (A, B, C, D o E): ")

    if eleccion.lower() == "a":
        mostrar_menu_desayuno()

        while True:
            eleccion_comida = input("Elige tu desayuno según la letra asignada (o 'Z' para volver al menú principal): ")

            if eleccion_comida.lower() == 'z':
                break
            
            if eleccion_comida.lower() == "a":
                desayuno += 4.50
            elif eleccion_comida.lower() == "b":
                desayuno += 5.00
            elif eleccion_comida.lower() == "c":
                desayuno += 5.00
            elif eleccion_comida.lower() == "d":
                desayuno += 7.00
            elif eleccion_comida.lower() == "e":
                desayuno += 8.00
            elif eleccion_comida.lower() == "f":
                desayuno += 7.00
            elif eleccion_comida.lower() == "g":
                desayuno += 6.00
            elif eleccion_comida.lower() == "h":
                desayuno += 6.00
            elif eleccion_comida.lower() == "i":
                desayuno += 6.00
            elif eleccion_comida.lower() == "j":
                desayuno += 5.00
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

    elif eleccion.lower() == "b":
        mostrar_menu_almuerzo()
        while True:
            eleccion_comida = input("Elige tu almuerzo según la letra asignada (o 'Z' para volver al menú principal): ")

            if eleccion_comida.lower() == 'z':
                break

            if eleccion_comida.lower() == "a":
                almuerzo += 6.00
            elif eleccion_comida.lower() == "b":
                almuerzo += 5.00
            elif eleccion_comida.lower() == "c":
                almuerzo += 9.00
            elif eleccion_comida.lower() == "d":
                almuerzo += 8.00
            elif eleccion_comida.lower() == "e":
                almuerzo += 9.00
            elif eleccion_comida.lower() == "f":
                almuerzo += 12.00
            elif eleccion_comida.lower() == "g":
                almuerzo += 10.00
            elif eleccion_comida.lower() == "h":
                almuerzo += 10.00
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

    elif eleccion.lower() == "c":
        mostrar_menu_cena()
        while True:
            eleccion_comida = input("Elige tu cena según la letra asignada (o 'Z' para volver al menú principal): ")

            if eleccion_comida.lower() == 'z':
                break

            if eleccion_comida.lower() == "a":
                cena += 7.50
            elif eleccion_comida.lower() == "b":
                cena += 7.50
            elif eleccion_comida.lower() == "c":
                cena += 8.00
            elif eleccion_comida.lower() == "d":
                cena += 10.00
            elif eleccion_comida.lower() == "e":
                cena += 10.00
            elif eleccion_comida.lower() == "f":
                cena += 9.00
            elif eleccion_comida.lower() == "g":
                cena += 10.00
            elif eleccion_comida.lower() == "h":
                cena += 12.00
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
    
    elif eleccion.lower() == "d":
        if desayuno == 0 and almuerzo == 0 and cena == 0:
            print("No ha realizado ninguna compra.")
        else:
            subtotal = cena + almuerzo + desayuno
            igv = round(subtotal * 0.18, 2)
            total = round(subtotal + igv, 2)

            print("\n🇨​​​​​🇦​​​​​🇷​​​​​🇬​​​​​🇦​​​​​🇳​​​​​🇩​​​​​🇴​​​​​...\n")
            time.sleep(3)

            print("*******IMPRIMIENDO BOLETA DE VENTA*********")
            time.sleep(1)
            print("-------------------------------------------")
            print("             BOLETA DE VENTA ")
            print("-------------------------------------------")
            print("SUBTOTAL : S/.", subtotal)
            print("IGV : S/.", igv)
            print("TOTAL : S/.", total)
            print("-------------------------------------------")
            print()
            print("    ＧＲＡＣＩＡＳ ＰＯＲ ＳＵ ＣＯＭＰＲＡ")

        break
    elif eleccion.lower() == "e":
        print("Pedido cancelado.")
        exit()

    else:
        print("Opción inválida. Por favor, elige A, B, C, D o E.")
