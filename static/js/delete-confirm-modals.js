// Delete Confirm Modal.
// Populates the href attribute of the delete confirm element with the 
// correct url and associated id for the trip, image or review that
// has been clicked on.

let deleteButtons = document.getElementsByClassName("btn-delete");
let DeleteConfirm = document.getElementById("delete-confirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let targetId = e.currentTarget.getAttribute("data-target_id");
        let task = e.currentTarget.getAttribute("data-task");
        DeleteConfirm.href = `${task}/${targetId}`;
    });
}

// Remove Confirm For Trip Places

let deletePlannerItems = document.getElementsByClassName("delete-planner-item");
let itemDeleteForm = document.getElementById("item-delete-form");
let itemDeleteConfirm = document.getElementById("item-delete-confirm");
let itemPlace = document.getElementById("item-place");


for (let item of deletePlannerItems) {
    item.addEventListener("click", (e) => {
        let tripId = e.currentTarget.getAttribute("data-trip_id");
        let placeId = e.currentTarget.getAttribute("data-place_id");
        let placeName = e.currentTarget.getAttribute("data-place_name");
        itemDeleteForm.setAttribute("action", `/trips/remove_place/${tripId}/${placeId}`);
        itemDeleteConfirm.value = placeId;
        itemPlace.innerText = placeName;
        
    });
}


