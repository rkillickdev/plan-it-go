//Solo Image Modal

let soloImages = document.getElementsByClassName("image-solo");
let modalSoloImage = document.getElementById("solo-modal-image");


for (let image of soloImages) {
    image.addEventListener("click", (e) => {
        let imageUrl = e.target.getAttribute("src");
        modalSoloImage.src = imageUrl;

    });
}

// Solo Review Modal

let soloReviews = document.getElementsByClassName("review-solo");
let SoloReviewProfile = document.getElementById("solo-review-profile");
let SoloReviewTitle = document.getElementById("solo-review-title");
let SoloReviewBody = document.getElementById("solo-review-body");

for(let review of soloReviews) {
    review.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("review_id");
        let reviewImagePath = e.target.getAttribute("src");
        let reviewTitle = document.getElementById(`review-title${reviewId}`).innerText;
        let reviewBody = document.getElementById(`review-body${reviewId}`).innerText;
        SoloReviewProfile.src = reviewImagePath;
        SoloReviewTitle.innerText = reviewTitle;
        SoloReviewBody.innerText = reviewBody;
    })
}

let userReviews = document.getElementsByClassName("user-review");
// let userReviewProfile = document.getElementById("solo-review-profile");
let userReviewTitle = document.getElementById("user-review-title");
let userReviewBody = document.getElementById("user-review-body");

for(let review of userReviews) {
    review.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("review_id");
        console.log(reviewId)
        // let reviewImagePath = e.target.getAttribute("src");
        // let reviewTitle = document.getElementById(`review-title${reviewId}`).innerText;
        let reviewBody = document.getElementById(`review-body${reviewId}`).innerText;
        // SoloReviewProfile.src = reviewImagePath;
        // SoloReviewTitle.innerText = reviewTitle;
        userReviewBody.innerText = reviewBody;
    })
}