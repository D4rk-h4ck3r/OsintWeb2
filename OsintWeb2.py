# creado por Hans Saldias
# 24/11/2025
# script para buscar informacion en web de fuentes abiertas
import os

def mostrar_menu():
    print("=== Menú de Opciones de OSINT ===")
    print("1. OSINT Framework")
    print("2. Maltego")
    print("3. Shodan")
    print("4. Censys")
    print("5. Recon-ng")
    print("6. Salir")

def abrir_herramienta(opcion):
    if opcion == '1':
        os.system("termux-open https://osintframework.com")
    elif opcion == '2':
        os.system("termux-open https://www.maltego.com")
    elif opcion == '3':
        os.system("termux-open https://www.shodan.io")
    elif opcion == '4':
        os.system("termux-open https://censys.io")
    elif opcion == '5':
        os.system("termux-open https://recon-ng.com")
    elif opcion == '6':
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida.")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")
    abrir_herramienta(opcion)
