const mapkey = JSON.parse(document.getElementById('maps-api-key').textContent);

// Load Google Maps API using Dynamic Library Import

(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
          key: mapkey,
          v: "weekly",
        });

// Parse variables received from HTML Template

const latitude = JSON.parse(document.getElementById('latitude').textContent);
const longitude = JSON.parse(document.getElementById('longitude').textContent);
let numLat = parseFloat(latitude);
let numLong = parseFloat(longitude);
const geoList = JSON.parse(document.getElementById('geo-list').innerHTML);

async function initMap() {
    // Request required libraries.
    const { Map, InfoWindow } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary(
      "marker",
    );
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: { lat: numLat, lng: numLong },
      mapId: "trip-detail-map",
    });
    const infoWindow = new google.maps.InfoWindow({
      content: "",
      disableAutoPan: true,
    });
    // Create an array of alphabetical characters used to label the markers.
    const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    const markers = locations.map((position, i) => {
      const label = labels[i % labels.length];
      const pinGlyph = new google.maps.marker.PinElement({
        glyph: label,
        glyphColor: "white",
      });
      const marker = new google.maps.marker.AdvancedMarkerElement({
        position,
        content: pinGlyph.element,
      });
  
      // open info window when marker is clicked
      marker.addListener("click", () => {
        infoWindow.setContent(position.place);
        infoWindow.open(map, marker);
      });
      return marker;
    });
  
    // Add a marker clusterer to manage the markers.
    const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });
}

const locations = geoList;
  
initMap();
    
 
    






    