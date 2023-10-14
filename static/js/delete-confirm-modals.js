// Delete Confirm For Images

var deleteButtons = document.getElementsByClassName("btn-delete");
var ImageDeleteConfirm = document.getElementById("image-delete-confirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let imageId = e.target.getAttribute("image_id");
        ImageDeleteConfirm.href = `delete_image/${imageId}`;
    });
}

// Delete Confirm For Trip Places

let deletePlannerItems = document.getElementsByClassName("delete-planner-item");
let itemDeleteForm = document.getElementById("item-delete-form");   // SET FORM ID AS THIS
let itemDeleteConfirm = document.getElementById("item-delete-confirm"); // SET BUTTON ID AS THIS
let itemPlace = document.getElementById("item-place");


for (let item of deletePlannerItems) {
    item.addEventListener("click", (e) => {
        let tripId = e.currentTarget.getAttribute("trip_id");
        let placeId = e.currentTarget.getAttribute("place_id");
        let placeName = e.currentTarget.getAttribute("place_name");
        itemDeleteForm.setAttribute("action", `/trips/remove_place/${tripId}/${placeId}`);
        itemDeleteConfirm.value = placeId;
        itemPlace.innerText = placeName;
        
    });
}


