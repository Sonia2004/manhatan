import openrouteservice

API_KEY = "5b3ce3597851110001cf6248a9486e7ed3c8400fa3ada5fc9ecc4546"

vehiculos = {
    "auto": {"rendimiento": 12},
    "camioneta": {"rendimiento": 9},
    "camion": {"rendimiento": 5}
}

coordenadas_estados = {
    "Aguascalientes": (-102.2916, 21.8853),
    "Baja California": (-115.4545, 32.6519),
    "Baja California Sur": (-110.3128, 24.1444),
    "Campeche": (-90.5349, 19.8301),
    "Chiapas": (-92.6376, 16.7569),
    "Chihuahua": (-106.0889, 28.6353),
    "CDMX": (-99.1332, 19.4326),
    "Coahuila": (-101.7068, 25.4383),
    "Colima": (-103.7245, 19.2457),
    "Durango": (-104.6554, 24.0277),
    "Estado de México": (-99.7591, 19.3574),
    "Guanajuato": (-101.2843, 21.0190),
    "Guerrero": (-99.9522, 17.5461),
    "Hidalgo": (-98.9785, 20.0911),
    "Jalisco": (-103.3496, 20.6597),
    "Michoacán": (-101.1870, 19.5665),
    "Morelos": (-99.1411, 18.6813),
    "Nayarit": (-104.8717, 21.7514),
    "Nuevo León": (-100.3161, 25.6866),
    "Oaxaca": (-96.7266, 17.0732),
    "Puebla": (-98.2050, 19.0414),
    "Querétaro": (-100.3807, 20.5888),
    "Quintana Roo": (-86.8475, 20.2127),
    "San Luis Potosí": (-100.9857, 22.1518),
    "Sinaloa": (-107.3935, 24.7973),
    "Sonora": (-110.9616, 29.0729),
    "Tabasco": (-92.9222, 17.9905),
    "Tamaulipas": (-98.8197, 24.3088),
    "Tlaxcala": (-98.2192, 19.3189),
    "Veracruz": (-96.1045, 19.1738),
    "Yucatán": (-89.1212, 20.9801),
    "Zacatecas": (-102.5795, 22.7709)
}

def calcular_ruta_y_restricciones(origen, destino, tipo_vehiculo):
    client = openrouteservice.Client(key=API_KEY)

    start_coords = coordenadas_estados.get(origen)
    end_coords = coordenadas_estados.get(destino)

    if not start_coords or not end_coords:
        return None, {"Error": "Estado no encontrado en la lista"}

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
