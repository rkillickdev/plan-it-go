let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 40.78343500, lng: -73.96625000 },
    zoom: 10,
  });
}

initMap();