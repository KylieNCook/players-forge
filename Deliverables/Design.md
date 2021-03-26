# D5. - Design

Group 08 - PlayersForge\
Group Members: Kylie Cook, Fernando Diaz, David Hermann, Jared McNeece, Conrad Murphy, Noah Olono

## 1. Description

PlayersForge is a website with a dedicated, free to join community for uploading and downloading mods. Users can access the PlayersForge website on their web browser and sign up 
to become apart of the modding community; gaining access to mods such as skins, maps, etc. Each of the mods are categorized and sorted by the game they are for and the type of mod. 

The PlayersForge website is currently still in early development, with multiple features to be implemented in the near future (community forum, dedicated mod pages, user profiles).
The website provides a sleak and simple design, allowing for users to easily navigate and locate their desired mods. The homepage currently features the most popular/most downloaded mods

Project repo: [https://github.com/KylieNCook/players-forge](https://github.com/KylieNCook/players-forge)

Trello: [https://trello.com/cs3864](https://trello.com/cs3864)

## 2. Architecture

We designed out system architecture to have four layers: psql & flask, models & forms, app, and serve. Psql & flask consists of packages downloaded for the website to work, configuration, a flask environment file for easy refresh changes, and sqlalchemy to connect with out database models. Then, modles & forms consist of all of our database models and forms, for example: Users database model and RegisterUsers form. Then, the app layers consists of routes for the website, templates (html) and static files (css, images, etc.). Lastly, there is the serve file, which is the system of connecting our github website folder to aws in order to serve the website.

![image](https://user-images.githubusercontent.com/78190024/112666147-186c2800-8e19-11eb-8d55-531e24bb5cd7.png)

## 3. Class Diagram

## 4. Sequence Diagram

## 5. Design Patterns

## 6. Design Principles
