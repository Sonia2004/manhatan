import openrouteservice

API_KEY = "5b3ce3597851110001cf6248a9486e7ed3c8400fa3ada5fc9ecc4546"

vehiculos = {
    "auto": {"rendimiento": 12},
    "camioneta": {"rendimiento": 9},
    "camion": {"rendimiento": 5}
}

coordenadas_estados = {
    "Yucatán": (-89.1212, 20.9801),
    "Chiapas": (-92.6376, 16.7569),
    "CDMX": (-99.1332, 19.4326),
    "Jalisco": (-103.3496, 20.6597),
    "Nuevo León": (-100.3161, 25.6866)
}

def calcular_ruta_y_restricciones(origen, destino, tipo_vehiculo):
    client = openrouteservice.Client(key=API_KEY)

    start_coords = coordenadas_estados[origen]
    end_coords = coordenadas_estados[destino]

    # Solicita ruta
    route = client.directions(
        coordinates=[start_coords, end_coords],
        profile="driving-car",
        format="geojson"
    )

    distance_km = route['features'][0]['properties']['summary']['distance'] / 1000
    duration_hr = route['features'][0]['properties']['summary']['duration'] / 3600

    rendimiento = vehiculos[tipo_vehiculo]["rendimiento"]
    gasolina_l = distance_km / rendimiento
    costo_estimado = gasolina_l * 23.5

    restricciones = {
        "Distancia total (km)": round(distance_km, 2),
        "Tiempo estimado (hrs)": round(duration_hr, 2),
        "Gasolina estimada (L)": round(gasolina_l, 2),
        "Costo estimado (MXN)": round(costo_estimado, 2),
        "Riesgo climático": "Bajo"
    }

    return route, restricciones
