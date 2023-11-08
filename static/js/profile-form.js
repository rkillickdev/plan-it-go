const profileSubmitButton = document.getElementById("profile-submit-button");
const profileFormContainer = document.getElementById("profile-form-container");
formPurpose = profileFormContainer.getAttribute("form_purpose");
console.log(formPurpose)


document.addEventListener("DOMContentLoaded", () => {
    if (formPurpose === 'update') {
        console.log("Hello")
        profileSubmitButton.value  = "Update Profile";
        console.log(profileSubmitButton.value)
    }
});