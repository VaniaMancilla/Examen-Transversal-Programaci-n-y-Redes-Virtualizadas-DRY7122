import math

# Coordenadas simples (latitud, longitud)
ciudades = {
    "santiago": (-33.4489, -70.6693),
    "lima": (-12.0464, -77.0428),
    
}

# Velocidades promedio (km/h)
transportes = {
    "auto": 80,
    "bus": 60,
    "avion": 800
}

def calcular_distancia(coord1, coord2):
    # Fórmula simple (no exacta, pero sirve)
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2) * 111

while True:
    origen = input("Ingrese ciudad de origen (o 's' para salir): ").lower()
    if origen == "s":
        print("Saliendo del programa...")
        break

    destino = input("Ingrese ciudad de destino: ").lower()

    if origen not in ciudades or destino not in ciudades:
        print("Ciudad no válida. Intente nuevamente.\n")
        continue

    print("\nMedios de transporte disponibles: auto, bus, avion")
    medio = input("Ingrese medio de transporte: ").lower()

    if medio not in transportes:
        print("Transporte no válido.\n")
        continue

    # Calcular distancia
    distancia_km = calcular_distancia(ciudades[origen], ciudades[destino])
    distancia_millas = distancia_km * 0.621371

    # Calcular tiempo
    velocidad = transportes[medio]
    tiempo_horas = distancia_km / velocidad

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Distancia: {distancia_millas:.2f} millas")
    print(f"Duración aproximada: {tiempo_horas:.2f} horas")

    # Narrativa
    print("\nNarrativa del viaje:")
    print(f"Viajarás desde {origen.capitalize()} hasta {destino.capitalize()} en {medio}.")
    print(f"El viaje cubrirá aproximadamente {distancia_km:.2f} km y tomará cerca de {tiempo_horas:.2f} horas.\n")
