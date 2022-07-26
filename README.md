<h1 align="center">Pianos-R-Us</h1>

(Include live link to project somewhere here)
<p> Pianos-R-Us is a B2C commerce application that aims to sell pianos/keyboards and a music books to music lovers and learners alike. The goal of the website is to provide users with a intuitive, interactive site that they can return to by hearing about discounts through the subscription service or facebook page and by having an account model that saves customer's details.

The site has been created as a retail store that allows products to be filtered out and searched for based on the customers needs.

Users can order one item or multiple items and place them into a cart to be bought at their convenience through the Stripe payment system. They are able to edit and remove products from the cart whenever they want and the total cost is displayed at all times. Users can also make an account to save their details, rate products and give reviews to products they have bought.

# Features
## Existing Features
## Navigation Bar
* The navigation bar is provided at the top of the webpage to allow the user to easily explore the website and maintains a consistent look on across the website. The navbar contains links to the home, log-in, and registration pages when a user is not logged in. If a user is logged in a link for logging out replaces these links and if the user is an admin they get the option to create a post.

![Navbar Logged Out](/static/images/pp4-navbar-screenshot1.png)

![Navbar Logged In](/static/images/pp4-navbar-screenshot2.png)

![Navbar Logged In(Admin)](/static/images/pp4-navbar-screenshot3.png)

## Hero Image and Text
* The hero image has text overlayed on top of it to clearly give the user an immediate idea of the site's purpose.

![Hero Image](/static/images/pp4-hero-image-screenshot.png)

## Card Posts
* Posts are displayed to the user underneath the hero image in cards. These cards show the post's hero image, the headline, the author, and the text in the post. This lets the user quickly decide whether or not this is a post they would like to click on.

![Card Posts](/static/images/pp4-card-post-screenshot.png)

## Post's Stories
* When a user clicks on a card post they are sent to a page with the hero image and headline at the top and the body of text about the post below with the author similar to the card post. An admin must approve a post in order for it to appear on the website.

