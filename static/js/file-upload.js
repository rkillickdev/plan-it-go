// This was a workaround to remove the default innerHTML on the custom file
// input label, generated by django crispy forms

const customFileLabel = document.querySelector(".custom-file-label");

document.addEventListener("DOMContentLoaded", () => {
    customFileLabel.innerHTML = "Select A File";
});

// Event listener added to submit button on forms with a file input field.
// The function checks if the file size is over 2MB and prevents form
// submission and alerts user if this is the case.
// I referenced several articles for this solution:
// https://www.willmaster.com/library/manage-forms/limiting-file-upload-size.php
// https://stackdiary.com/tutorials/how-to-check-file-upload-size-with-javascript
// https://wesbos.com/javascript/05-events/prevent-default-and-form-events

const fileUploadInput = document.querySelector(".file-upload-input")
const uploadSubmit = document.getElementById("submit-button");

uploadSubmit.addEventListener("click", (e) => {
    const fileSize = fileUploadInput.files[0].size;
    const maxSizeInBytes = 2097152

    if (fileSize > maxSizeInBytes) {
        e.preventDefault();
        alert('File size must be less than 2MB.  Please select another image');   
    }
});





