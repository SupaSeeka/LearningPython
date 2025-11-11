const map = L.map('map').setView([52.2053, 0.1218], 14);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; OpenStreetMap contributors',
}).addTo(map);

const infoPanel = document.getElementById('info');

const locations = [
  { name: 'Corpus Christi Clock', coords: [52.203747, 0.117628], description: "C'est le Corpus Christi Clock. C'est très beau.", image: 'corpusClock.jpg' },
  { name: 'Five Blends Coffee House', coords: [52.200956, 0.134564], description: "Café du 'Five Blends'. C'est un bon café. J'adore le café au lait et le croissant.", image: 'fiveBlends.jpg' },
  { name: 'Kings College Chapel', coords: [52.2048, 0.1165], description: "Eglise du `Kings College`. C'est magnifique et grand.", image: 'kingsCollegeChapel.webp' },
  { name: 'Le Hôpital de Addenbrooke', coords: [52.1747, 0.1399], description: "C'est l'hôpital de Addenbrookes. C'est mal.", image: 'addenbrookes.jpg' },
  { name: 'Vanderlyle', coords: [52.200999, 0.134478], description: "C'est le restaurant Vanderlyle. C'est le Michelin Star et c'est très bon", image: 'vanderlyle.jpg' },
  { name: 'The Eagle Pub', coords: [52.20406, 0.117926], description: "C'est le pub 'The Eagle'. Le biere est fantastique", image: 'eagle.jpg' },
  { name: 'Gonville and Caius College', coords: [52.206019, 0.117212], description: "C'est le Gonville and Caius College. C'est le college de moi grandpere.", image: 'gonvilleAndCaius.jpg' },
  { name: 'Cambridge University Library', coords: [52.205082, 0.108426], description: "C'est la bibliotheque de l'université de Cambridge.", image: 'cul.avif' }
];

// Add markers and click events to update sidebar
locations.forEach((loc) => {
  const marker = L.marker(loc.coords).addTo(map);
  marker.on('click', () => {
    infoPanel.innerHTML = `
      <h2>${loc.name}</h2>
      <p>${loc.description}</p>
      <img src="${loc.image}" alt="${loc.name}" style="max-width:100%; height:300px; object-fit:cover; border-radius:5px; margin-top:10px;">
      <p><strong>Coordinates:</strong> ${loc.coords[0].toFixed(5)}, ${loc.coords[1].toFixed(5)}</p>
    `;
  });
});

// Print coordinates when map is clicked
map.on('click', function(e) {
  console.log('You clicked the map at: ', e.latlng.lat, e.latlng.lng);
});

