// Solo Review Modal

let soloReviews = document.getElementsByClassName("review-solo");
let soloReviewProfile = document.getElementById("solo-review-profile");
let soloReviewTitle = document.getElementById("solo-review-title");
let soloReviewBody = document.getElementById("solo-review-body");

for(let review of soloReviews) {
    review.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("data-review_id");
        let reviewImagePath = e.target.getAttribute("src");
        let reviewTitle = document.getElementById(`review-title${reviewId}`).innerText;
        let reviewBody = document.getElementById(`review-body${reviewId}`).innerText;
        soloReviewProfile.src = reviewImagePath;
        soloReviewTitle.innerText = reviewTitle;
        soloReviewBody.innerText = reviewBody;
    })
}

// OLD CODE FOR FILE UPLOAD FILE SIZE CHECKER

uploadSubmit.addEventListener("click", (e) => {
    const fileSize = fileUploadInput.files[0].size;
    const maxSizeInBytes = 2097152;

    if (fileSize > maxSizeInBytes) {
        e.preventDefault();
        fileWarningModal.show();
    }
});