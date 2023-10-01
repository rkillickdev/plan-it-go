var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let imageId = e.target.getAttribute("image_id");
        deleteConfirm.href = `delete_image/${imageId}`;
    });
}