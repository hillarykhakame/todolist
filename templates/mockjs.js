// Initialize the map and set its view to a chosen geographical coordinates and zoom level
var map = L.map('map').setView([-1.2736, 36.8440], 12);

// Set up the OpenStreetMap tiles using Leaflet
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add markers with their respective popups
let startmarker = L.marker([-1.27429, 36.72339]).addTo(map);
let marker = L.marker([-1.2382688, 36.9123459]).addTo(map);

// Add a popup to the markers
startmarker.bindPopup("<b>Divergent point!</b><br>Start of Nairobi River.").openPopup();
marker.bindPopup("<b>Confluence point!</b><br>Nairobi river.").openPopup();

// Add a new marker at the coordinates (0.2827, 34.7519)
let newMarker = L.marker([0.2827, 34.7519]).addTo(map);

// Add a popup to the new marker
newMarker.bindPopup("<b>New Location!</b><br>Point at 0.2827° N, 34.7519° E.").openPopup();
