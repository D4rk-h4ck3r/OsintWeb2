# Nombre del script: mi_script.py
# Descripción: Osint web esta basado a abrir web de informacion de fuentes abiertas.
# Autor: Hans Saldias
# Fecha: 24 de noviembre de 2025

import webbrowser

def mostrar_menu():
    print("\033[33m=== Menú de Opciones de OSINT ===\n \033[32m== Creted by: D4rk-h4ck3r ==\033[0m")
    print("\033[33m1. OSINT Framework")
    print("2. Maltego")
    print("3. Shodan")
    print("4. Censys")
    print("5. Recon-ng")
    print("0. Exit")

def abrir_url(opcion):
    urls = {
        "1": "https://osintframework.com/",
        "2": "https://www.paterva.com/web7/",
        "3": "https://www.shodan.io/",
        "4": "https://censys.io/",
        "5": "https://github.com/lanmaster53/recon-ng"
    }
    
    if opcion in urls:
        webbrowser.open(urls[opcion])
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "0":
            print("Saliendo del programa...")
            break
        
        abrir_url(opcion)

if __name__ == "__main__":
    main()
