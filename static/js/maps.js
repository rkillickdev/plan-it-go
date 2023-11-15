const mapkey = JSON.parse(document.getElementById('maps-api-key').textContent);

// Load Google Maps API using Dynamic Library Import

(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
          key: mapkey,
          v: "weekly",
          // Use the 'v' parameter to indicate the version to use (weekly, beta, alpha, etc.).
          // Add other bootstrap parameters as needed, using camel case.
        });

const latitude = JSON.parse(document.getElementById('latitude').textContent);
const longitude = JSON.parse(document.getElementById('longitude').textContent);
const placeName = JSON.parse(document.getElementById('place-name').textContent);

let numLat = parseFloat(latitude);
let numLong = parseFloat(longitude);

// Initialize and add the map
let map;

async function initMap() {
  const position = { lat: numLat, lng: numLong };
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    zoom: 16,
    center: position,
    mapId: "place-detail-map",
  });

  // Marker added and named
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: placeName,
  });
}

initMap();