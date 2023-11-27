# **PlanIt Go**

<br>

![Deployed Site Responsive Views](docs/features/responsive/pp4-readme-resposive-mock-up.png)

<br>

[View the deployed app on Heroku](https://plan-it-go-5b10d0005b0a.herokuapp.com/)

<br>

PlanIt Go has been developed as part of the [Code Institute](https://codeinstitute.net/) Diploma in Full Stack Software Development (Portfolio Project #4).  The aim of the site is to provide inspiration for new and exciting adventures and assist the user in planning their next big trip.

## **CONTENTS**

* [User Experience (UX)](#user-experience-ux)
    * [Strategy Plane](#strategy-plane)
        * [Project Goals](#project-goals)
    * [Agile Methodology](#agile-methodology)
        * [Epics](#epics)
        * [User Stories](#user-stories)
    * [Scope Plane](#scope-plane)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
    * [Structure Plane](#structure-plane)
        * [Features](#features)
            * [Navbar](#navbar)
            * [Footer](#footer)
            * [Home Page](#home-page)
            * [Browse Places](#browse-places)
            * [Browse Details](#browse-details)
            * [Authorisation](#authorisation)
            * [Trip List](#trip-list)
            * [Profile Creation](#profile-creation)
            * [Trip Creation](#trip-creation)
            * [Trip Details](#trip-details)
            * [Place Details](#place-details)
            * [User Reviews](#user-reviews)
            * [User Images](#user-images)
            * [Toasts](#toasts)
            * [Role Based Login](#role-based-login)
            * [Error Pages](#error-pages)
            * [Favicon and Meta Tags](#favicon-and-meta-tags)
            * [Security](#security)
            * [Responsive Design](#responsive-design)
            * [Accessibility](#accessibility)
            * [Future Features](#future-features)
    * [Surface Plane](#surface-plane)
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Programs and Tools Used](#programs-and-tools-used)
    * [Frameworks and Libraries Used](#frameworks-and-libraries-used)
* [Testing](#testing)
* [Deployment and Local Development](#deployment-and-local-development)
* [Bugs](#bugs)
    * [Known Bugs](#known-bugs)
    * [Solved Bugs](#solved-bugs)
* [Credits](#credits)
    * [Code Used and Referenced](#code-used-and-referenced)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)


# **User Experience (UX)**

## **STRATEGY PLANE**
___

## **Project Goals**

<br>

Born out of a love for travel and exploring new cities, this site hopes to help the user plot out their ideal itinerary, by offering recommendations of places to visit when they arrive at their chosen destination.  Arriving in a new city can be overwhelming if you don’t know where you’re heading.  Sometimes the best kept secrets are not so obvious, so the site aims to steer users towards the best places to visit.

Site users should be able to browse destinations for inspiration and view recommendations of places to visit.  The aim is that this should inspire new users to sign up to the site.  Creating a user profile will offer additional functionality, where logged in users have the ability to create trips and use the place recommendations to build itineraries.  Once they have visited a place on their trip, they will be able to leave a review or upload images for it.  Once approved by a site moderator, these reviews and images should be available for other users to view.  As site traffic increases, the database of reviews and images associated with each recommended place will grow and give site users up to date and more detailed insights as to whether a place is worth adding to their itinerary.

The ‘trip itinerary’ functionality will also serve as a great way for users to record and journal their travels, storing their ‘go to’ places for the next time they return to a city and preserving memories with photos of the places they visited.

The site will be developed as a stand alone travel planner, but the functionality could also be integrated into larger travel sites.

[Back to top &uarr;](#contents)

## **AGILE METHODOLOGY**
___

This project was approached following the principles of Agile Development, building the solution incrementally through repeated iterations.  Initially, 5 [epics](#Epics) were defined.  These were broad definitions of functionality for the site that would not fit into a single iteration.

Epics were then broken down into user stories and logged as issues on GitHub using the following [customised template](https://github.com/rkillickdev/plan-it-go/blob/main/.github/ISSUE_TEMPLATE/epic.md).  Acceptance Criteria were defined as part of each user story to clearly present the objectives and conditions that must be satisfied for the user story to be marked as complete.  Implementation of the user story was then broken down into tasks - technical work required to facilitate execution of the user story.  Each user story was given a story points label to indicate the estimated amount of work required to complete the story.

![User Story Template](docs/features/agile/pp4-agile-user-story-template.png)

A Product Backlog milestone was created on GitHub to establish a 'single authoritative source of work'.  I initially moved all user stories to the backlog before they were allocated to sprints.  The product backlog was refined throughout the course of development with user stories reprioritised as the project evolved.

Timeboxing was used throughout the development of the project.  Week long 'sprints' (otherwise referred to as iterations) were defined using Milestones on Github.  User stories from the product backlog were then allocated to a sprint following the principles of MoSCoW prioritisation.  Each user story was assigned a label specifying "Must Have", "Could Have" or "Should Have" to indicate expectation of its completion.  Stories were then tackled according to level of priority.  When defining prioritisation levels for each user story in a sprint, I was mindful that the percentage of "Must Haves" should 'not exceed 60% of the overall effort planned for the iteration'.  A 20% contingency of "Could Haves" was set, therefore leaving the remaining 20% for "Should Haves".  If it was clear that a user story would not be completed in the current sprint, it was labelled as "Won't Have" and returned to the Product Backlog.  This was then allocated to a future sprint with a higher prioritisation level.

Throughout the development process, I used a kanban board to provide up to date information about the status of progress for each iteration.  The board was created and managed using GitHub Projects and can be viewed [here](https://github.com/users/rkillickdev/projects/4).

![PlanIt Go Kanban Board](docs/features/agile/pp4-agile-kanban-board.png)

User stories for each sprint were initially allocated to the 'Todo' column and then transferred to the 'In Progress' column as they were worked on.  Once each task for the user story had been completed and all acceptance criteria satisfied, the issue was marked as complete and moved to the 'Done' column.

There are four user stories that have not been addressed in any of the iterations so far.  These are not core to the functionality of the site but might be nice to implement eventually, so I have stored these in a 'Future Features' column.  They can then easily be prioritised and allocated to a future sprint.

[Back to top &uarr;](#contents)

### **Epics**

#### **EPIC: User Account [#1](https://github.com/rkillickdev/plan-it-go/issues/1)**
`
Create the functionality for site users to create and use their own Account/ Profile
`

#### **EPIC: Plan Trip [#7](https://github.com/rkillickdev/plan-it-go/issues/7)**
`
Provide functionality so the site user can create/ read/ update/ delete trips and build an itinerary of places to visit
`

#### **EPIC: Manage Trip [#16](https://github.com/rkillickdev/plan-it-go/issues/16)**
`
Provide functionality so the site user can view and update any trips that they have created
`

#### **EPIC: Review [#21](https://github.com/rkillickdev/plan-it-go/issues/21)**
`
Create functionality for the user to log their experiences of visiting a place from their planner itinerary, by writing reviews and uploading images
`

#### **EPIC: User Experience [#28](https://github.com/rkillickdev/plan-it-go/issues/28)**
`
Implement functionality and design within the site to ensure a positive user experience
`

### **User Stories**

#### **EPIC: User Account [#1](https://github.com/rkillickdev/plan-it-go/issues/1)**

* As a Site User I can register an account so that I can access features only available to registered users such as creating and planning trips [#2](https://github.com/rkillickdev/plan-it-go/issues/2)
* As a Site User I can log in to my account so that I can create, view, update and delete my trips [#3](https://github.com/rkillickdev/plan-it-go/issues/3)
* As a Site User I can log out of my account for security so that no one else can access or modify my trips [#4](https://github.com/rkillickdev/plan-it-go/issues/4)
* As a Site User I am aware of my login status so I know whether I can carry out actions available only to logged in users [#5](https://github.com/rkillickdev/plan-it-go/issues/5)
* As a Site User I can create and update a user profile for my account so that I can personalise my details with a screen name, image and bio [#6](https://github.com/rkillickdev/plan-it-go/issues/6)
* As a Site Administrator I can moderate user reviews so that I can decide whether the content and images are appropriate for other site users to view [#34](https://github.com/rkillickdev/plan-it-go/issues/34)
* As a Site Administrator I can access models from the Django admin panel so that I can interact directly with the database [#35](https://github.com/rkillickdev/plan-it-go/issues/35)
* As a user with staff status I can add and amend details for destinations so that the content on the site can continually be expanded and updated [#39](https://github.com/rkillickdev/plan-it-go/issues/39)
* As a user with staff status I can add places for a destination to the database so that site users can browse these recommended places and add to their trips [#40](https://github.com/rkillickdev/plan-it-go/issues/40)
* As an admin superuser I can customise the django admin panel so that I can order and filter instances of models [#42](https://github.com/rkillickdev/plan-it-go/issues/42)
* As a staff user I can moderate places through the site interface so that I can ensure places with sufficient quality info are displayed to site users [#61](https://github.com/rkillickdev/plan-it-go/issues/61)

#### **EPIC: Plan Trip [#7](https://github.com/rkillickdev/plan-it-go/issues/7)**

* As a Site User I can create a personalised trip planner for a chosen destination so that I can start planning places to visit on my trip [#8](https://github.com/rkillickdev/plan-it-go/issues/8)
* As a Site User I can view recommended activities for the chosen location so that I can plan a bespoke itinerary for the trip that appeals to my tastes and interests [#9](https://github.com/rkillickdev/plan-it-go/issues/9)
* As a Site User I can view details of a specific place so that I can decide whether I should add it to my itinerary [#10](https://github.com/rkillickdev/plan-it-go/issues/10)
* As a Site User I can add a recommendation to my trip planner so that I can build an itinerary to use and refer to when travelling to the location [#11](https://github.com/rkillickdev/plan-it-go/issues/11)
* As a Site User I can remove places from my trip planner so that I can have control over building an itinerary and change my mind about places that were previously added [#12](https://github.com/rkillickdev/plan-it-go/issues/12)
* As a Site User I can choose to view my current trip itinerary at any point during planning so that I can keep track of places I have added [#13](https://github.com/rkillickdev/plan-it-go/issues/13)
* As a Site User I can edit my trip itinerary by removing a place or adding more so that I can continue modifying my plans [#14](https://github.com/rkillickdev/plan-it-go/issues/14)
* As a Site User I can save all the places in my trip itinerary so that I can return to my planning at any time [#15](https://github.com/rkillickdev/plan-it-go/issues/15)
* As a user I can see a countdown to my trip so that I know how many days until I travel [#36](https://github.com/rkillickdev/plan-it-go/issues/36)
* As a user I can filter recommended places so that I can build an itinerary tailored to my interests [#37](https://github.com/rkillickdev/plan-it-go/issues/37)
* As a user I can see places visually on a map so that I can see where they are and plan a route [#38](https://github.com/rkillickdev/plan-it-go/issues/38)
* As a user I can view place ratings displayed as stars so that I can immediately understand the popularity of a place [#41](https://github.com/rkillickdev/plan-it-go/issues/41)

#### **EPIC: Manage Trip [#16](https://github.com/rkillickdev/plan-it-go/issues/16)**

* As a Site User I can view a summary of all upcoming and completed trips so that I can choose one to view or edit [#17](https://github.com/rkillickdev/plan-it-go/issues/17)
* As a Site User I can select a trip so that I can view or edit details of the itinerary [#18](https://github.com/rkillickdev/plan-it-go/issues/18)
* As a Site User I can mark places on a trip itinerary as completed so that I can keep track of places that I have visited while travelling [#19](https://github.com/rkillickdev/plan-it-go/issues/19)
* As a Site User I can delete an entire trip so that I have control of the trips that are stored in my user account [#20](https://github.com/rkillickdev/plan-it-go/issues/20)

#### **EPIC: Review [#21](https://github.com/rkillickdev/plan-it-go/issues/21)**

* As a Site User I can write a review of a place on my itinerary so that I can share my experiences of the visit with other site users [#22](https://github.com/rkillickdev/plan-it-go/issues/22)
* As a Site User I can edit my review so that I can update the content or correct grammatical errors [#23](https://github.com/rkillickdev/plan-it-go/issues/23)
* As a Site User I can delete my review so that I can have control of reviews if I decide they are no longer relevant or necessary [#24](https://github.com/rkillickdev/plan-it-go/issues/24)
* As a Site User I can decide whether I would recommend a place so that I can help other site users to make decisions when planning places to visit on their trip [#25](https://github.com/rkillickdev/plan-it-go/issues/25)
* As a Site User I can upload images for a place on my itinerary so that I can store the memories from my trip and share these experiences with other site users [#26](https://github.com/rkillickdev/plan-it-go/issues/26)
* As a Site User I can delete images that I have uploaded for a place so that I can have control over which images are viewable [#27](https://github.com/rkillickdev/plan-it-go/issues/27)

#### **EPIC: User Experience [#28](https://github.com/rkillickdev/plan-it-go/issues/28)**

* As a Site User I can immediately understand the purpose of the site when I arrive at the home page so that I can quickly and intuitively start planning trips [#29](https://github.com/rkillickdev/plan-it-go/issues/29)
* As a Site User I can intuitively navigate the site so that I can view the content I require with minimal steps [#30](https://github.com/rkillickdev/plan-it-go/issues/30)
* As a Site User I can view site content simply and intuitively so that I can easily gather the information I need [#31](https://github.com/rkillickdev/plan-it-go/issues/31)
* As a Site User I feel a positive emotional response while interacting with the site so I am engaged and continue to use and return [#32](https://github.com/rkillickdev/plan-it-go/issues/32)
* As a Site User I can view the site on a range of screen sizes so that I can enjoy good user experience on my device of choice [#33](https://github.com/rkillickdev/plan-it-go/issues/33)
* As a user I can access links to social media accounts related to the site so that I can find out more about the site and its developer [#46](https://github.com/rkillickdev/plan-it-go/issues/46)

[Back to top &uarr;](#contents)

## **SCOPE PLANE**
___

In order to satisfy the goals outlined in the [strategy plane](#strategy-plane), I will implement the following features:

* Allow all site users to browse destinations and view recommended places to visit
* Allow logged in users to perform CRUD functionality on trips, profiles, reviews and images
* Allow logged in staff users to perform CRUD functionality on locations
* Allow logged in staff users to retrieve place data from a json file and populate the Places database with it
* Allow staff moderator to approve user reviews and images in the Django Admin Panel
* Make the site responsive across a range of devices

[Back to top &uarr;](#contents)

## **SKELETON PLANE**
___

## **Wireframes**

Wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/) and used as a blueprint for development of the site layout and structure. As the concept for administrator functionality across the site evolved over time, I used the existing wireframes as my guide to ensure format and layout was consistent for these pages.

<details><summary>Mobile</summary>

<br>

![PlanIt-Go wireframe mobile home](docs/wireframes/mobile/pp4-wireframe-mobile-home.png)

![PlanIt-Go wireframe multi](docs/wireframes/mobile/pp4-wireframe-mobile-multi-01.png)

![PlanIt-Go wireframe mobile trip detail](docs/wireframes/mobile/pp4-wireframe-mobile-trip-detail.png)

![PlanIt-Go wireframe mobile place detail](docs/wireframes/mobile/pp4-wireframe-mobile-place-detail.png)

![PlanIt-Go wireframe mobile reviews and images](docs/wireframes/mobile/pp4-wireframe-mobile-reviews-images.png)

</details>

<details><summary>Tablet</summary>

<br>

![PlanIt-Go wireframe tablet multi](docs/wireframes/tablet/pp4-wireframe-desktop-multi-01.png)

![PlanIt-Go wireframe tablet trip detail](docs/wireframes/tablet/pp4-wireframe-tablet-trip-detail.png)

![PlanIt-Go wireframe tablet place detail](docs/wireframes/tablet/pp4-wireframe-tablet-place-detail.png)

![PlanIt-Go wireframe tablet reviews and images](docs/wireframes/tablet/pp4-wireframe-tablet-reviews-images.png)

</details>

<details><summary>Desktop</summary>

<br>

![PlanIt-Go wireframe desktop multi](docs/wireframes/desktop/pp4-wireframe-desktop-multi-01.png)

![PlanIt-Go wireframe desktop trip detail](docs/wireframes/desktop/pp4-wireframe-desktop-trip-detail.png)

![PlanIt-Go wireframe desktop place detail](docs/wireframes/desktop/pp4-wireframe-desktop-place-detail.png)

![PlanIt-Go wireframe desktop reviews and images](docs/wireframes/desktop/pp4-wireframe-desktop-reviews-images.png)

</details>

## **Database Schema**

<br>

![PlanIt-Go final database schema](docs/database-schema/pp4-database-schema-final.png)

The database diagram above demonstrates that the Profile model has a one to one relationship with the User model.  A new profile is created whenever a new user registers.  Users can update their own Profile instance.  The following relationships also exist between models:

*  **One to many relationship:**  Profile model and Trip model - one profile can have many trips
*  **One to many relationship:**  Location model and Trip model - one location can have many trips
*  **One to many relationship:**  Location model and Place model - one location can have many places
*  **Many to many relationship:**  Place model and Trip model - one trip can have many places and one place can be part of many trips
*  **One to many relationship:**  Place model and Image model - one place can have many images
*  **One to many relationship:**  Profile model and Image model - one profile can have many images
*  **One to many relationship:**  Place model and Review model - one place can have many reviews
*  **One to many relationship:**  Profile model and Review model - one profile can have many reviews

From the original planning phase to the final site, tweaks were made to the database schema to suit the functionality of the site.  In particular, the Places database was modified to store any fields required from the APIFY web scraper json response.  Some fields remain in models that are not yet used, but will provide future functionality.  For example the Trip start and end DateFields.  A PDF for the original database schema v01 Can be viewed [here](docs/database-schema/planit-go-database-highlight-schema-v01.pdf)

The database schema was created using [dbdiagram.io](https://dbdiagram.io/home) and can be found [here](https://dbdiagram.io/d/PlanIt-Go-Database-Schema-Final-656329493be1495787bf2ddf)

### **Population of the Places Database**

A question that arose during the planning stages of the project was how best to provide a list of recommended places to visit based on a location selected by the site user.  I looked into various travel APIs that could deliver this data.

Initially, I planned to use the [Amadeus Points Of Interest API](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/points-of-interest).  This is a summary of the API functionality from their documentation:

*`
"The API provides a ranked list of attractions and the name, coordinates, category (sights, beach/park, historical, nightlife, restaurant or shopping), tags and score for each one. The scores are powered by the AVUXI TopPlace algorithm which analyses millions of online reviews, photos and comments to determine popularity"
`*

I tested this API and results were successful. I deliberated over whether this could be used in production to fetch data each time a site user created a new trip.  Ultimately, I decided that this API didn't provide all the information fields that a user might need, mostly notably an image and description.

On further investigation, I discovered the [APIFY Tripadvisor Scraper](https://apify.com/maxcopell/tripadvisor).  I initially wrote a view called get_places that used the API associated with this web scraping tool to return a data set and then populate the Places database with the results.  Code for this can be seen [here](docs/old-code/apify-webscraper-api-call.py).  Results were successful in the development environment although response time much slower than the Amadeus API.  However once the site was deployed to Heroku, results became less reliable where the API call and response appeared successful but Heroku threw an error before results could be written to the database.

Given the time limitations of the project, I have decided to pre-populate the Places database with places for a certain amount of pre-defined locations for demonstration purposes. I can run a request from the APIFY dashboard for a specified location and save the response in a json file which is then stored in a [data folder](static/data) within the static files directory.  The [get_places view](places/views.py) has been modified to iterate over a specified json file and populate the database.  I have created a user login with staff permissions that is able to access and run this view via the site user interface.  You can read more about staff login functionality [here](#staff-login-functionality).

![PlanIt-Go data retrieval APIFY dashboard](docs/features/pp4-database-apify-console.png)

[Back to top &uarr;](#contents)

## **STRUCTURE PLANE**
___

## **Features**

### **Navbar**

![PlanIt-Go navbar above 991px. Logged Out User](docs/features/pp4-features-navbar-full-logged-out.png)

The navbar is common to all pages.  The HTML structure for this feature lives in the nav.html file with the following file path:

```
templates/includes/nav.html
```
This file is then included in the base.html file, which is subsequently included in every html template.  This ensures that any changes to the navbar html code need only be made once.

To the left of the navbar is a clean, minimal brand logo that is deigned to instantly communicate the core aims of the site.  By using a globe as a substitute for the letter 'O' in 'GO', site users are subconsciously aware that 'planning of global travel' is at the heart of the site's objectives.  The colours used in the brand logo are consistent with the colour scheme used throughout the rest of the site.  The hover effect applied to the brand logo is consistent with the effect used for other clickable links throughout.  Clicking on the logo takes the site user back to the home page.

To the right of the navbar, page links are displayed and a hover effect applied so users know they are clickable.  Links for the currently active page are styled using the site's primary colour.  Dependent on the status of the site user, links display as shown in the table below.  This helps to signal to the user their current authentication status.

| Link | Template | Visibility |
| ---- | -------| -------- |
| Home | index.html | All users |
| Profile | profile_form.html | Logged in users |
| My Trips | trip_list.html | Logged in users |
| Signup | signup.html | Logged out users |
| Login | login.html | Logged out users |
| Logout | logout.html | Logged in users |

![PlanIt-Go navbar above 991px. Logged Out User](docs/features/pp4-features-navbar-full-logged-in.png)

To ensure good user experience and satisfy the site owner's goal of responsive design across a range of device sizes, the navigation menu collapses down into a hamburger menu on screen sizes below 992px.  This prevents the navbar from feeling cluttered on smaller devices and the instantly recognisable hamburger icon ensures that site navigation remains intuitive for users.

![PlanIt-Go collapsed nav items below 992px](docs/features/pp4-features-navmenu-toggler-collapsed.png)

Clicking on the hamburger icon expands the nav links which are stacked vertically.  Clicking again collapses the links.

![PlanIt-Go expanded nav items below 992px](docs/features/pp4-features-navmenu-toggler-expanded.png)


### **Footer**

![PlanIt-Go footer](docs/features/pp4-features-footer.png)

The footer is common to all pages.  The HTML structure for this feature lives in the footer.html file with the following file path:

```
templates/includes/footer.html
```

The footer displays social media links to the PlanIt Go Facebook, Twitter and Instagram pages.  These open in new browser tabs when clicked.  Font awesome icons are used as they are universally recognisable for the user without the need for text.  A hover effect which transforms the icon to the primary site colour indicates to the user that these links are clickable.  The GitHub profile name of the site developer is also displayed and a clickable GitHub icon that directs the user to the repository for PlanIt Go in a new browser tab.

[Back to top &uarr;](#contents)

### **Home Page**

#### **Header Hero Image**

![PlanIt-Go footer](docs/features/pp4-features-hero-image.png)

The aim of the owner is that the purpose of the site should be immediately evident to the user when they land on the home page.  The hero image chosen to convey this message communicates both the themes of travel and planning, with the coloured pins placed in the map reminiscent of an age before the possibility of online trip planning.  A younger site user is more likely to associate these pins with the recognisable Google Maps interface, where digital pins are used to communicate location.

The colours from the hero image were the starting point for the colour scheme used consistently throughout the rest of the site, although for accessibility I had to use stronger shades to ensure acceptable contrast.  The core goals of the site are reinforced by the title in the header, and the revolving words add a touch of visual interest for the user.  The colours chosen for these interchanging words tie in with one of the featured pins shown on the map.

A call to action is then used, to draw the user into the 'trip planning' functionality of the site.  The 'Sign Up' clickable button will direct non logged in users to the signup page.  Those that already have user credentials can easily switch to the login page to enter their details.  If a user is already logged in, the call to action button displays 'Get Started' and redirects the user to their 'trip list' page where they can edit existing trips or create new ones.

#### **Site Goals**

![PlanIt-Go home page site goals](docs/features/pp4-features-site-goals.png)

Three cards on the home page layout the ways in which the site can be used.  The inclusion of icons above each statement helps communicate these goals before the user has even read the text.

#### **Destinations Carousel**

![PlanIt-Go home page destinations carousel](docs/features/pp4-features-destinations-carousel.png)

The aim of this section is to allow users to browse and draw inspiration.  Clicking on each carousel card displays information about the featured destination in a large modal window.  From here, they can follow a 'Things To Do' link for this specific destination.  Throughout, the user will be gently guided and given the option to sign up and enjoy the full features and functionality of the site.

![PlanIt-Go home page destination modal](docs/features/pp4-features-destination-modal.png)

[Back to top &uarr;](#contents)

### **Browse Places**

Users that are not logged in can still browse place recommendations for each featured destination.  Results are paginated to 12 places per page and displayed as clickable cards.  Users are always provided with the option to discover 'More Destinations'.  Clicking on this button directs them back to the home page destinations carousel.

![PlanIt-Go browse places](docs/features/pp4-features-browse-places.png)

### **Browse Details**

Users that are not logged in can view details of a place.  The appearance and styling of this page replicates what a logged in user would see.  The main difference is that clicking on the 'Plan A Trip' button directs the user to the 'sign up' page.  Clicking on the 'More Places' button navigates back to the browse places page.

![PlanIt-Go browse details summary](docs/features/pp4-features-browse-details-summary.png)

![PlanIt-Go browse details](docs/features/pp4-features-browse-details.png)

[Back to top &uarr;](#contents)

### **Authorisation**

The default Django allauth templates used for signing up, logging in and logging out have been styled to match the rest of the site and ensure a consistent user experience.

![PlanIt-Go sign up page](docs/features/pp4-features-signup.png)

![PlanIt-Go login page](docs/features/pp4-features-login.png)

![PlanIt-Go logout page](docs/features/pp4-features-logout.png)

In the settings.py file, the following urls have been set for redirecting users after signup and login:

```python
ACCOUNT_SIGNUP_REDIRECT_URL = '/trips/trip_list'
LOGIN_REDIRECT_URL = '/trips/trip_list'
```

[Back to top &uarr;](#contents)

### **Trip List** 

Dependent on the status of the logged in user account, one of three pages are displayed.  Conditional 'If/ Else' statements are used in the html template to achieve these different displays:

#### **New Users**

Upon successful login, a user profile is automatically created with a unique id.  The aim of the site however is to offer personalised profiles, so new users are encouraged to click the 'Create Profile' link where they can enter a unique screen name, upload a profile image and write a bio.  Only the screen name is a compulsory field in the form, as this is how they will be identified on the site moving forwards.

![PlanIt-Go trip list with no profile](docs/features/pp4-features-trip-list-no-profile-action-call.png)

#### **Returning Users**

If a logged in user has already provided a screen name, but as yet have not created any trips, they are encouraged to get started and click the + button 'Create A Trip'.  There is also the option to seek some inspiration, which lets the user browse destinations and places.

![PlanIt-Go trip list with no trips action call](docs/features/pp4-features-trip-list-no-trips-action-call.png)
![PlanIt-Go trip list with no trips inpiration offered](docs/features/pp4-features-trip-list-no-trips-inspiration.png)

If a logged in user already has one or more trips created, these are listed in date created order.  They can either click on each trip to view further details, or click the + button 'Create A Trip'.

![PlanIt-Go trip list with existing trips action](docs/features/pp4-features-trip-list-existing-trips-action.png)
![PlanIt-Go existing trips list](docs/features/pp4-features-trip-list-existing-trips.png)

[Back to top &uarr;](#contents)

### **Profile Creation**

If the user has not already entered profile information, placeholders are used for the image and bio.  If the user enters these fields, their own image and bio is then displayed on their profile page.

![PlanIt-Go create profile](docs/features/pp4-features-create-profile-header.png)
![PlanIt-Go create profile](docs/features/pp4-features-create-profile-form.png)

Once the user has entered required profile details, clicking on the profile link in the nav bar at any time displays their profile info which they can update if desired.

![PlanIt-Go create profile](docs/features/pp4-features-update-profile-header.png)
![PlanIt-Go create profile](docs/features/pp4-features-update-profile-form.png)

[Back to top &uarr;](#contents)

### **Trip Creation**

The form used to create a new trip has been generated using django-crispy-forms.  Styling to keep it consistent with the rest of the site has been done in the forms.py file in the trips app.

![PlanIt-Go trip creation page](docs/features/pp4-features-create-trip.png)

### **Trip Details**

#### **Trip Summary**

The bootstrap accordion component is used to store a map displaying the trip destination, trip title, trip image and clickable icons for users to instigate actions.  The accordion is displayed open by default but clicking the arrow icon collapses it.  As places are added to the trip itinerary, markers are added to pinpoint that place on the map.  If there are several places in a small radius, a cluster icon is displayed.  This functionality has been implemented using Google Maps [Marker Clustering](https://developers.google.com/maps/documentation/javascript/marker-clustering#cdn).

![PlanIt-Go trip details summary](docs/features/pp4-features-trip-details-summary.png)

Clicking on view recommendations locates the user to the 'Recommendations' section on the same page.  Clicking on the pencil icon directs the user to the trip update form where they can edit details.  Clicking on the trash can icon displays a delete confirm modal.  If the user confirms deletion of the trip, they are redirected back to their trip list page.

![PlanIt-Go trip details delete confirm modal](docs/features/pp4-features-delete-confirm-trip-modal.png)

#### **Recommendations**

![PlanIt-Go trip details recommendations](docs/features/pp4-features-trip-details-recommendations.png)

Users are presented with recommended places to add to their itinerary based on the trip destination.  The results returned from the Place model are paginated 12 places at a time with 3 places displayed per row. The card for each place has a hover effect applied to indicate to the user that this is a clickable link.  Clicking on a place directs the user to the relevant [Place Details Page](#place-details).  Places that have already been added to the trip itinerary do not appear as part of this list of recommendations.

#### **Trip Itinerary**

An accordion component is used to display information relating to the trip itinerary, but only appears on screen once the trip has at least one place added. By default, each place in the itinerary is collapsed:

![PlanIt-Go trip details itinerary collapsed](docs/features/pp4-features-trip-itinerary-collapsed.png)

Expanding each accordion item presents the user with the following clickable options:

* Image is clickable -> Directs user to the [Place Details Page](#place-details)
* Remove From Planner -> A modal is used to confirm the user's intention to remove the place.
* Leave A Review -> Directs user to the [User Reviews Page](#user-reviews) 
* Upload Image -> Directs user to the [User Images Page](#user-images)

![PlanIt-Go trip details itinerary expanded](docs/features/pp4-features-trip-itinerary-expanded.png)

![PlanIt-Go planner place delete confirm](docs/features/pp4-features-planner-delete-confirm-place-modal.png)

[Back to top &uarr;](#contents)

### **Place Details**

#### **Place Summary**

On navigating to a 'place details' page, the user is presented with a summary section containing the following:

* Place Image
* Place Name
* Place Star Rating -> visually communicated using Font Awesome icons
* Add/ Remove From Trip -> This button allows the user to toggle between adding or removing the place
* More Recommendations -> This button directs the user back to the [Trip Details Page](#trip-details).  This button has susequently been renamed 'Your Trip' since the screenshot was taken.

![PlanIt-Go planner place summary](docs/features/pp4-features-place-summary.png)

#### **Details Tab**

A full description of the place is displayed in the details navigation tab:

![PlanIt-Go planner place description](docs/features/pp4-features-place-detail.png)

Below the description, the following details are available:

* Address
* Website if available - this link opens in a new browser tab
* Google Map displaying location of the place.  This functionally was implemented with the help of the following [Google's Map Documentation](https://developers.google.com/maps/documentation/javascript/adding-a-google-map).  The following [javascript file](static/js/maps.js) is loaded at the bottom of the place detail page.

![PlanIt-Go planner place location details](docs/features/pp4-features-place-location-details.png)

#### **Reviews Tab**

The reviews tab is only visible to users if a review exists for the selected place.  Reviews are displayed using the Bootstrap Carousel component and appear as clickable cards with hover effect consistent with the rest of the site.  Clicking on a card opens the full review in a modal.  Only reviews that have been approved by a site administrator will be displayed.

![PlanIt-Go place detail reviews](docs/features/pp4-features-place-detail-reviews.png)

#### **Gallery Tab**

The gallery tab is only visible to users if images relating to the selected place have been uploaded to the site. Images are displayed as thumbnails in rows of 3.  Clicking on any of the images opens a full size version in a modal. Only images that have been approved by a site administrator will be displayed.

![PlanIt-Go place detail gallery](docs/features/pp4-features-place-detail-gallery.png)

[Back to top &uarr;](#contents)

### **User Reviews**

From their trip itinerary, users can navigate to their 'reviews page' to leave a review for a place once they have visited.  The form is generated using django crispy forms.  Styling is done in the forms.py file for the places app.

![PlanIt-Go user review form](docs/features/pp4-features-user-review-none-existing.png)

Users can also view, edit or delete any other reviews they have already left.  A confirmation modal is used to check the user really wants to delete a review before removing from the database.  Once a review has been submitted, this is immediately visible to the logged in user and they still have the ability to edit/ delete, but the review is not accessible to other site users until the content has been approved by a site moderator.

![PlanIt-Go existing user reviews](docs/features/pp4-features-existing-user-reviews.png)

![PlanIt-Go review delete confirm](docs/features/pp4-features-review-delete-confirm.png)

### **User Images**

Users are presented with the option to 'upload image' for each place in their trip itinerary.  Once directed to this page, they can select an image to upload.  To prevent a situation where file upload causes the page to hang for an unacceptable amout of time, for now I have implemented code that only allows users to upload files under 2MB in size.  If the chosen file exceeds this size, users are presented with a warning modal and asked to choose a smaller file.

![PlanIt-Go add image](docs/features/pp4-features-add-image-updated-style.png)

![PlanIt-Go file size warning](docs/features/pp4-features-file-size-warning.png)

If a user has already uploaded images for other places, a gallery is displayed.  Functionality has been implemented to allow the user to 'add more' images to a place listed in the gallery, or delete an image.  A confirmation modal is used to check the user really wants to delete an image before removing from the database.  Once an image has been submitted it is immediately visible to the logged in user, but the image is not visible to other site users in the 'place gallery' tab until it has been approved by a site administrator.

![PlanIt-Go image gallery](docs/features/pp4-features-add-image-gallery.png)

[Back to top &uarr;](#contents)

### **Toasts**

Toasts are available as a Bootstrap component, and have been used in conjunction with [Django Messages](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/) to provide the user with feedback as they navigate the site. This helps to communicate when an interaction has been successful or unsuccessful, therefore always keeping the user informed and providing an enhanced user experience.  

![PlanIt-Go toast success message ](docs/features/pp4-features-toast-success-trip-add.png)

To avoid the repetition of code and to ensure that the appearance of messages is consistent across the site, the toast  html structure lives in the [messages.html](templates/includes/messages.html) file and has been included in the base.html template.  If a message is detected on page load, the following [toasts javascript file](static/js/toasts.js) is loaded which initialises the toast.

### **Role Based Login**

#### **Staff User Functionality**

Functionality is included on the site that is only available to users with 'staff' status.  These user logins can be created and provided with relevant permissions by a superuser in the [Django Admin Panel](#django-admin-panel). Clicking on the 'Add A Destination' directs the staff user to a page where they can create and edit destinations.

![PlanIt-Go staff user login redirect page ](docs/features/pp4-features-trip-list-staff-user.png)

![PlanIt-Go staff user create destination form ](docs/features/pp4-features-create-destination-staff-user.png)

Once the location form has been successfully populated with the required information, an instance of Location is created and saved to the database and displayed as a card in the destinations list below.  A success message is displayed in a toast to keep the user informed.  Clicking on the destination card opens the destination modal.

![PlanIt-Go staff user destination list ](docs/features/pp4-features-destination-list-staff-user.png)

If a staff user clicks on the magnifying glass for a destination that is already populated with places, they are directed to the [place list page](#browse-places) for the selected destination.

Clicking on the pencil icon on any of the destination cards allows the staff user to update details.  The form is populated with details of the selected location, the submit button changes to 'update' and the title also changes to 'Update Details For...'

![PlanIt-Go staff user update destination](docs/features/pp4-features-update-destination-staff.png)

At this stage,  a newly created destination will have no recommended places associated with it.  Staff users are able to check if any places for the destination can be retrieved.  If they click on the magnifying glass icon at the bottom of a destination with no associated places, they are directed to the 'get places' page.  The form drop down menu location field is filtered so only locations that do not have any associated places appear.  The form is submitted and an attempt is made to retrieve places for the selected location.  Read [here](#population-of-the-places-database) about how place data is retrieved and handled.  If there is place data available for the selected location, the database will be populated and the user is redirected to the place list page for the newly populated destination.  A success message of "Places have been retrieved successfully" is displayed in a toast to keep the user informed.  If no place data is currently available, users are alerted to this with a toast message of "We were not able to retrieve this data" and they are redirected to the 'destinations' page.

![PlanIt-Go staff user destination list ](docs/features/pp4-features-get-places-staff-user.png)

[Back to top &uarr;](#contents)

#### **Place Moderation**

I realised that an element of moderation is required on the data returned in the json response from the APIFY web scraper.  Sometimes descriptions are not worded very well or might not appear in english.  I therefore decided to build in functionality that gives staff users the ability to moderate a place when they are checking these details.  When logged in as staff and accessing the place detail page, there is an option to toggle approval.  By default, all places are approved but if the staff moderator is not satisfied with the quality of the data, they can remove approval for it.  These places will subsequently not be displayed to regualar site users.  Once the staff user has 'un-approved' a place and left the page, it can only be re-approved via the Django admin panel as it no longer appears on the place list page.

![PlanIt-Go staff unapprove place](docs/features/pp4-features-remove-place-approval.png)

![PlanIt-Go staff approve place](docs/features/pp4-features-add-place-approval.png)

#### **Destination Moderation**

There might be an occasion, where a staff user creates a new destination but does not immediately populate with place data.  I do not want destinations displayed to regular site users until the associated content and data has been throughly checked and approved.  I therefore added an 'approved' field to the Location Model which defaults to the value False.  While this boolean field is set to false on an instance of a Location, it will not be available to regular site users whether they are browsing or creating trips.  This field can only be set to true by a moderator in the Django Admin Panel.

![PlanIt-Go staff approve place](docs/features/pp4-features-django-admin-superuser.png)

#### **Django Admin Panel**

Models for the site can be accessed and manipulated from the Django Admin panel.  The designated superuser has total control over this.  I have set up a 'moderator' login for a staff user with limited permissions in the admin panel.  They are able to view and approve reviews and images created by users.  They also have access to Trips, Locations, Places and Profiles.  I have customised the layout and selected display fields to be shown for each model, to make navigation of the  Django admin panel more intuitive.  Code for this has been implemented in the related admin.py files.

![PlanIt-Go Django admin moderator](docs/features/pp4-features-django-admin-moderator.png)

[Back to top &uarr;](#contents)

### **Error Pages**

I have included custom 403, 404 and 500 error pages as a form of defensive design. This improves the user experience by keeping the user informed about the problem and engaged with the site.  The styling imagery and branding used on these pages is consistent with the rest of the user experience.  To ensure the user does not decide to navigate away from the site, a 'Back To Home Page' button is displayed.  This also ensures they do not have to use the back button in their browser for navigation.

#### **404 Error Page**

Displayed if the user tries to access a broken link or page on the site that does not exist/ has been moved.

![PlanIt-Go 404 error](docs/features/pp4-features-404-error.png)

#### **403 Error Page**

Displayed if the user tries to access unauthorised content.  Read [here](#defensive-programnming) about the defensive programming that was implemented to stop unauthorised users accessing, editing and deleting content that does not belong to them.

![PlanIt-Go 403 error](docs/features/pp4-features-403-error.png)

#### **500 Error Page**

Displayed to warn the user when an internal server error occurs.  This lets them know that there is a problem with the site and not at their end. They are also informed that a solution to the problem is being worked on in the hope that they will not navigate away from the site.

![PlanIt-Go 500 error](docs/features/pp4-features-500-error.png)

[Back to top &uarr;](#contents)

### **Favicon and Meta Tags**

A favicon link has been included in the head of the base.html template and displays in each browser tab. The image is the same icon that is used in the navbar brand heading, to ensure consistency of styling.  It is a 16px X 16px ico file generated on the [Favicon.ico & App Icon Generator](https://www.favicon-generator.org/)

![Favicon Image](docs/features/pp4-features-favicon.png)

Open Graph and Twitter meta tags have been placed in the head of the base.html template to control how the URL is displayed when shared on social media.  It appears as displayed below:

![Meta Tags social media display](docs/features/pp4-features-meta-tags-socials-display.png)

[Back to top &uarr;](#contents)

### **Security**

Mention debug set to false methodology

#### **Defensive Programming**

To secure certain Django Views and ensure they are only accessible to registered users, the ```
@login_required()``` decorator is used for function based views. 
The ```LoginRequiredMixin``` is used on any class based views where restrictions are required.  A site user that tries to access any of these restricted pages while not logged in, will be directed to the login page.

When navigating the site, logged in users are only presented with the option to edit or delete trips, reviews or images if they own them.  However simply removing this functionality from the user interface does not alone provide adequate security.  An additional layer of defensive programming has therefore been added in certain views to prevent specific URLs being targeted and modified. This code below is an example of how the profile ID linked to an image is checked against the profile ID of the currently logged in user.  Only if they match is the delete() method allowed to run on the image instance.  Otherwise a message is displayed to the user which informs them that they can only delete their own images.

```python
if image.profile.id == request.user.profile.id:
        image.delete()
        messages.add_message(request, messages.SUCCESS, 'Image deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own images!')
```

#### **Protection Of Sensitive Details**

Any keys containing sensitive data were stored in and retrieved from the env.py file during development. This was added to the gitignore file to ensure this data was never pushed to the GitHub repo.  For the deployed production version of the site hosted on Heroku, these sensitive keys are stored securely in the config vars.

I have also made my best efforts to protect my Google Maps API key, which needs to be accessible in certain html templates and javascript files.  The key is passed from the back end to the front end as part of the context data.  I am then using the [json_script template tag](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/) so the key can be accessed in the javascript files.  This way, the key is never actually written or stored in any of the files that live in the GitHub repo.  However, if you inspect the page, you can still see the google maps key.  I spoke with my mentor about this and he confirmed that this should be ok, as I am taking extra security measures with my Google Account by setting up application restrictions that limit the API keys' usage to only website addresses that I have specified.

In the settings file, for production purposes I have declared ```DEBUG = False```.  This prevents users from seeing the detailed traceback displayed by Django if an exception is raised.  Although this is useful while in development mode, these messages could contain information about the site that we would not want the final user to see. 

#### **CRSF Tokens**

CSRF tokens were used in forms across the site to protect against [Cross Site Request Forgery](https://docs.djangoproject.com/en/3.2/ref/csrf/).  When rendering forms using the crispy forms helper, these are automatically included.  For any other forms across the site, I have added manually.

[Back to top &uarr;](#contents)

### **Responsive design**

I adopted a mobile first approach when designing and building the site.  Bootstrap's grid system and responsiveness tiers were used to provide different layouts according to default breakpoints and ensure responsiveness across a range of device sizes.  Additional styling tweaks were made using media queries in my [styles.css](static/css/styles.css) sheet.

![PlanIt-Go responsive design 01](docs/features/responsive/pp4-mobile-responsive-01.png)

![PlanIt-Go responsive design 02](docs/features/responsive/pp4-mobile-responsive-02.png)

![PlanIt-Go responsive design 03](docs/features/responsive/pp4-mobile-responsive-03.png)

![PlanIt-Go responsive design 04](docs/features/responsive/pp4-mobile-responsive-04.png)

![PlanIt-Go responsive design 05](docs/features/responsive/pp4-mobile-responsive-05.png)

[Back to top &uarr;](#contents)

### **Accessibility**

To ensure that the site is as accessible as possible for all users and compatible with screen readers, I have implemented the following:

* Semantic markup used to structure the HTML code.
* Checked that the colour contrast ratio across the website meets acceptable standards.
* Descriptive alt attributes have been given to all images.
* Aria labels have been used for interactive elements where no accessible name is provided.

I used the [Wave Chrome Extension](https://wave.webaim.org/extension/) to check the accessibility of each page,  Results for this can be viewed in the[TESTING.md file](https://github.com/rkillickdev/plan-it-go/blob/main/TESTING.md)

## **Future Features**

Functionality that is not within the scope of this project, but that could be implemented in future sprints to enhance the user experience would be:

* The ability to specify dates of travel and display a countdown on the user's trip detail page
* The ability to refine recommended places by filtering e.g only restaurants.  Instances of the Place database already have 'type' and 'category' attributes so this filtering should be achievable.
* The ability for users to recommend a place, or better still leave a rating.  This could be useful data to acquire, as eventually recommendations could be displayed in order of popularity amongst site users.
* The ability to mark a trip or visit to a place as complete

[Back to top &uarr;](#contents)

## **SURFACE PLANE**

## **Colour Palette**

I initially used the palette generator tool on the [coolors](https://coolors.co/) website, to extract colours from the hero image used on the home page that could be used consistently throughout the site.  From this starting point, I found I needed to tweak colours to ensure contrast ratios met acceptable standards.

![PlanIt-Go hero image colour palette generator](docs/surface/pp4-map-pins-hero-colours.png)

![PlanIt-Go colour palette](docs/surface/pp4-colour-palette.png)

I used the [WebAim](https://webaim.org/resources/contrastchecker/) tool to check acceptability of contrasts.

<details><summary>Contrast Results</summary>

<br>

![PlanIt-Go contrast checker primary](docs/surface/pp4-contrast-checker-primary.png)
![PlanIt-Go contrast checker dark](docs/surface/pp4-contrast-checker-dark.png)

</details>

## **Typography**

Spacing and typography is consistent throughout the site to provide the user with a sense of familiarity as they navigate between pages. Font awesome icons are used alongside informational headings to hint at content. The following font has been selected from Google Fonts and imported to the css styles sheet.

* Raleway - a sans-serif font

## **Imagery**

Static images used throughout the site have been chosen to tie in with the core goals of the site and inspire users to plan their own trips to destinations far and wide.  These images are royalty free and have been sourced from [pexels](https://www.pexels.com/).

The brand logo used in the navbar has been designed to be minimalistic and instantly convey the site goals to the user.  'Planet' appears as 'PlanIt' to communicate that trip planning is at the heart of the site. The 'O' in 'Go' has been substituted with a globe to suggest the theme of global destinations.  The colour scheme used is consistent with the rest of the site. 

![PlanIt-Go brand logo](docs/surface/pp4-brand-logo.png)

<br>

# **Technologies Used**

## **Languages Used**

* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Sass](https://sass-lang.com/) - Preprocessor scripting language used to modify default Bootstrap styles
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

* I decided not to use jQuery in this project and implemented any functionality that required JavaScript with vanilla JavaScript.  I plan to use jQuery in a future project to enhance my knowledge of this library

## **Programs and Tools Used**

* [Git](https://en.wikipedia.org/wiki/Git) -  Version control.
* [GitHub](https://github.com/) - All files for the project stored and saved in a repository.
* [Gitpod](https://www.gitpod.io/) - IDE used to write the code, make git commits and push to GitHub.
* [Heroku](https://dashboard.heroku.com/apps) - For deployment of the project.
* [ElephantSQL](https://www.elephantsql.com/) - a PostgresQL database used for the deployed production site
* [Cloudinary](https://www.cloudimage.io/) - Used to store user uploaded images
* [PEP8](https://pep8ci.herokuapp.com/) - CI Python Linter
* [JSHint](https://jshint.com/) - Javascript linter
* [W3C](https://validator.w3.org/) - HTML Validator
* [W3C jigsaw](https://jigsaw.w3.org/css-validator/) - CSS Validator
* [Black](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/) - Python Auto Formatter
* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used at testing stage to show statistics for performance, accessibility, best practices and SEO.
* [Google DevTools](https://developer.chrome.com/docs/devtools/) - Used throughout build of website for debugging, checking responsiveness and trialing new features/ styling.
* [Google Fonts](https://fonts.google.com/) - Used to import required fonts for the website via the css style page.
* [dbdiagram](https://dbdiagram.io/home) - Database Relationship Diagrams Design Tool
* [Balsamiq](https://balsamiq.com/wireframes/) - Used to create wireframes.
* [Font Awesome](https://fontawesome.com/) - Used for all icons throughout the website.
* [TinyPNG](https://tinypng.com/) - For compression of image files to improve website performance.
* [Birme](https://www.birme.net/?target_width=425&target_height=450&auto_focal=false&image_format=jpeg&quality_jpeg=100&quality_webp=100) - For resizing and re-formatting images to make them suitable for use on the website.
* [xnipapp](https://www.xnipapp.com/) - For capturing site screenshots
* [jpg2png](https://jpg2png.com/) - For conversion of JPG images to PNG format.
* [gyazo](https://gyazo.com/captures) - For mp4 screen captures of site functionality
* [ezgif](https://ezgif.com/video-to-gif) - For conversion of mp4 video files to GIFs
* [freeconvert](https://www.freeconvert.com/gif-compressor) - For compression of GIFs
* [Aspose](https://products.aspose.app/pdf/merger) - Used to merge 3 mobile images to a single png file.
* [Favicon.ico & App Icon Generator](https://www.favicon-generator.org/) - For creating the 16x16px ico favicon.
* [Techsini](https://techsini.com/multi-mockup/index.php) - For displaying images of how the website looks across a range of devices.
* [Meta Tags IO](https://metatags.io/) - For improving site visual appearance on social media.
* [Stackoverflow](https://stackoverflow.com/) - Used for researching solutions/ fixing bugs

## **Frameworks and Libraries Used**

* [Django](https://www.djangoproject.com/) - High level Python web framework used to develop the project
* [Bootstrap v5.3.2](https://getbootstrap.com/) - Frontend framework used to create a responsive site

The [requirements.txt](requirements.txt) file provides information on required installations for this project.  Below are libraries that I installed to implement site functionality:

* [amadeus](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/points-of-interest) - Installed in the testing phase when researching how to retrieve data for places that could be used on the site.
* [apify](https://apify.com/) - Installed when testing the use of the APIFY Trip Advisor web scraper.  This made it possible to retrieve a response via their API rather than through their own interface.
* [cloudinary](https://cloudinary.com/) - Python library to facilitate integration of cloudinary with Django
* [dj-databse-url](https://pypi.org/project/dj-database-url/) - A utility that allows use of the DATABASE_URL environment variable to configure a Django application.  This was used for connection to the PostgreSQL database.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - A Django package that facilitates Cloudinary storage for media files used in the project.
* [django-allauth](https://docs.allauth.org/en/latest/) - An integrated set of Django applications addressing authentication, registration and account management.  Used to implement role based login functionality across the site.
* [django-autoslug](https://pypi.org/project/django-autoslug/) - Used for automating population of the slug field in several models across the project.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - A Django package that provides control over the rendering behaviour of Django forms.  This was used extensively in the forms.py files for each app, to ensure styling of forms remained consistent with the rest of the site aesthetic.
* [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.
* [numpy](https://numpy.org/) - A Python library used for working with numerical data. I used it to retrieve a word count for each place description, before saving as an instance to the database.
* [psycopg2](https://pypi.org/project/psycopg2/) - A Python PostgreSQL Database Adapter.
* [whitenoise](https://pypi.org/project/whitenoise/) - Simplified static file serving for WSGI applications.  I used this to serve static images, css files and JavaScript files.

[Back to top &uarr;](#contents)

# **Testing**

Please follow this link to the [TESTING.md file](https://github.com/rkillickdev/plan-it-go/blob/main/TESTING.md), for documentation about the testing procedure I followed for this project.

# **Deployment and Local Development**

I made sure to keep my requirements.txt file up to date throughout, running the command `pip3 freeze > requirements.txt` from the terminal whenever any new libraries were installed.  It is important that all requirements are added to this before deployment so Heroku installs the necessary dependencies.

In development mode, the sqlite3 database provided by Django was used but this was not suitable for use in a production environment.  The deployed site uses a PostreSQL database hosted by [elephantSQL](https://www.elephantsql.com/) that Heroku can access.  It was therefore necessary to create an account with [elephantSQL](https://www.elephantsql.com/), and create a new database instance selecting the Tiny Turtle(free) plan.  My database instance is also named 'plan-it-go'.  From the ElephantSQL dashboard, clicking on the database reveals a 'details' page where you can access the database URL, which is necessary for use in both the production and development environments.

To implement functionality of the PostgreSQL database with Django, the following libraries were installed using the terminal command:

```
pip3 install dj_database_url==0.5.0 psycopg2
```

The database URL contains information that should not be exposed publicly and therefore must not be pushed to the GitHub repository.  For development purposes I stored the database URL in the env.py file which had been added to the gitignore file.  I did not connect to the production Postgres database from my development environment until I was sure that the models were functioning and included all the fields I required.  I used the following code in my settings.py file to enable switching between development and production databases.

```python
if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
```

Once happy with the functionality of my models, I set the development variable to ```False ``` and migrated changes using the following command in the terminal:

```
python3 manage.py migrate
```

Any time I made an amendment to a model, once I had thoroughly tested in development mode I then switched and migrated these changes to the production database.

## **Cloudinary Media Files**

I am using [Cloudinary](https://cloudinary.com/) to host media files which I installed using the terminal command:

```
pip3 install dj3-cloudinary-storage
```

The following steps were taken to set Cloudinary functionality up in Django:

* `'cloudinary_storage',` and `'cloudinary',` added to INSTALLED_APPS in settings.py

```python
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## **WhiteNoise Static Files**

I am using [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/index.html) to host my static files which I installed using the terminal command:

```
pip3 install whitenoise
```

Add WhiteNoise to the MIDDLEWARE list in settings.py, above all other middleware apart from Django’s SecurityMiddleware:

```python
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

It is also important to have installed apps listed in the correct order, to prevent an issue I encountered where collection of static files failed on deployment to Heroku.  See details of this in my [solved bugs](#solved-bugs) section and read this [slack post](https://code-institute-room.slack.com/archives/C026PTF46F5/p1683039292374329) that helped me identify the problem. The `'django.contrib.staticfiles'` must be above the installed cloudinary apps:

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    # ...
]
```

For security reasons, it is important to not run with debug turned on in production.  I have implemented the following code to ensure that `DEBUG = True` while in development but defaults to `False` for the deployed site:

```python
development = os.environ.get('DEVELOPMENT', False)
# ...
DEBUG = development
```

In my env.py file I have `os.environ["DEVELOPMENT"] = "True"`.  This means that when setting the value of the variable `development` in the settings.py file, there will be an attempt to access 'DEVELOPMENT'.  This is only defined in the env.py file, but **not** in the Heroku config vars, therefore because 'DEVELOPMENT' cannot be found by Heroku, the variable `development` defaults to False.  And therefore it follows that: 
```python
DEBUG = False
```

## **Heroku Deployment**

The following steps were followed to deploy the site to Heroku:

1.  Create an account and login to [Heroku](https://id.heroku.com/login)
2.  In the Heroku dashboard, click the 'New' button at the top right of the screen and then select "Create new app".
3.  I selected the name 'plan-it-go' ,set my region to Europe and clicked on the 'Create app' button.

<br>

![Heroku deployment create app](docs/deployment/pp4-heroku-create-app.png)

4.  Click on the settings tab and then click the 'Reveal Config Vars' button.

<br>

![Heroku deployment config vars](docs/deployment/pp4-heroku-add-config-var.png)

5. I entered the following Key : Value pairs to config vars:

    * CLOUDINARY_URL : (Enter your [Cloudinary](https://cloudinary.com/) API Credentials)
    * DATABASE_URL: (Enter your ElephantSQL database URL)
    * GOOGLE_MAPS_API_KEY : (Enter your [Google Maps](https://developers.google.com/maps/) API Key)
    * MY-APIFY-TOKEN: (Enter your Apify Token - access at [Apify](https://apify.com/))  
    * PORT : 8000
    * SECRET_KEY : (Enter your Django Secret Key)

6. Prior to deployment of the site, the following two steps must be implemented in Django:
    * Add Heroku host name to ALLOWED_HOSTS in settings.py
    ```python
    if development:
        ALLOWED_HOSTS = [
            '8000-rkillickdev-planitgo-u9uuwhusilu.ws-eu106.gitpod.io'
            ]
    else:
        ALLOWED_HOSTS = ['plan-it-go-5b10d0005b0a.herokuapp.com']
    ```
    * Create a Procfile with the following code,  which tells Heroku how to run the project:
    ```python
    web: gunicorn planitgo.wsgi
    ```

    `web` here tells Heroku `this is a process that should accept http traffic`

    `gunicorn` here is a web services gateway interface server (wsgi), which is a `standard that allows Python services to integrate with web servers`.  As the version of Django being used for this project is `3.2.21`, the Gunicorn server must be installed using the terminal command:

    ```
    pip3 install 'django<4' gunicorn
    ``` 

7.  Next select the 'Deploy' tab, select GitHub as the deployment method, and click the 'Connect to GitHub' button.
8.  Search for the GitHub repository name (plan-it-go) in the 'App Connected to GitHub' section and then click the 'connect' button'
9.  You can now choose to enable automatic deploys or deploy manually.  When the 'automatic deploys' button is clicked and enabled, Heroku will rebuild the app every time a new change is pushed to GitHub.  In the 'Manual deploy' section, the 'Deploy branch' button can be clicked to deploy manually.
10.  I chose to deploy manually. Once the app is built, a link is provided to the [deployed app](https://plan-it-go-5b10d0005b0a.herokuapp.com/).

## **Local Development**

### **How to fork:**

1. Log in (or sign up) to GitHub.
2. Find the required repository, in this case: rkillickdev/plan-it-go
3. Click on the "fork" button at the top right of the page.

### **How to clone:**

1. Log in (or sign up) to GitHub.
2. Find the required repository, in this case: rkillickdev/plan-it-go
3. Click on the green code button.  This will give you the choice of cloning the repository using HTTPS, an SSH key or GitHub CLI.  Make your selection and copy the provided URL link.
4. Open the Terminal in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory.
6. Type 'git clone' and then paste the URL you copied earlier.
7. Press enter.

[Back to top &uarr;](#contents)

# **Bugs**

## **Known Bugs**

| Bug Description | Solutions Tried |
| ------------ | --------------- |
| A small styling issue that would be nice to fix in future iterations, is to replace the standard browser blue highlight effect that appears when using drop down menus on desktop devices with one of the core site highlight colours. | I have tried targeting this with various css classes with no success yet.  With more time, I hope to find a work around or fix |
| Unreliable Image SRC backup placeholder script | I have tested the [img-src-backup](static/js/img-src-backups.js) JavaScript file that should catch any occasion an image link served externally were to throw an error, and replace with a placeholder image.  Although this has been working when tested, it does not seem to provide 100% reliability and this is functionality that I would like to look into further with the benefit of more time.  My next approach will be to look at a way to add event listeners **after** the page has loaded so it can read the correct image tags, but **before** the url is retrieved |

<br>

## **Solved Bugs**

Below are bugs that were discovered during development and testing.  I have not listed some of the smaller quick fixes that were implemented during the testing phase, but they were raised as 'bug' issues on GitHub and can be seen as part of my [Project Kanban Board]((docs/features/agile/pp4-agile-kanban-board.png)).

| Bug Description | Solution |
| ------------ | --------------- |
| ModuleNotFoundError when using Django allauth | I found this [article](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar) on the problem.  The solution was to insert: ```'allauth.account.middleware.AccountMiddleware'``` in MIDDLEWARE in the settings.py file.  This is required for allauth version 0.56.0 |
| I deployed the site to Heroku early and encountered an issue where no static files were being collected.  I am using whitenoise to host my static files | The solution was that under `INSTALLED APPS` in the settings.py file, `django.contrib.staticfiles` must be listed **BEFORE** `cloudinary_storage`, otherwise `collectstatic` does not work.  I found this [great post](https://code-institute-room.slack.com/archives/C026PTF46F5/p1683039292374329) in the Code Institute Slack channels that helped me solve the issue fairly quickly |
| I discovered that once a review had been submitted on the reviews page, refreshing the browser would result in another identical review being created | For the review_create view (trips/view.py),I added an ```HttpResponseRedirect``` for any requests with the 'POST' method.  Prior to this, both POST and GET requests were using render, and this was causing the problem when posting a review. |
| Addresses displaying ```None``` as a value on the place detail / browse detail pages | I discovered that within the address object of place json data returned by the web scraper, some empty address lines would be represented as an empty string and some as Null which then showed as None when the json data was parsed by python.  I added an additional conditional statement to the single_place_info.html template on line 74, which now reads as ```{% if value and not value == "" %}```.  This checks if there is any value at all, and then goes on to check whether this value is an empty string.  It must satisfy these two conditions to then render the value to the template. |
| Defensive programming missing on trip and profile views | Add defensive programming where necessary using ```raise PermissionDenied()```.  View [GitHub Issue#44](https://github.com/rkillickdev/plan-it-go/issues/44) to see the full steps taken to resolve |
| If Image links that are loaded from external sources such as the https://media-cdn.tripadvisor.com/ or Cloudinary are broken/ return an error, there was no defensive programming in place to ensure a replacement image is displayed | I wrote a javascript file to listen for errors on any image tags on the page.  If an error is detected, a placeholder image is loaded from the static/images folder.  View [GitHub Issue#45](https://github.com/rkillickdev/plan-it-go/issues/45) to see the full steps taken to resolve |
| Profile form submit button displaying 'Create Profile' if user is updating their profile | I wrote the forms.js javascript file to determine form status and change the submit button value to 'Update' if required. View [GitHub Issue#47](https://github.com/rkillickdev/plan-it-go/issues/47) |
| Google maps markers not displaying the correct place names on hover/ clicking | I needed to pass the place name to the maps.js and map-cluster.js javascript files from the html template.  I did this using the json_script template tag, and then used this to label the map markers.  View [GitHub Issue#49](https://github.com/rkillickdev/plan-it-go/issues/49) |
| Destination carousel cards displaying incorrect information when opened in modal | To solve this, I reverted back to only wrapping the img element of the card in the button to trigger the modal. View [GitHub Issue#50](https://github.com/rkillickdev/plan-it-go/issues/50) |
| I noticed side scrolling was necessary on the profile page when viewing on smaller mobile devices |  I discovered that the issue was being caused by overflow from the image file select field.  I added the "form-select" class to any form with a file input field.  This has prevented overspill and solved the problem of side scrolling.  View [GitHub Issue#54](https://github.com/rkillickdev/plan-it-go/issues/54) | 
| During testing, I discovered that users might create a trip name that was unique, but when 'slugified' it would not be unique.  For example there could be two trip names 'LA LA Land' and 'la la land'.  When an instance of Trip is created and saved to the database, the slug field is auto populated and both would be 'slugified' as 'la-la-land'.  This throws an error and directs the user to the error 500 template. | I removed `unique=True` from the slug field in Trip model and Location model. This does not cause any further issues, as I am only using the slug field as an informational element in URLs therefore it is not a problem if two slugs are identical. The slug is always accompanied by the primary key, and this is the field that is used to look up records from the database. View [GitHub Issue#49](https://github.com/rkillickdev/plan-it-go/issues/68) to see the full steps taken to resolve |

<br>

[Back to top &uarr;](#contents)

# **Credits**

## **Code Used and Referenced**

* In the initial planning stages of the project, I found the Code Institute Peer Review channel on Slack a helpful tool to see what was required for the PP4 project.  In particular, I found this [Cinema Go Project](https://github.com/seanf316/P4-Cinema-Go) was a source of inspiration and a good indicator for covering all the assessment criteria.

### **Video tutorials and classes**

* I referenced this [Udemy Django 4 and Python Full-Stack Developer Masterclass](https://www.udemy.com/course/django-and-python-full-stack-developer-masterclass) which I had purchased before I started the Ci diploma, to help consolidate some of the Django concepts.

* I used this [Udemy Bootstrap 5 From Scratch | Build 5 Modern Websites Course](https://www.udemy.com/course/bootstrap-from-scratch) to consolidate and expand my understanding of Bootstrap and Sass.

* [Django Wednesdays YouTube Tutorial - creating users and profiles](https://www.youtube.com/watch?v=KNvSWubOaQY)

### **Threads and Articles**

* [Populating a database with data from an API response](https://dev.to/yahaya_hk/how-to-populate-your-database-with-data-from-an-external-api-in-django-398i)

* [Referenced this thread when choosing the best format for storing Geo data](https://dba.stackexchange.com/questions/107089/decimal-or-point-data-type-for-storing-geo-location-data-in-mysql#:~:text=precision%20you%20should%20use%20DECIMAL,number%20after%20the%20decimal%20point.)

* [Referenced thread when understanding how to filter list views down to only objects owned by the logged in user](https://stackoverflow.com/questions/59408167/list-of-current-user-objects-in-django-listview)

* [Referenced thread when writing the get_place view to populate the Places database, to prevent duplicate entries](https://stackoverflow.com/questions/67104304/how-do-i-check-for-duplicates-in-django-sqlite-database)

* [Referenced thread to understand how to pass url arguments to a generic class based List View](https://stackoverflow.com/questions/52871149/how-to-pass-variable-in-url-to-django-list-view)

* [Referenced when setting css_class and css_id on crispy forms](https://github.com/django-crispy-forms/django-crispy-forms/issues/849)

* [Referenced when setting only first slide of carousel to active](https://stackoverflow.com/questions/15867692/how-to-put-an-class-on-specific-first-element-inside-loop)

* [Referenced when attempting to only set one carousel item as active at any time](https://stackoverflow.com/questions/46976268/django-multiple-active-item-carousel)

* [Referenced when understanding how to filter by many to many fields](https://stackoverflow.com/questions/36024677/many-to-many-exclude-on-multiple-objects)

* [Referenced the following when trying to access environment variables in Django templates](https://stackoverflow.com/questions/62797296/how-to-access-environment-variable-from-html-or-js-in-django)

* [Referenced this article about using json script template tag to pass variables from Django template to JavaScript file](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)

* [Referenced Google Docs about Maps API](https://adamj.eu/tech/2020/02/18/safely-including-data-for-javascript-in-a-django-template/)

* [Referenced this Code Institute thread when investigating the topic of keeping Google API keys secure](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1599498777037500)

* [Referenced thread when understanding how to check current URL](https://stackoverflow.com/questions/2491605/how-to-get-the-current-url-namespace-using-django)

* [Referenced thread when attempting to make Bootstrap cards all the same size](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width)

* [Used this tutorial when learning how to implement pagination with function based views](https://www.youtube.com/watch?v=N-PB-HMFmdo&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=19)

* [Referenced this when finding out how to access allauth forms and style with Django crispy forms](https://gist.github.com/ambivalentno/9d6828fe8b5d894a6f2d)

* [Referenced this article when attempting to target carousel items with JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget)

* [Using set.all() to iterate over instances of a foreign key](https://stackoverflow.com/questions/60180014/django-display-foreign-key-reference-in-template)

* [Using .first() when filtering objects](https://stackoverflow.com/questions/39094974/objectdoesnotexist-vs-filter-first-and-check-for-none#:~:text=first()%20will%20return%20the,one%20item%20matches%20the%20query%2C%20.)

* [Referenced when researching a solution to listening for onerror events from images](https://stackoverflow.com/questions/8124866/how-does-one-use-the-onerror-attribute-of-an-img-element)

* [Cloudinary image transformations](https://cloudinary.com/documentation/django_image_manipulation#apply_common_image_transformations)

* [Optimising images with Cloudinary](https://cloudinary.com/documentation/image_optimization)

* [Python image uploads with Cloudinary](https://cloudinary.com/documentation/django_image_and_video_upload)

* [Sending messages from Django views and accessing in templates](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/)

* [Solution for counting words in a sentence with numpy](https://www.geeksforgeeks.org/python-program-to-count-words-in-a-sentence/)

* [Implementation of font awesome stars to represent place ratings](https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons)

* [Displaying Django messages in Bootstrap toasts](https://stackoverflow.com/questions/58863057/displaying-a-message-as-a-popup-alert-in-django)

* [Targeting Bootstrap navbar toggler icon for hover effect](https://stackoverflow.com/questions/63695329/how-can-i-change-bootstrap-4-navbar-toggler-color-on-hover)

* [Filtering form field queryset to limit drop down menu choices](https://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform)

* [Referenced when understanding how to add staff_required to class based views](https://gist.github.com/tauzen/8752582)

* [Fix for allauth middleware bug 'ModuleNotFoundError'](https://stackoverflow.com/questions/77012106/django-allauth-modulenotfounderror-no-module-named-allauth-account-middlewar)

* [Referenced this thread when finding solutions for defensive programming across the site](https://stackoverflow.com/questions/72980454/defensive-programming-for-delete-function-in-views-django)

* [Testing of Django forms with unittest](https://stackoverflow.com/questions/25937042/how-to-test-custom-django-forms-clean-save-methods)

* [Django best practices](https://learndjango.com/tutorials/django-best-practices-projects-vs-apps)

* [unittest and Crispy Forms](https://stackoverflow.com/questions/24898912/django-crispy-form-unit-test-fails-because-of-typeerror-of-helper-object)

* [unittesting with Django Update Views](https://stackoverflow.com/questions/38859266/django-how-to-unit-test-update-views-forms)

* [Using slugify to auto populate slug fields](https://stackoverflow.com/questions/141487/is-there-an-easy-way-to-populate-slugfield-from-charfield)

* [*args & **kwargs in Python](https://realpython.com/python-kwargs-and-args/)

* The following threads and articles were referenced while I was researching and implementing Django Crispy Forms:

    * [Article One](https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html)

    * [Article Two](https://stackoverflow.com/questions/58857859/django-crispy-tag-vs-formcrispy-filter-whats-the-difference)

    * [Article Three](https://stackoverflow.com/questions/75603468/overriding-the-default-class-attribute-using-django-crispy-forms)

    * [Article Four](https://www.scaler.com/topics/django/django-crispy-forms/)

    * [Article Five](https://github.com/django-crispy-forms/django-crispy-forms/issues/97)

    * [Article Six](https://ana-balica.github.io/2014/11/04/the-tale-of-dry-with-django-crispy-forms/)

    * [Article Seven](https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html)

    * [Article Eight](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html)

<br>

[Back to top &uarr;](#contents)

## **Media**

* The Places database was populated with data retrieved from the [APIFY Trip Advisor Web Scraper](https://console.apify.com/actors/dbEyMBriog95Fv8CW/console).  Information and images that appear as part of the place detail pages comess from the scraped APIFY data.

* [chatGPT](https://chat.openai.com/) was used to generate some text content for the destination descriptions, a few test user reviews and some user 'travel themed' profile screen names.  I also used it to generate some content for the 3 site goals on the home page, but actually ended up editing it quite heavily to fit the site purpose.  Other content for the site was written by myself.

* [Royalty free images used throughout the site from Pexels](https://www.pexels.com/)

* The following [T.S. Eliot quote](https://www.goodreads.com/quotes/9840-we-shall-not-cease-from-exploration-and-the-end-of) which acts as as placeholder for user bios, was sourced online

<br>

## **Acknowledgements**

* To my family for supporting me through this journey!
* To my Code Institute Mentor Can Sucullu for his help, advice and feedback during our mentoring sessions.














