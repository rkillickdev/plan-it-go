let ratingNumber = document.getElementById("stars").getAttribute("place_rating");

document.getElementById("stars").innerHTML = generateStars(ratingNumber);

// Referenced the following article when finding a star rating display solution:
// https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons

function generateStars(rating) {
    let starList = [];
    let number = rating 

    // Append filled stars to starList
    for (number; number >=1; number--)
        starList.push('<i class="fa-solid fa-star text-primary" aria-hidden="true"></i>&nbsp;');
        
    // Append any half stars if necessary
    if (number == .5) starList.push('<i class="fa-solid fa-star-half-stroke text-primary" aria-hidden="true"></i>&nbsp;;');

    // // Append empty stars to starList
    for (let i =(5 - rating); i>=1; i--)
        starList.push('<i class="fa-regular fa-star text-primary" aria-hidden="true"></i>&nbsp;');

    return starList.join('');
}
