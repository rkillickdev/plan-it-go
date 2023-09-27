var editButtons = document.getElementsByClassName("btn-edit");
var reviewText = document.getElementsByTagName("textarea")[0];
var userRating = document.getElementsByTagName("input")[0];
var reviewForm = document.getElementById("reviewForm");
var submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewRating = e.target.getAttribute("review_rating")
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        let ratingContent = document.getElementById(`rating_review${reviewRating}`).innerText;
        console.log(ratingContent);
        reviewText.value = reviewContent;
        userRating.valueAsNumber = ratingContent;
        submitButton.innerText = "Update Review";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}
