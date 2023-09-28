var deleteButtons = document.getElementsByClassName("btn-delete");
var editButtons = document.getElementsByClassName("btn-edit");
var deleteConfirm = document.getElementById("deleteConfirm");
var reviewText = document.getElementsByTagName("textarea")[0];
var reviewForm = document.getElementById("reviewForm");
var submitButton = document.getElementById("submitButton");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        deleteConfirm.href = `delete_review/${reviewId}`;
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.value = "Update Review";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}


