// Initialize the map
var map = L.map('map').setView([-1.2736, 36.8440], 12);

// Set up the OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Create a red marker icon
var redIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
    iconSize: [25, 41],  // Size of the icon
    iconAnchor: [12, 41], // Anchor of the icon (point of the icon that is anchored to the marker's location)
    popupAnchor: [1, -34], // Offset for the popup
    shadowSize: [41, 41]  // Size of the shadow
});

// Add the red marker at the initial position
var initialMarker = L.marker([-1.2736, 36.8440], { icon: redIcon }).addTo(map);
initialMarker.bindPopup("<b>Initial Position</b><br>This is the center of the map.").openPopup();

// Fetch coordinates from the server
fetch('/api/coordinates/')
    .then(response => response.json())
    .then(data => {
        data.forEach(point => {
            // Add a marker for each point
            const marker = L.marker([parseFloat(point.lat), parseFloat(point.long)]).addTo(map);
            marker.bindPopup(`<b>${point.projectTitle}</b><br>${point.description}`).openPopup();
        });
    })
    .catch(error => console.error('Error fetching coordinates:', error));
