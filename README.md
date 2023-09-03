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