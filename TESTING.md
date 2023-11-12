# **PlanitGo Testing**

## **Testing Overview**

## **CONTENTS**

## **Automated Testing**

### **Unit Testing**

## **Manual Testing**

### **Full Testing**

#### **Homepage**

#### **Navbar**

### **User Story Testing**

### **Form Testing**

### **Defensive Testing**

### **Javascript Testing**

## **Validators**

### **W3C Markup Validator**

All pages have been run through the [W3C](https://validator.w3.org/).  Initially a couple of recurring errors appeared in various templates.  These are outlined below and have now been resolved:

• Custom attributes had been used throughout, but I had not prepended these with [**data-**](https://www.geeksforgeeks.org/what-are-custom-attributes-in-html5/).  These attributes have now been corrected.

• The following error appeared when trying to trigger the review modal by wrapping the review cards in a button: <br>
```Error: Element div not allowed as child of element button in this context. (Suppressing further errors from this subtree.)``` <br>
I solved this error by triggering the modal from a div, with a role attribute "button" and an aria label for accessibility.

It was not possible to copy and paste the html templates into the validator, due to the Django templating language being used.   Pages that can be accessed without user authentication were validated using the direct url.  However, any pages that require user login cannot be validated using the URL.  Instead, I visited each page as an authenticated user and retrieved the html code by right clicking and selecting *View Page Source*.  I then selected Validate by Direct Input on the W3C validator and pasted this raw HTML.

| Page | Errors | Warnings| Result |
| ---- | -------| --------| ------ |
| [Index.html](docs/testing/validation/html/index_html.png) | 0 | 0 | Passed |
| [place_list.html](docs/testing/validation/html/place_list_html.png) | 0 | 0 | Passed |
| [browse_detail.html](docs/testing/validation/html/browse_detail_html.png) | 0 | 0 | Passed |
| [login.html](docs/testing/validation/html/login_html.png) | 0 | 0 | Passed |
| [signup.html](docs/testing/validation/html/sign_up_html.png) | 0 | 0 | Passed |
| [trip_list.html](docs/testing/validation/html/trip_list_html.png) | 0 | 0 | Passed |
| [create_trip.html](docs/testing/validation/html/create_trip_html.png) | 0 | 1 | Passed |
| [profile_form.html](docs/testing/validation/html/profile_form_html.png) | 0 | 1 | Passed |
| [trip_detail.html](docs/testing/validation/html/trip_detail_html.png) | 0 | 0 | Passed |
| [place_detail.html](docs/testing/validation/html/place_detail_html.png) | 0 | 0 | Passed |
| [review.html](docs/testing/validation/html/review_html.png) | 0 | 0 | Passed |
| [add_image.html](docs/testing/validation/html/add_image_html.png) | 0 | 1 | Passed |
| [logout.html](docs/testing/validation/html/logout_html.png) | 0 | 0 | Passed |
| [destinations.html](docs/testing/validation/html/destinations_html.png) | 0 | 1 | Passed |
| [get_places.html](docs/testing/validation/html/get_places_html.png) | 0 | 0 | Passed |

• There was a warning that appeared on any page that contains a form with an upload image field:

```
Warning: The type: attribute is unnecessary for JavaScript resources.
```

### **W3C CSS Validator**

### **Lighthouse:**

<br>

I used Lighthouse within Google Chrome developer tools as a way of testing performance, accessibility, best practices and SEO of the site.

<br>

<details><summary>Desktop Results</summary>

Home Page

[! Lighthouse Desktop Results]

