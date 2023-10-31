let editButtons = document.getElementsByClassName("btn-edit");
let reviewText = document.getElementsByTagName("textarea")[0];
let reviewForm = document.getElementById("reviewForm");
let submitButton = document.getElementById("submitButton");

// Clicking on review edit button populates form text area with review content.
// Title of form submit button changed to 'Update Review'

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("review_id");
        let reviewContent = document.getElementById(`review-body${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.value = "Update Review";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}


