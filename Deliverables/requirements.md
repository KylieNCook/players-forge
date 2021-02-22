# D.2 Requirements

Group 08 - PlayersForge\
Group Members: Fernando Diaz and company

## 1. Positioning 
**1.1. Problem Statement**

The problem of searching for and downloading game mods affects people who
don't have the time, patience, or experience with technology and mods;
the impact of which is spending extensive time on different websites to download
new mods or update ones that are already in their use.

**1.2. Product Positioning Statement** 

For people that would rather find and download mods from a single and easily accessible website,
PlayersForge is a modding collection that allows users of various gaming experiences to 
search for mods that match the games that they play in one space. Unlike GameBanana, our product
combines clean, organized, and attractive design with game mod searching.

**1.3. Value Proposition and consumer segment.**


PlayersForge is a game mod search website that allows gamers and modders with limited 
to extensive modding experiences to find and download mods that match their game 
preferences inside of a simple, convenient, and eye-appealing design.


## 2. Stakeholders

- Users: Users will include gamers and modders alike. They will be the ones who will upload and download the mods from our website.
- Developers: Developers are the ones responsible for the creation of the website.
- Communities: The ones who will be looking at our website for the potential to share and download mods for a 	specific game. 

## 3. Functional Requirements (features)
1. Allow users to download published mods for free without an account.
2. Allow users to search for mods based on key words and categories and receive results sorted by relevance and popularity.
3. Alert users with notifications if any relevant mods or games receive updates.
4. Allow users to create an account and become a registered member.
5. Allow members to publish mods.
6. Allow members to create a new game category if the game is not yet represented.
7. Display recommendations for mods based on previous downloads.
8. Display suggestions for mods that are rising in popularity.
9. Display help and information pages for users on how to download or create mods for certain games.
10. Enforce a strict, clear, and concise naming system for uploaded files.
11. Scan uploaded files for malware.
12. Provide users with community pages and tabs where users can communicate with each other.

## 4. Non Functional Requirements
1. Usability - 4 out of 5 testers should be able to navigate the service effectively.
2. Speed - The web server should respond to and return requests within 5 seconds 95% of the time.
3. Security - The service should be HTTPS compliant.
4. Security - The service should scan uploaded files for suspicious code.
5. Accessibility - The service should include alternate themes such as a dark theme and colorblind theme.
6. Performance - Verify a score of B or better from each category on [WebPageTest](https://www.webpagetest.org)
7. Readability - The source code of the service should be easy to understand and maintain.
8. Resource Constraints - Besides downloads and uploads, individual pages should not exceed 10 MB.
	
## 5. MVP (Minimal Viable Product)

	The MVP for our project will be the website itself. The features we are going to validate are the ability to upload and download mods. The ability to create an account will also be required to upload mods. We will validate the features by using the website for ourselves by putting us in User role which is making sure we can create an account then seeing if we can download and upload mods. The site doesn’t have to have all of the aesthetic features yet but must be functional.


## 6. Use Cases
**6.1 Use case diagram**

Screenshot link: https://prnt.sc/103ec7c

**6.2 Use case descriptions and interface sketch**

**Use Case**: Search for mods

**Actor**: User

**Description**: User can use a search bar to find specific mods

**Preconditions**: Insert request into search bar

**Postconditions**: Returns list of relevant mods to search request


**Main Flow**:

1.	Actor types desired request into search bar

**Alternative Flow**:

None



**Use Case**: Subscribe to modders

**Actor**: User

**Description**: The user can subscribe to a specific modders account and receives notifications/updates for that account’s activity

**Preconditions**: User has an account

**Postconditions**: The user will be receiving notifications for their desired modders

**Main Flow**:
1.	The user subscribes to the modders they desire


**Alternative Flow**:
None



**Use Case**: Create a PlayersForge account

**Actor**: User

**Description**: Someone who wants to create an account and become a member of PlayersForge

**Preconditions**: They have internet and web access

**Postconditions**: They have created an account

**Main Flow**:
1.	Account logs into PlayersForge website and creates an account


**Alternative Flow**:
None



**Use Case**: Post in community pages

**Actor**: User

**Description**: User can create new posts and respond to existing ones on a community forum

**Preconditions**: Actor already has a PlayersForge account 

**Postconditions**: Actor successfully posts to community forum

**Main Flow**:
1.	Access community forum section of website
2.	Create a new post of respond to existing one


**Alternative Flow**:
None




**Use Case**: Create new game categories

**Actor**: User

**Description**: Create new category on webpage for uploading mods to

**Preconditions**: User is a member of the website and category doesn’t already exist

**Postconditions**: New category is created on webpage 

**Main Flow**:
1.	Actor selects add new category on game categories page
2.	Inserts name and description of new game category


**Alternative Flow**:
None



**Use Case**: Publish mods

**Actor**: User

**Description**: Upload mods to PlayersForge database and posted to website 

**Preconditions**: Actor has an account and mod to upload

**Postconditions**: Mod is successfully uploaded to website

**Main Flow**:
1.	Actor logs into web application
2.	Selects the option in the header to upload mods
3.	Go through requirements to successfully upload mod


**Alternative Flow**:
None



## 7. User Stories
- As a PlayersForge user I would like to have a dedicated part of my library that shows my favorite mods, so I can access them quickly.
- As a PlayersForge user I want to have a modular layout that allows me to customize my home page so that it looks as I want it to.
- As a PlayersForge user I want to have a recommendations tabs to find mods like the ones I have downloaded so I can find new mods I may like.
- As a PlayersForge user I want to have the ability to connect my account to social media accounts I have so I can share my favorite mods with my friends.
- As a PlayersForge user I want to have the option menu to contribute to the list of modifications and allow me to recommend to friends within the service.
- As a PlayersForge contributor I want to have an analytics menu so I can see the performance of the mods I have contributed to PlayersForge. 


## Issue Tracker 
Screenshot link: https://prnt.sc/103bpgk
Trello link: https://trello.com/b/js9KbTtP/issue-tracker
