let soloImages = document.getElementsByClassName("image-solo");
let modalSoloImage = document.getElementById("solo-modal-image")

for (let image of soloImages) {
    image.addEventListener("click", (e) => {
        let imageUrl = e.target.getAttribute("src");
        modalSoloImage.src = imageUrl;

    });
}



// var deleteButtons = document.getElementsByClassName("btn-delete");
// var ImageDeleteConfirm = document.getElementById("image-delete-confirm");

// for (let button of deleteButtons) {
//     button.addEventListener("click", (e) => {
//         let imageId = e.target.getAttribute("image_id");
//         ImageDeleteConfirm.href = `delete_image/${imageId}`;
//     });
// }