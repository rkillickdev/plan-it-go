// Referenced the following article when finding a solution for inserting
// default images where external image links return an error:
// https://dillionmegida.com/p/default-image-src/

const images = document.getElementsByTagName("img");

for (let image of images ) {
    image.addEventListener("error", (e) => {
        e.target.src = "/static/images/world-map-plane-1500x1000-compress.webp";
        e.onerror = null;
    });
}