![Post's Stories(Text)](/static/images/pp4-posts-stories-screenshot1.png)

## Commenting on Posts
* A comment section is displayed underneath the post so people can share their thoughts.
* Users with accounts can comment on posts once an admin has approved the comment. Admins are also able to delete comments in case they change their minds.

![Post's Stories(Comments)](static/images/pp4-post-stories-screenshot2.png)

* When a user has left a comment they are given an alert to notify them.

![Comment's Alert](static/images/pp4-comment-alert.png)

## Post Creater
* This page allows admins to upload posts to the website which requires a title, the post's text and an excerpt. (The slug can be made by the user otherwise it will be automatically generated.)

![Post Creater](static/images/pp4-post-creation.png)

## Account Registration
### Registration Page
* This application allows the user to create an account to log in and access additional features on the app. When registering the webpage will ask for a username (that doesn't already exist), an optional email, a password, and the password a second time to confirm it. The webpage will detect the strength of the password entered to make sure it isn't too small or easy to figure out.

![Registration page](static/images/pp4-registration-page.png)

### Login Page
* Logging in lets the user leave comments on posts. The register and login links are only in the navbar whenever the user isn't already logged in. When the user is logged in the navbar replaces register and log in with log out to easily allow the user to sign out when they're done.

![Login page](static/images/pp4-login-page.png)

### Logout Page
* The logout page will ask the user if they are certain that they would like to log out and they must press a button to confirm this.

![Logout page](static/images/pp4-logout-page.png)

## Footer
* The footer is used to add authenticity to the website and to let people know that this is strictly for educational use only.

![Footer](static/images/pp4-footer-screenshot.png)

## SEO and Marketing
### Keywords and descriptions
A range of words were brainstormed and chosen relating to pianos and music along with words that a user may tangentially use when looking these up. This included short-tail keywords and long-tail phrases to attract large and relevant numbers of potential customers to the website.

The words and phrases chosen were: piano store, piano shop, electronic piano, thomann dp 95, electronic keyboards, 61 key electronic keyboard, wurlitzer electric piano, best electronic keyboard for beginners, bastien piano basics, piano songbook, piano book, piano classics, teach yourself piano, piano books for beginners, piano stool, piano benches.

The relevancy and authoritativeness of these phrases were chosen by manually looking them up on google and seeing their search traffic combined with using wordtracker.com to check the volume of the web searches and competitiveness.

The words and phrases were used for:
* Description and keyword meta tags in html
* Informational alt tags

### Marketing Techniques
The types of marketing used for this app were social media marketing and email marketing. A facebook page was set up to advertise that this website exists.

![Facebook page 1](static/images/pp4-logout-page.png)

The email marketing was set up through Mailchimp which allowed users to subscribe to a newsletter from the website by entering their email address. This was placed in the footer of the website on each page. The subscribers list is maintained on Mailchimp.

![Mailchimp Subscription](static/images/pp4-logout-page.png)
![Mailchimp Subscription List](static/images/pp4-logout-page.png)

## Privacy Policy
A privacy policy was generated using https://www.privacypolicygenerator.info/. This was done to address the GDPR policies. The link was placed in the footer of each page of the website and the policy was downloaded  and given styling to match the rest of the website.

![Privacy Policy](static/images/pp4-logout-page.png)

# Future Features to be added
### Likes/Dislikes
* This would allow the user to like and dislike posts and give people an indicator of whether they should read them or not.

### Post Filter
* Ideally, a user could filter through different posts based on the type of new story it is e.g. (medical, tv, celebrity), how recent it is and the number of comments (interactivity) to give the user an easier time navigating the website and posts.

### Dates
* This would allow users to see how relevant the post and comments are.

### Allow users to make posts
* Users would have much greater influence over the website by being able to leave posts.

### Restyling of admin pages
* The admin pages all add functionality to the website but they don't match the website's theme or have its core features (navbar and footer).

# Technologies Used
## Languages Used
* HTML - A mark-up language that uses semantic structures.
* CSS - Cascade style sheets are used to style the quiz and website.
* Python - Programming language used to create the databases, models, and views for this website.

## Libraries, Frameworks and Programs
* Gitpod - Used as a platform for writing code. The command line commits and pushes to GitHub.
* GitHub - Used for agile development to track progress on the kanban board.
* Heroku - Cloud platform used to deploy this application and host the code.
* Flask - Used to make working with Python easier and faster.
* Django - Used for importing frameworks that sped up making the website.
* Bootstrap - Used to build webpages.
* Cloudinary - Used to display the images used on the website indefinitely.
* lucidchart - Used to create the entitiy relationship diagram for this project.
* Balsamiq - Used to make the wireframes for the webpages.
* Allauth - Used for account registration.
* Font Awesome - Used to include the icons in the footer.
* Google Fonts - Used to allow different fonts when creating posts.
* Gunicorn - Used as a server to help run on Heroku.
* Django Crispy Forms - Used to easily create forms for logging in.
* Django Summernote - Used for post creation.

# Design
## Wireframes
* These wireframes are for the home, post story, registration, login, and logout pages. There are no wireframes for the Django admin pages used for creating posts, comments, and comment approval.

<details>
<summary>Wireframes</summary>

![home-wireframe](static/wireframes/pp4-home-page-wireframe.png)

![post-wireframe](static/wireframes/pp4-post-story-page-wireframe.png)

![register-wireframe](static/wireframes/pp4-registration-page-wireframe.png)

![login-wireframe](static/wireframes/pp4-login-page-wireframe.png)

![logout-wireframe](static/wireframes/pp4-logout-page-wireframe.png)
</details>

## Entity Relationship Diagrams
* The ER diagram shows the logic between the post and comments model with the author having a fixed ID that is used between the two. The relationship between the comments and the author is a many-to-many relationship at both ends.

* The relationship between the author and the posts and the posts and comments is a one-to-many relationship.

* The likes, created_on, and updated_on variables are data that wasn't used in the end.

<details>
<summary>Entity Relationship Diagram for Posts and Comments</summary>

![ER Diagram](static/er-diagrams/pp4-er-diagram.png)

</details>

## Planning
* A project in Github was used as an Agile Tool for tracking the building process of this project. Issues were tracked using a kanban board and linked to multiple Epics that would show the over all progress of this project's development. Each issue was tested to ensure that they could be considered completed. The criteria of these tests are outlined below.

# Testing
## Validator Testing
### HTML
* The only errors that are occuring here are from the jinja code because it the website doesn't support it. The images below is the code not containing the jinja code and passing the tests showing that is meets the appropriate requirements. The !Doctype and footer were pasted in as well because these weren't detected as coming from the jinja tags.

* The jinja tags were left in instead of being replaced with standard html because it would've meant taking out the if statements that make the navbar and comments section change based on whether the user is signed in so this was chosen as the better option.

<details>
<summary>HTML Validation</summary>

![base validation](static/validator-images/pp4-basehtml-validator.png)
![index validation](static/validator-images/pp4-indexhtml-validator.png)
![post validation](static/validator-images/pp4-posthtml-validator.png)
![signup validation](static/validator-images/pp4-signuphtml-validator.png)
![login validation](static/validator-images/pp4-loginhtml-validator.png)
![logout validation](static/validator-images/pp4-logouthtml-validator.png)

</details>

* Many htmls files were imported from different sources to allow the website to work but were never touched so those haven't been validated. However the login, logout and signup were altered so those have been validated above.

### CSS
* No errors or warnings were found through the W3C CSS validator and I was given the code for this icon to prove this.
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!"/>
    </a>
</p>

<details>
<summary>CSS Validation</summary>

![CSS Validation](static/validation-images/pp4-css-validation.png)

</details>

### Python
* Only the models.py and settings.py files didn't pass testing because the length of the lines of code had too many characters but there isn't a way to shorten them.

<details>
<summary>Python Validation</summary>

![Admin Validation](static/python-validation/pp4-adminpy-validation.png)
![Apps Validation](static/python-validation/pp4-appspy-validation.png)
![Blog-Urls Validation](static/python-validation/pp4-blog-urlspy-validation.png)
![Forms Validation](static/python-validation/pp4-formspy-validation.png)
![Models Validation](static/python-validation/pp4-modelspy-validation.png)
![Settings Validation](static/python-validation/pp4-settingspy-validation.png)
![Urls Validation](static/python-validation/pp4-urlspy-validation.png)
![Views Validation](static/python-validation/pp4-viewspy-validation.png)

</details>

### User Testing
The navbar was tested by clicking each link with each type of user to see if it worked.

The post drafting was tested by logging into the admin page and creating test posts to see the functionality at work to make sure it was showing up on the database.

Post creation was tested by purposely filling in some sections and leaving others empty to check that the post creater was only allowing posts to be made if they met the correct requirements. 

Comment creation was tested by making several comments across multiple posts to check that this feature was working as intended. It was decided that the user needed a visual que to let them know that their comment had been sent to an admin to be approved because otherwise users would have no way to know if their comment had been made or not.

Posts and comments were viewed with all types of accounts and multiple posts and comments were made using placeholder text and images to make sure all appropriate aspects of the website could be seen by a user.

The administration account was tested by creating another user and making a comment on a post. The comment didn't show up in the comment section until I logged in as an admin and approved the comment like it was intended. I deleted a comment to ensure this worked too and a post was also made and deleted by an admin to make sure this functioned correctly.

When the account registration was made it was tested by going to the registration page and filling it out. I added a username, made a password and confirmed it. I knew I was signed in because the navbar changed from Register/Log-in to Logout. Similarly the admin accounts navbar had been changed to Create a Post and Logout.

## Manual Testing
### Media Queries
I tested the media queries by manually adjusting the screen size from roughly 500-1000px to make sure the correct changes were taking place above or below each specific screen size.

This project was designed with mobile first in mind so the media query for 576px decreases the card's title and body text size and on the home page to prevent the card titles from overlapping on top of one another and to visually match the change in text of the card title. This was also done for the media query at 768px for the same reasons.

## Known Bugs
* The card text for card posts never stops extending until it has displayed all of its text. I tried a few ways to prevent this would usually end with the text being hidden but the page staying the same length so the user would scroll down a long blank section.

* The footer doesn't remain at the bottom of the webpage depending on which page the user is on. This is very noticable on the signup, login and logout pages.

# Deployment (Edit this section)
This app was deployed using Heroku.
* Log into Heroku and make an account.
* In your gitpod code create a file called "requirements.txt" and add all of your code's dependencies to it.
* Go back to Heroku and click create new app. This app must have a unique name and a region.
* Now go to the Settings tab and scroll down to the Config Vars section. You will see two inputs called key and value.
* For the first key put CREDS and paste the contents of creds.json into value. 
* For the second key put PORT and "8000" into value.
* Scroll furthur down on this tab to Buildpack. 
* Click 'add Buildpack' and select Python. Do this again and select Node.js. Make sure Python is first and Node.js is second or it could affect your code.
* Go to the Deploy tab and you will see the deployment method, click Github. Enter the name of your repository and you will be given a list of the closest names that resemble what you have typed, click the one you want for this app.
* Sign into heroku on gitpod and deploy from gitpod.
* You should set DEBUG = True when you start making your code to make it appear cleanly in the gitpod repository but when this is no longer needed remove this or set DEBUG to false.
* Back on heroku go to click Open App in the top right of the screen and the app should run as long as DEBUG is false.

## Forking
* Log into Github
* Load up the required repository.
* In the top right of the screen below the profile icon there is a fork button, click this.
* The repository should now be copied onto your Github account.

## Cloning
* Log into Github and choose a repository.
* Click on the green code button.
* You will be given three ways to clone the code. If you're using https, click “Clone with https” and copy the link.
* Open the terminal and type in the command "git clone" followed by a space and the copied url.
* The repository will now be cloned onto the computer.

# Acknowledgements
## Credits (Edit this)
* Most of the code and issues were heavily influenced by the information on the "Boutique Ado" walkthrough project from Code Institute.
* Pagination boilerplate was used in this project. It was found from it being mentioned in the CI project above.
* This youtube video that was used to give me a better understanding of Entity Relationship Diagrams, https://www.youtube.com/watch?v=-CuY5ADwn24.
* Another youtube video that helped improve my understanding of views and linking them up to urls, https://www.youtube.com/watch?v=TblSa29DX6I.
* My mentor Brian Macharia who supported me and provided me with both feedback and solutions to problems I faced while creating the website.
* My lecturer Simen Daehlin helped me to better write my code to solve a couple of problems I had run into.
* Code institute for the classes, sources, and tutors that they provided me.
* Bootstrap for the media query sizes that I used: https://getbootstrap.com/docs/4.1/layout/overview/

## Content
* The placeholder text and image used in Post 1 about Halo were taken from 

## Media
* Hero Image came from https://media.gettyimages.com/photos/man-plays-the-piano-picture-id156996195?s=612x612
* Post 1's image came from 
* Post 2's image came from 