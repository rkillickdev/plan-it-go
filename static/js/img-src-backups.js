const destinationImages = document.getElementsByClassName("destination-image")

for (let image of destinationImages ) {
    image.addEventListener("error", (e) => {
        e.target.src = "/static/images/world-map-plane-1500x1000-compress.webp";
        e.onerror = null;
    });
}
