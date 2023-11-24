//Populates Solo Image Modal

let soloImages = document.getElementsByClassName("image-solo");

for (let image of soloImages) {
    image.addEventListener("click", (e) => {
        let modalSoloImage = document.getElementById("solo-modal-image");
        let imageUrl = e.target.getAttribute("src");
        let imageAlt = e.target.getAttribute("alt");
        modalSoloImage.src = imageUrl;
        modalSoloImage.alt = imageAlt;
    });
}

// Populates Solo Destination Info Modal

let destinationCities = document.getElementsByClassName("destination-city-mini");

for(let city of destinationCities) {
    city.addEventListener("click", (e) => {
        let destinationCity = document.getElementById("destination-city");
        let destinationImage = document.getElementById("destination-image");
        let destinationSummary = document.getElementById("destination-summary");
        let tripIdeasLink = document.getElementById("trip-ideas");
        let destinationId = e.target.getAttribute("data-destination_id");
        let destinationSlug = e.target.getAttribute("data-destination_slug");
        let summary = e.target.getAttribute("data-destination_summary");
        let destinationImagePath = e.target.getAttribute("src");
        let city = document.getElementById(`destination-city${destinationId}`).innerText;
        destinationSummary.innerText = summary;
        destinationCity.innerText = city;
        destinationImage.src = destinationImagePath;
        tripIdeasLink.href = `../places/${destinationId}/${destinationSlug}`;
    });
}

// Populates Review Modal

let userReviews = document.getElementsByClassName("user-review");

for(let review of userReviews) {
    review.addEventListener("click", (e) => {
        let modalProfileImage = document.getElementById("modal-profile-image");
        let modalProfileName = document.getElementById("modal-profile-name");
        let modalLocation = document.getElementById("modal-location");
        let modalBody = document.getElementById("modal-body");
        let reviewId = e.currentTarget.getAttribute("data-review_id");
        let reviewImagePath = document.getElementById(`review-image${reviewId}`).getAttribute("src");
        let reviewProfile = document.getElementById(`review-profile-name${reviewId}`).innerText;
        let reviewLocation = document.getElementById(`review-location${reviewId}`).innerText;
        let reviewBodyText = document.getElementById(`review-body${reviewId}`).innerText;
        modalProfileName.innerText = reviewProfile; 
        modalLocation.innerText = reviewLocation;
        modalBody.innerText = reviewBodyText;
        modalProfileImage.src = reviewImagePath;
    });
}