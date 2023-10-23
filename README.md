# **Plan-It Go Travel Planner**

<br>

## **CONTENTS**

* [User Experience (UX)](#user-experience-ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
        * [Target Users](#target-users)
    * [Agile Methodology](#agile-methodology)
        * [Epics](#epics)
        * [User Stories](#user-stories)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
    * [Structure Plane](#structure-plane)
        *[Features](#features)

# **User Experience (UX)**

## **STRATEGY PLANE**
___

## **Project Goals**

<br>

The aim of Plan-It Go is to provide inspiration for new and exciting adventures and assist the user in planning their next trip.

Born out of a love for travel and exploring new cities, this site hopes to help the user plot out their ideal itinerary, by offering recommendations based on the experience of other travellers.  Arriving in a new city can be overwhelming if you don’t know where you’re heading.  If only you had known about a quirky little bar or restaurant round the corner rather than settling for second best. Sometimes the best kept secrets are not so obvious, but with the help of Plan-It Go, you can be in the know about the best places to visit.

Having selected a location for their trip, users will be provided with recommendations of places to visit.  Once logged in to the site, users will have the ability to use these recommendations to build an itinerary for their trip.
Recommendations will be sourced using the [Amadeus Points Of Interest API](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/points-of-interest).  This is a summary of the API functionality from their documentation:

*`
"The API provides a ranked list of attractions and the name, coordinates, category (sights, beach/park, historical, nightlife, restaurant or shopping), tags and score for each one. The scores are powered by the AVUXI TopPlace algorithm which analyses millions of online reviews, photos and comments to determine popularity"
`*

When users add a place to their trip itinerary, data retrieved from the API for this place will be added to the site’s own ‘place’ database.  As site traffic increases and users start building their own trips, reviewing places they have visited and posting photos of their experiences, the data collated from these interactions will be used to start making recommendations to other site users.

The ‘trip planner’ functionality also serves as a great way for users to record and journal their travels, storing their ‘go to’ places for the next time they return to a city and preserving memories with photos of the places they visited.

All users of the site will be able find inspiration for their next getaway, by browsing trips that other users have planned.  The site owner hopes that this will encourage users to create their own account and make use of the trip planner themselves.  The site serves as a stand alone travel planner, but the functionality could also be integrated into larger travel sites.



[Back to top &uarr;](#contents)

## **Target Users**

<br>

## **AGILE METHODOLOGY**
___

## **Epics**

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



## **User Stories**

#### **EPIC: User Account [#1](https://github.com/rkillickdev/plan-it-go/issues/1)**

* As a Site User I can register an account so that I can access features only available to registered users such as creating and planning trips [#2](https://github.com/rkillickdev/plan-it-go/issues/2)
* As a Site User I can log in to my account so that I can create, view, update and delete my trips [#3](https://github.com/rkillickdev/plan-it-go/issues/3)
* As a Site User I can log out of my account for security so that no one else can access or modify my trips [#4](https://github.com/rkillickdev/plan-it-go/issues/4)
* As a Site User I am aware of my login status so I know whether I can carry out actions available only to logged in users [#5](https://github.com/rkillickdev/plan-it-go/issues/5)
* As a Site User I can create and update a user profile for my account so that I can personalise my details with a screen name, image and bio [#6](https://github.com/rkillickdev/plan-it-go/issues/6)
* As a Site Administrator I can moderate user reviews so that I can decide whether the content and images are appropriate for other site users to view [#34](https://github.com/rkillickdev/plan-it-go/issues/34)

#### **EPIC: Plan Trip [#7](https://github.com/rkillickdev/plan-it-go/issues/7)**

* As a Site User I can create a personalised trip planner for a chosen destination so that I can start planning places to visit on my trip [#8](https://github.com/rkillickdev/plan-it-go/issues/8)
* As a Site User I can view recommended activities for the chosen location so that I can plan a bespoke itinerary for the trip that appeals to my tastes and interests [#9](https://github.com/rkillickdev/plan-it-go/issues/9)
* As a Site User I can view details of a specific place so that I can decide whether I should add it to my itinerary [#10](https://github.com/rkillickdev/plan-it-go/issues/10)
* As a Site User I can add a recommendation to my trip planner so that I can build an itinerary to use and refer to when travelling to the location [#11](https://github.com/rkillickdev/plan-it-go/issues/11)
* As a Site User I can remove places from my trip planner so that I can have control over building an itinerary and change my mind about places that were previously added [#12](https://github.com/rkillickdev/plan-it-go/issues/12)
* As a Site User I can choose to view my current trip itinerary at any point during planning so that I can keep track of places I have added [#13](https://github.com/rkillickdev/plan-it-go/issues/13)
* As a Site User I can edit my trip itinerary by removing a place or adding more so that I can continue modifying my plans [#14](https://github.com/rkillickdev/plan-it-go/issues/14)
* As a Site User I can save all the places in my trip itinerary so that I can return to my planning at any time [#15](https://github.com/rkillickdev/plan-it-go/issues/15)

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
* As a Site User I **feel a positive emotional response while interacting with the site ** so I am engaged and continue to use and return [#32](https://github.com/rkillickdev/plan-it-go/issues/32)
* As a Site User I can view the site on a range of screen sizes so that I can enjoy good user experience on my device of choice [#33](https://github.com/rkillickdev/plan-it-go/issues/33)




## **SKELETON PLANE**
___

## **Wireframes**

<br>

## **Database Schema**

<br>

[A PDF for Database Schema v01 Can be viewd here](docs/database-schema/planit-go-database-highlight-schema-v01.pdf)

[The database schema created using dbdiagram.io can be found here](https://dbdiagram.io/d/64f2f6f902bd1c4a5ed78564)


## **STRUCTURE PLANE**
___

## **Features**

### **Navbar**

The navbar is common to all pages.  The HTML structure for this feature lives in the nav.html files with the following file path:

`
templates/includes/nav.html

`
This file is then included in the base.html file, which is subsequently included in every html template.  This ensures that any changes to the navbar html code need only be made once.

To the left of the navbar is a clean, minimal brand logo that is deigned to instantly comumunicate the core aims of the site.  By using a globe as a substitute for the letter 'O' in 'GO', site users are subconciously aware that 'planning of global travel' is at the heart of the site's objectives.  The colours used in the brand logo are consistent with the colour scheme used throughout the rest of the site.  The hover effect applied to the brand logo is consistent with the effect used for all other clickable links throughout.  Clicking on the logo takes the site user back to the home page.

To the right of the navbar, page links are displayed and a hover effect applied so users know they are clickable.  Dependent on the status of the site user, links display as follows:

* Home -> index.html - Visible to all users
* Ideas -> trip_browse.html - Visible to all users
* Profile -> profile_form.html - Visible to logged in users
* My Trips -> trip_list.html - Visible to logged in users
* Signup -> login.html - Visible to logged out users
* Login -> login.html - Visible to logged out users
* Logout -> logout.html - Visible to logged in users
 
 To ensure good user experience and satisfy the site owner's goal of responsive design across a range of device sizes, the navigation menu collapses down into a hamburger menu on screen sizes below 992px.  This prevents the navbar from feeling cluttered on smaller devices and the instantly recognisable hamburger icon ensures that site navigation remains intuitive for users.

### **Footer**

### **Home Page**

**Header Hero Image**

The aim of the owner is that the purpose of the site should be immediately evident to the user when they land on the home page.  The hero image chosen to convey this message communicate both the themes of travel and planning, with the coloured pins placed in the map reminiscent of an age before the possibility of online trip planning.  A younger site user is more likely to associate these pins with the recognisable Google Maps interface, where digital pins are used to comunicate location.

The colours from the hero image were the starting point for the colour scheme used consistently throughout the rest of the site.  The core goals of the site are reinforced by the title in the header, and the revolving words adds a touch of visual interest for the user.  The colours chosen for these interchanging words tie in with the three featured pins on the map hero image.

A call to action is then used, to draw the user into the 'trip planning' fuctionality of the site.  The 'start planning' clickable button will direct non logged in users to the signup page.  Those that already have user credentials can easily switch to the login page to enter their details.  If a user is already logged in, they will be taken directly to their 'trip list' page where they can edit existing trips or create new ones.

**Site Goals**

Next three cards layout the ways in which the site can be used.  The inclusion of icons above each statement helps communicate these goals before the user has even read the text.

**Destinations Carousel**

The aim of this section is to allow users to browse and draw inspiration from the trips of other site users.  Clicking on each carousel card display information about the featured destination in a large modal window.  From here, they can follow a link to browse trips for this specific destination.  Throughout, the user will be gently guided and given the option to sign up and enjoy the full features and functionality of the site.

### **Login/ Sign Up Pages**

In the settings.py file, the following urls have been set for redirecting users after signup and login:

```python
ACCOUNT_SIGNUP_REDIRECT_URL = '/trips/trip_list'
LOGIN_REDIRECT_URL = '/trips/trip_list'
```

### **Trip List** 

Dependent on the status of the logged in user account, one of three pages are displayed.  Conditional 'If/ Else' statements are used in the html template to achieve these different displays:

* **New Users**

Upon successful login, a user profile is automatically created with a unique id.  The aim of the site however is to offer personalised profiles, so new users are encouraged to click the 'Create Profile' link where they can enter a unique screen name, upload a profile image and write a bio.  Only the screen name is a compulsory field in the form, as this is how they will be identified on the site moving forwards.

* **Returning Users**

If a logged in user has already provided a screen name, but as yet have not created any trips, they are encouraged to get started and click the + button 'plan your first trip'.  There is also the option to seek some inspiration, which lets the user browse trips planned by fellow site users.

If a logged in user already has one or trips created, these are listed in date order.  They can either click on each trip to view further details, or click the + button 'plan your next trip'.

### **Trip Details**

**Trip Summary**

**Recommendations**

**Trip Planner**

* View Place Details

* Remove From Planner

* Leave A Review

* Upload Image

### **Place Details**

**Place Summary**

**Details Tab**

**Reviews Tab**

**Gallery Tab**

### **User Reviews**

### **User Images**

### **Toasts**

### **Error Pages**

### **Favicon and Meta Tags**

### **Security & Defensive Design**

### **Responsive design**












