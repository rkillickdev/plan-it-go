//Solo Image Modal

let soloImages = document.getElementsByClassName("image-solo");
let modalSoloImage = document.getElementById("solo-modal-image");


for (let image of soloImages) {
    image.addEventListener("click", (e) => {
        let imageUrl = e.target.getAttribute("src");
        let imageAlt = e.target.getAttribute("alt");
        modalSoloImage.src = imageUrl;
        modalSoloImage.alt = imageAlt;
    });
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

// Review Modal

let userReviews = document.getElementsByClassName("user-review");
let modalProfileImage = document.getElementById("modal-profile-image")
let modalProfileName = document.getElementById("modal-profile-name");
let modalLocation = document.getElementById("modal-location");
let modalBody = document.getElementById("modal-body");

for(let review of userReviews) {
    review.addEventListener("click", (e) => {
        let reviewId = e.currentTarget.getAttribute("review_id");
        let reviewImagePath = document.getElementById(`review-image${reviewId}`).getAttribute("src");
        let reviewProfile = document.getElementById(`review-profile-name${reviewId}`).innerText;
        let reviewLocation = document.getElementById(`review-location${reviewId}`).innerText;
        let reviewBodyText = document.getElementById(`review-body${reviewId}`).innerText;
        modalProfileName.innerText = reviewProfile; 
        modalLocation.innerText = reviewLocation;
        modalBody.innerText = reviewBodyText;
        modalProfileImage.src = reviewImagePath;

    })
}