import json
import os
from datetime import datetime  # Para sacar fecha actual
from colorama import Fore

SERVICIOS_FILE = "servicios.json"  # Nombre del archivo para guardar datos

# Carga lista de servicios si hay archivo
def cargar_servicios():
    if not os.path.exists(SERVICIOS_FILE):
        return []
    with open(SERVICIOS_FILE, "r") as file:
        return json.load(file)

# Guarda lista de servicios en archivo
def guardar_servicios(servicios):
    with open(SERVICIOS_FILE, "w") as file:
        json.dump(servicios, file, indent=4)

# Agrega nuevo servicio con datos
def agregar_servicio():
    servicios = cargar_servicios()
    nuevo_id = 1 if not servicios else servicios[-1]["id"] + 1

    marca = input(Fore.CYAN + "Marca del auto: ")
    modelo = input(Fore.CYAN + "Modelo del auto: ")
    detalle = input(Fore.CYAN + "Detalle del servicio (qué se va a hacer): ")
    costo = input(Fore.CYAN + "Costo estimado en $: ")

    # Fecha de hoy
    fecha_actual = datetime.now().strftime("%Y-%m-%d")

    nuevo = {
        "id": nuevo_id,
        "marca": marca,
        "modelo": modelo,
        "detalle": detalle,
        "costo": costo,
        "fecha": fecha_actual,
        "estado": "pendiente"
    }

    servicios.append(nuevo)
    guardar_servicios(servicios)
    print(Fore.GREEN + "✅ Servicio agregado.")
    return nuevo

# Muestra lista de todos los servicios
def listar_servicios():
    servicios = cargar_servicios()
    if not servicios:
        print(Fore.YELLOW + "No hay servicios guardados.")
        return

    total = 0
    for s in servicios:
        color_estado = Fore.GREEN if s["estado"] == "pagado" else Fore.RED
        print(Fore.WHITE + f"ID: {s['id']} | Auto: {s['marca']} {s['modelo']} | Fecha: {s['fecha']}")
        print(Fore.WHITE + f"Detalle: {s['detalle']} | Costo: ${s['costo']} | {color_estado}Estado: {s['estado']}")
        print("-" * 40)
        try:
            total += float(s["costo"])
        except:
            pass  # Si no es número ignora

    print(Fore.LIGHTBLUE_EX + f"Total estimado: ${total}")

# Marca servicio como pagado
def marcar_pagado():
    servicios = cargar_servicios()
    try:
        id_buscar = int(input(Fore.CYAN + "ID a marcar como pagado: "))
    except ValueError:
        print(Fore.RED + "No es número.")
        return

    for s in servicios:
        if s["id"] == id_buscar:
            s["estado"] = "pagado"
            guardar_servicios(servicios)
            print(Fore.GREEN + "✅ Servicio marcado como pagado.")
            return s

    print(Fore.RED + "No encontré ese ID.")

# Elimina un servicio por ID
def eliminar_servicio():
    servicios = cargar_servicios()
    try:
        id_buscar = int(input(Fore.CYAN + "ID a eliminar: "))
    except ValueError:
        print(Fore.RED + "No es número.")
        return

    for s in servicios:
        if s["id"] == id_buscar:
            servicios.remove(s)
            guardar_servicios(servicios)
            print(Fore.GREEN + "✅ Servicio eliminado.")
            return s

    print(Fore.RED + "No encontré ese ID.")
