let map = L.map('map').setView([23.6345, -102.5528], 5);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

let layerRuta = null;

function calcularRuta() {
    const origen = document.getElementById("origen").value;
    const destino = document.getElementById("destino").value;
    const tipoVehiculo = document.getElementById("tipoVehiculo").value;

    fetch("/optimize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ origen, destino, tipoVehiculo })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) return alert("Error: " + data.error);

        if (layerRuta) map.removeLayer(layerRuta);
        layerRuta = L.geoJSON(data.ruta, { style: { color: "red" }}).addTo(map);
        map.fitBounds(layerRuta.getBounds());

        let infoHTML = "<h3>Restricciones Calculadas</h3><ul>";
        for (let key in data.restricciones) {
            infoHTML += `<li><strong>${key}:</strong> ${data.restricciones[key]}</li>`;
        }
        infoHTML += "</ul>";
        document.getElementById("info").innerHTML = infoHTML;
    });
}
