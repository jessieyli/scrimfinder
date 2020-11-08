# scrim-searcher
## Our Inspiration
College eSports can be fun, but finding scrimmages and a good way to practice can be tedious. As a coordinator for a Cornell University's Varsity League of Legends Team, searching for scrims can often be disorganized and disjointed among the many different discord servers used to find other teams to play against. Scrim searcher compiles all that information in an easy-to-use form where you can find teams that meet your availability and rank requirements in seconds.

## How It Works
Scrim Searcher is quick, simple, and streamlined way to find high-quality scrimmage games for League of Legends and Valorant. While other scrimmage websites often involve lengthy downloads and account verification, Scrim Searcher's in-browser interface makes it extremely accessible and easy to navigate for all users. Simply add your team's information, a scrimmage time, and your discord username, and your request will automatically be added to Scrim Searcher's existing database of scrimmage openings. Players can contact one another utilizing your discord usernames, and you're all set to scrim! 

## Challenges
As with any form of web development, we ran into a plethora of issues and bugs when creating Scrim Searcher. From database linking to app deployment, our progress often came to a standstill for multiple hours. Many of these issues required long debugging sessions, particularly when it came to properly launching our application on Heroku and connecting the website to our SQL database.

## Accomplishments That We're Proud Of
As relatively novice programmers, we're extremely proud that we were able to produce a fully functioning and self-sufficient web application within the short timeframe of this hackathon. It was a multi-layered process that required extensive collaboration within our team, and we're very proud of our delegation, organization, and diligence throughout the project's construction. 

## What We Learned
During this project, our team learned a lot about SQL databases and Flask Apps, which were the keystone components of Scrim Searcher. We were also able to learn a lot about web development using HTML/CSS and 
designing simple yet functional user interfaces. For some of us, it was also our first time working with Git and back-end frameworks, so we also learned a lot about web app structure and real-time collaboration.

## What's Next For Scrim Searcher?
We have a lot of ideas on how to improve Scrim Searcher, and we'll be pursuing them in the following weeks! Here's a list of some of the most important changes we plan to make:
- User Accounts and Authentication
- AI-driven Rank Matching and Scrim Suggestions 
- In-platform Messaging
- Platform Connections to Discord and Twitch
- Integration of Riot API for Player and Team Information
- Integration of Calendar API for Smoother Scheduling
- Increased Flexibility in Scrimmage Time Selection

[Check out our app on Heroku](https://scrim-searcher.herokuapp.com/)

If you wish to run this app locally, make sure that you have installed Python3 and use the following commands (for Windows):
`venv/Scripts/activate`  
`pip install mysql-connector-python-rf`  
`pip install flask`
