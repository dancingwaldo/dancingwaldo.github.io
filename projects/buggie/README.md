# Buggie - A Bug Tracker
#### Video Demo: https://youtu.be/FJpQjZTiSoM
#### Description:

## What is it?
As the title suggests, this is a simple bug tracker.
The goal is to make tracking your projects second nature, and an invisible part of your workflow, as a solo developer.
It was created with the solo dev in mind. As such, many of the extra features you come to expect from other Project Management products (Jira, Monday, etc.) are nowhere to be seen...
But that's ok! When you are working on projects by yourself, you don't need all that cruft!


## Ok, but what does it do?
Let's start with the three basic objects you will interact with.

### Objects:
    - Projects
    - Features
    - Bugs

#### Projects:
These are the over-arching "containers" if you will, that will house your features and bugs.
They will have two attributes: a title, and a summary.
Feel free to put whatever you want in these fields!
Just remember, a good summary of a project can be something you reference later, something that can remind you what the purpose of the project is, and what you originally intended on making to begin with.

#### Features:
These are the parts of your Project that comprise the whole.
Each functional aspect of the Project should be split into a Feature. This will make it easier later for when you start finding and recording Bugs.
Features also have a title and a summary.

#### Bugs:
The bread-and-butter of what this software is all about. Bugs!
As you're working on building your software, you encounter bugs, and have to keep track of them obviously! How else are you going to squash them?
So when you are working on a particular Feature, and notice an issue that you'll have to address later, you'll go to that Feature's page and add a Bug.
Bugs have a couple more attributes than Projects and Features:
    - Title
    - Summary
    - Severity
    - State
Title and Summary are just like before; descriptiveness is key!
Severity is an integer between 1 and 5. 1 being not that big of a deal, and 5 being a project-breaking issue.
State refers to the progress being made. There are four states that I'll go into once we get to the Kanban Board.

Now that we've looked at what objects you can create, edit, and delete, let's dive into the pages or views you will be interacting with:

### Pages/Views:
    - Register Page
    - Login Page
    - Homepage
    - Project Page
    - Feature Page/Kanban Board

#### Register Page:
This is where you can create your own account that will house all your Projects and the data they contain.
Pretty self explanatory here, just remember to follow the password requirements!

#### Login Page:
Once you have an account create, login to it here.

#### Homepage:
Ahh home sweet home...
This will list all of the Projects you create.
To create a new one, all you have to do is click on the plus symbol. A modal will popup and ask you to fill out the title and summary, then click save changes.
All projects can be edited using the edit button in the footer of each Project card.
*** IMPORTANT NOTE ***
If you want to delete one of your projects, you MUST delete all corresponding Bugs and Features first.
I will be implementing a better solution in the future.

#### Project Page:
If you click on a specific Project's summary, you will be transported to the Project Page.
Here you will see another similar view, but this time any and all Features associated with the selected Project will be displayed.
All the actions you would expect are here as well. Plus symbol for adding Features, edit button for making changes or deleting Features.
*** IMPORTANT NOTE ***
Same as above: if you want to delete a Feature, just make sure all of the Bugs associated with it are deleted first.
Again, I will be implementing a better solution in the future.

#### Feature Page/Kanban Board:
Alright, this is where you will be spending most of your time.
After clicking on the Feature that you want to see, this Kanban board view shows all of the Bugs associated with the Feature you selected.
There are four lanes, each corresponds to the four states that a Bug can be in:
    - Backlog: A Bug you will get to at some point
    - In Progress: A Bug that you are currently working on
    - Blocked: A Bug you are struggling to find the solution to
    - Complete: A Bug you have successfully fixed
Click on one of the plus symbols in one of the lanes, and another Modal will popup.
Here you can fill out title, summary, severity, and state of the Bug.
Thankfully, the state will autofill depending on the Lane you chose. If you made a mistake, no big deal, it's editable via the dropdown menu!


## Neat. How was it made?
Before I get into the tech involved in making this, I need to talk a bit about why I made certain design choices.

### Design Choices
Since the top goal for me and this project was creating an MVP, I decided to stick with the default graphical style of the Bootstrap elements themselves.
I had several ideas for how I wanted Buggie to look, but unfortunately not enough time to properly implement.
Luckily, Bootstrap's elements are clean and well-designed, so I think the current iteration of this project looks good.
I will be implementing my design ideas in the future, as I intend on adding to this project (see The Future below).

### Backend
The core backend logic was implemented using Python, and Flask was used to handle server-side operations and routing.
An SQL database containing four tables is what drives the functionality of this project. One table for the user accounts, the other three are for the projects, features, and bugs respectively.

