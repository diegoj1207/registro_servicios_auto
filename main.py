# Importo mis funciones de servicios
import servicios

# Para guardar log de lo que pasa
import logging

# Para que se vea con color en consola
from colorama import init, Fore

# Arranco colorama, autoreset así no se mezclan colores
init(autoreset=True)

# Config de log, guarda en archivo registro.log
logging.basicConfig(filename="registro.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Menú principal, muestra opciones
def menu():
    while True:
        print(Fore.LIGHTCYAN_EX + "\n=== MENÚ REGISTRO DE SERVICIOS AUTO ===")
        print(Fore.YELLOW + "1. Agregar servicio")
        print(Fore.YELLOW + "2. Listar servicios")
        print(Fore.YELLOW + "3. Marcar servicio como pagado")
        print(Fore.YELLOW + "4. Eliminar servicio")
        print(Fore.YELLOW + "5. Salir")
        print(Fore.LIGHTBLACK_EX + "Elegí opción del 1 al 5 👇")

        # Pido opción al usuario
        opcion = input(Fore.CYAN + "Opción: ")

        if opcion == "1":
            # Llama función para agregar servicio
            servicio = servicios.agregar_servicio()
            logging.info(f"Servicio agregado: {servicio}")
        elif opcion == "2":
            # Llama función para ver lista
            servicios.listar_servicios()
        elif opcion == "3":
            # Marca como pagado
            servicio = servicios.marcar_pagado()
            if servicio:
                logging.info(f"Servicio pagado: {servicio}")
        elif opcion == "4":
            # Elimina uno
            servicio = servicios.eliminar_servicio()
            if servicio:
                logging.info(f"Servicio eliminado: {servicio}")
        elif opcion == "5":
            print(Fore.LIGHTBLUE_EX + "\nGracias por usar el registro 🚗")
            break
        else:
            print(Fore.RED + "Opción no válida.")

# Si corre directo el archivo, arranca el menú
if __name__ == "__main__":
    menu()
