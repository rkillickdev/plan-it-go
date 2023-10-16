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
let soloReviewProfile = document.getElementById("solo-review-profile");
let soloReviewTitle = document.getElementById("solo-review-title");
let soloReviewBody = document.getElementById("solo-review-body");

for(let review of soloReviews) {
    review.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("review_id");
        let reviewImagePath = e.target.getAttribute("src");
        let reviewTitle = document.getElementById(`review-title${reviewId}`).innerText;
        let reviewBody = document.getElementById(`review-body${reviewId}`).innerText;
        soloReviewProfile.src = reviewImagePath;
        soloReviewTitle.innerText = reviewTitle;
        soloReviewBody.innerText = reviewBody;
    })
}


// Solo Destination Info Modal

let destinationCities = document.getElementsByClassName("destination-city-mini");
let destinationCity = document.getElementById("destination-city")
let destinationImage = document.getElementById("destination-image")
let destinationSummary = document.getElementById("destination-summary")
let tripIdeasLink = document.getElementById("trip-ideas")

for(let city of destinationCities) {
    city.addEventListener("click", (e) => {
        let destinationId = e.target.getAttribute("destination_id");
        let destinationSlug = e.target.getAttribute("destination_slug");
        let summary = e.target.getAttribute("destination_summary");
        let destinationImagePath = e.target.getAttribute("src");
        let city = document.getElementById(`destination-city${destinationId}`).innerText;
        destinationSummary.innerText = summary;
        destinationCity.innerText = city;
        destinationImage.src = destinationImagePath
        tripIdeasLink.href = `trip_inspiration/${destinationId}/${destinationSlug}`



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