### Frontend
The frontend is structured around HTML templates, which were made possible by the use of Flask and Jinja.
Vanilla HTML and CSS are the scaffolding of the project, but the real interactive power came from using Bootstrap 5.
Bootstrap not only allowed me to start getting functional prototypes for each feature up and running quickly, but also made it so I wouldn't have to worry too much about smaller devices.
Bootstrap is built with mobile-first development in mind, so everything scales nicely (there were some challenges, but I'll get into those later).
There is a good chunk of Javascript which allowed me to pass data between different elements on the page.
This allowed the autofill functionality possible, and was critical for different parts of the program to 'know' what Project, Feature, or Bug the user was currently viewing.

### Development Process
I kept a sort of "Captain's Log" text document that I used to keep track of my progress, and noted any struggles, feature ideas, etc.
Basic ideation came before this log, and the refinement of the project idea continued as I worked on it.
That being said, here is a VERY basic outline of my development timeline:

Day 1:
- Figure out data structure
- Create the SQL Tables
Day 2:
- Implement Register Page
- Implement Login Page
- Populate dummy data in Tables for testing
- Prototype the Index Page
- Work on Account Navigation
- Start Major Bootstrap Research (figure out what components will work)
Day 3:
- Add Login Required Decorator to functions
- Implement Project Page
- Start Feature Page
- Make changes to Account Nav
- Add Links to Project Cards
- Continue Bootstrap Research
Day 4:
- Implement Kanban Board
- Figure out how to use Modals
- Implement Add Projects Button using Modals
- Implement Add Features Button using Modals
- Figure out how to use Javascript to pass data between elements
Day 5:
- Implement Add Bugs Button using Modals
- Implement Editing Projects
- Implement Deletion of Projects
- Implement Editing Features
- Implement Deletion of Features
- Implement Editing Bugs
- Implement Deletion of Bugs
Day 6:
- Create Breadcrumbs for simple navigation
- Fix a variety of bugs (real bugs, not the object "Bugs")
- Do final testing
- Continue to fix bugs
- Create readme file


### Files Created and their Purpose
Here is a full list of files in the project and what their purposes are

- app.py
    The Application. This houses the Python logic and Flask Routes necessary for the backend to function.
- helpers.py
    A variety of python helper functions to obfuscate repetitive code and clean up app.py.
- buggie.db
    The Database. All four previously mentioned tables live here.
- requirements.txt
    This lists all dependencies for this application.
- readme.md
    The readme file you are reading right now (woah, meta!)
- styles.css
    The main vanilla CSS styles that I used to override some of the Bootstrap look/behavior.
- index.html
    Home sweet home! This is the Homepage that displays all Projects (if logged in).
- layout.html
    This is the template used for all other html files. Jinja allows for this.
- register.html
    The page that allows users to register for an account.
- login.html
    The page that allows users to login to their existing account.
- project.html
    This page shows the selected Project and its corresponding Features.
- feature.html
    This is where all the Bugs from the selected Feature are laid out on the Kanban board.
- apology.html
    This is the error page.


## The Future
As the project in its current state is really only an MVP, here are the planned features I will implement in the future:

### Visual Redesign
I intend on creating a look that is unique, and not something that you would look and say "oh they used Bootstrap for this".

### Color Themes
The reason for the dark gray look right now is due to my propensity for migraines and the need to keep my eye strain down.
That being said, I understand the desire for customization and tailoring your viewing experience to your own needs.

### Click and Drag for Bugs on the Kanban Board
This design choice has always been front of mind. The ability to click and drag a Bug from one Lane to another, and have that Bug's state change accordingly, is definitely on the horizon!


## Sources
Here you will find all of my sources for different aspects of this project.

### CSS
https://www.w3schools.com/howto/howto_css_center-vertical.asp
https://www.geeksforgeeks.org/how-to-apply-an-ellipsis-to-multiline-text-in-css/

### Javascript
https://www.shecodes.io/athena/115449-how-to-use-query-selector-with-an-id#:~:text=querySelector(%22%23myElement%22)%3B,that%20matches%20the%20specified%20ID

### Flask
https://www.geeksforgeeks.org/passing-url-arguments-in-flask/

### Bootstrap
Almost every page of this site should be considered a source.
I spent a LOT of time reading through their documentation.
If an element of Bootstrap was implemented, and it wasn't covered in the course, it came from here.
https://getbootstrap.com/

Specific Sources:
https://stackoverflow.com/questions/67667887/nested-cards-fitting-cards-within-a-card-bootstrap-cards
https://getbootstrap.com/docs/5.3/getting-started/introduction/
https://getbootstrap.com/docs/5.3/layout/columns/
https://getbootstrap.com/docs/5.3/layout/containers/
https://getbootstrap.com/docs/5.3/layout/breakpoints/
https://getbootstrap.com/docs/5.3/components/breadcrumb/
https://getbootstrap.com/docs/5.3/components/card/
https://getbootstrap.com/docs/5.3/components/modal/
https://getbootstrap.com/docs/5.3/components/modal/#varying-modal-content

### Kanban
***     THESE HAVE ONLY BEEN USED FOR REFERENCE.    ***
***     I JUST NEEDED TO SEE SOME EXAMPLES.         ***
***     NO CODE WAS USED FROM THE FOLLOWING SITES:  ***
https://www.codeply.com/go/YEFHXEnn0v/bootstrap-kanban
https://bootdey.com/snippets/view/bs4-Kanban-Board#html
https://jsfiddle.net/adminkit/vzudye75/
