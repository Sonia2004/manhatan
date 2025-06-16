from flask import Flask, render_template, request, jsonify
from utils import calcular_ruta_y_restricciones
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    origen = data.get("origen")
    destino = data.get("destino")
    tipo_vehiculo = data.get("tipoVehiculo", "auto")

    try:
        ruta_geojson, restricciones = calcular_ruta_y_restricciones(origen, destino, tipo_vehiculo)
        return jsonify({"ruta": ruta_geojson, "restricciones": restricciones})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
