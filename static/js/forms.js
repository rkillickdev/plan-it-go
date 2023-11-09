// Checks to see if purppose of form is to enter new details
// or update existing details.  Changes value of submit button
// based on the form_purpose attribute.

const submitButton = document.getElementById("submit-button");
const formContainer = document.getElementById("form-container");
formPurpose = formContainer.getAttribute("form_purpose");
console.log(formPurpose)

document.addEventListener("DOMContentLoaded", () => {
    if (formPurpose === 'update') {
        submitButton.value  = "Update";
    }
});