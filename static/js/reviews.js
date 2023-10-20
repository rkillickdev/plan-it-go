let deleteButtons = document.getElementsByClassName("btn-delete");
let editButtons = document.getElementsByClassName("btn-edit");
let deleteConfirm = document.getElementById("deleteConfirm");
let reviewText = document.getElementsByTagName("textarea")[0];
let reviewForm = document.getElementById("reviewForm");
let submitButton = document.getElementById("submitButton");

// Populates the href attribute of the delete confirm modal with the review id
// that has been clicked on.

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        deleteConfirm.href = `delete_review/${reviewId}`;
    });
}

// Clicking on review edit button populates form text area with review content.
// Title of form submit button changed to 'Update Review'

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review-body${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.value = "Update Review";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}


