let ratingNumber = document.getElementById("stars").getAttribute("place_rating");

document.getElementById("stars").innerHTML = generateStars(ratingNumber);

// Referenced the following article when finding a star rating display solution:
// https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons

function generateStars(rating) {
    let starList = [];

    // Append filled stars to starList
    for (let i = rating; i >=1; i--)
        starList.push('<i class="fa-solid fa-star" aria-hidden="true"></i>&nbsp');

    // Append empty stars to starList
    for (let i =(5 - rating); i>=1; i--)
        starList.push('<i class="fa-regular fa-star" aria-hidden="true"></i>&nbsp');

    return starList.join('');
}
