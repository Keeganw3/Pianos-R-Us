<h1 align="center">Pianos-R-Us</h1>

Website: https://pianos-r-us.herokuapp.com

<p> Pianos-R-Us is a B2C commerce application that aims to sell pianos, keyboards and music books to music lovers and pianists alike. The goal of the website is to provide users with an intuitive, interactive store that they can return to by hearing about discounts through the subscription service or facebook page and by having an account model that saves customer's details.

The site has been created as a retail store that allows products to be filtered out and searched for based on the customers needs.

Users can order one item or multiple items and place them into a cart to be bought at their convenience through the Stripe payment system. They are able to add and remove products from the cart whenever they want and the total cost is displayed at all times. Users can also make an account to save their details, show their order history and give reviews to products.

# Features
## Existing Features
## F1:Navigation Bar
* The navigation bar is provided at the top of the webpage to allow the user to easily explore the website. It also maintains a consistent look across the website. The navbar lets the user find the products they're looking for by providing categories which can be further refined through filtering on the product page. They can also return to the home page through the site logo, and access their cart and account functionalities if they're signed in by clicking on the appropriate icons. If they're not signed in they will be shown links to sign in or register for an account instead. The account icon also changes colour based on whether the user is signed in or not. Lastly, the user can return to the landing page at any time using the site icon in the top left of the navbar.

Fig 1: Desktop Navbar
![Main Navbar](static/screenshots/main_nav_screenshot.png)

Fig 2: Mobile Navbar

![Mobile Navbar](static/screenshots/mobile-navbar-log-out.png.png)

## F2:Landing Page
* The landing page contains a hero image and hero text so that the user can intuitively understand what the app is selling and the goal of the company. There is also a shop now button if the user wants to go straight to the products or they can scroll down to get more information on what the app has to offer.

Fig 3: Desktop Landing
![Desktop Landing Page](static/screenshots/desktop-landing.png)

Fig 4: Mobile Landing

![Mobile Landing Page](static/screenshots/mobile-landing.png)

## F3:Products page
All items in the store are displayed here with their images, names, prices, rating and categories. A user can use the navbar and sort function to filter through the products.

Fig 5: Product Listings
![Products Page](static/screenshots)

Fig 6: Mobile Products Listings

![Products Page](static/screenshots)

Fig 7: Product Listings Filter

![Products Page](static/screenshots/desktop-products-filter.png)

## F4:Product_view Page
If the user clicks the image of the product on the products page they will be brought to the product details page where the product description along with the other product's relevant information is shown. The user can buy the item on its own or add it to a cart to purchase other products.

Fig 8: Product Page
![Product_view Page](static/screenshots/desktop-product-view.png)

Fig 9: Mobile Product Page

![Products_view Page](static/screenshots)

## F5:Product Management
An admin is able to add, remove, and edit products as it is required. In order to add a product it must have a name, image and description. The option to remove and edit a product is only shown to an admin on the products page with two buttons underneath the product's image as shown in the screenshot below.

Fig 10: Desktop Product Management
![Desktop Product Management](static/screenshots/desktop-add.png)

Fig 11: Mobile Product Management

![Mobile Product Management](static/screenshots/mobile-add.png)

## F6:Cart
When a user wants to buy several products at once they can use the cart. This keeps track of all the items the user has requested along with the amount, the cost per item and the total cost. The cart is available whether the user is signed in or not however the user won't be able to save their order history if they don't sign in.

Fig 12: Desktop Cart Page
![Desktop Cart](static/screenshots/desktop-cart.png)

Fig 13: Mobile Cart Page

![Mobile Cart](static/screenshots/mobile-cart.png)

## F7:Checkout
When a user want to buy one or many items they can reach the checkout page where they're delivery and payment card information are required. The payment system has been securely set up using Stripe and several webhooks to notify the user if a problem occurs. When the user successfully places an order they receive a notification on the checkout_success page as shown below.

Fig 14: Desktop Checkout Page
![Desktop Checkout Page](static/screenshots/desktop-checkout.png)

Fig 15: Mobile Checkout Page

![Mobile Checkout Page](static/screenshots/mobile-checkout.png)

## Account Registration
### F8:Registration Page
* This application allows the user to create an account to log in and access additional features on the app. When registering the webpage will ask for a username (that doesn't already exist), an optional email, a password, and the password a second time to confirm it. The webpage will detect the strength of the password entered to make sure it isn't too small or easy to figure out.

Fig 16: Desktop Registration
![Desktop Registration](static/screenshots/desktop-register.png)

Fig 17: Mobile Registration

![Mobile Registration](static/screenshots/mobile-register.png)

Fig 18: Email Verification

![Email Verification](static/screenshots/mobile-verification.png)

Fig 19: Navbar Logged Out

![Navbar Logged Out](static/screenshots/log-out-navbar.png)

Fig 20: Navbar User Logged In

![Navbar Logged In](static/screenshots/user-navbar.png)

Fig 21: Navbar Admin Logged In

![Navbar Logged In(Admin)](static/screenshots/admin-navbar.png)

### F9:Login Page
* Logging in lets the user leave reviews on posts. The register and login links are only in the navbar whenever the user isn't already logged in. When the user is logged in the navbar replaces register and log in with log out to easily allow the user to sign out when they're done.

Fig 22: Desktop Login
![Desktop Login page](static/screenshots/desktop-log-in.png)

Fig 23: Mobile Login
![Mobile Login page](static/screenshots/mobile-log-in.png)

### F10:Logout Page
* The logout page will ask the user if they are certain that they would like to log out and they must press a button to confirm this.

Fig 24: Desktop Logout
![Desktop Logout](static/screenshots/desktop-log-out.png)

Fig 25: Mobile Logout
![Mobile Logout](static/screenshots/mobile-log-out.png)

## F11:Accounts
A user can make an account at anytime using the navbar. If a user does create an account this allows them to save their delivery information, leave reviews and shows a purchase history of previous orders. 

Fig 26: Desktop Account Page
![Account Page](static/screenshots)

Fig 27: Mobile Account Page
![Mobile Account Page](static/screenshots)

## F12:Reviews
An account holder can leave reviews on the bottom of a product's detail page to tell people what they think of a product, how well it works and of it is worth the price. When a review is left they receive a notification that it will be assessed by an admin. Once an admin approves it, the review will appear at the bottom of the page.

Fig 28: Reviews
![Reviews](static/screenshots)

## F13:Footer
* The footer is used to link the user to the site's facebook page and subscription in case they want to learn about deals in the store. There is also text to let people know that this is strictly for educational use only.

Fig 29: Desktop Footer
![Footer](static/screenshots/desktop-footer.png)

Fig 30: Mobile Footer

![Footer](static/screenshots/mobile-footer.png)

## SEO and Marketing
### F14:Keywords and descriptions
A range of words were brainstormed and chosen relating to pianos, music stores and music along with words that a user may tangentially use when looking these up. This included short-tail keywords and long-tail phrases to attract large and relevant numbers of potential customers to the website.

The words and phrases chosen were: piano store, piano shop, electronic piano, thomann dp 95, electronic keyboards, 61 key electronic keyboard, wurlitzer electric piano, best electronic keyboard for beginners, bastien piano basics, piano songbook, piano book, piano classics, teach yourself piano, piano books for beginners, piano stool, piano benches.

The relevancy and authoritativeness of these phrases were chosen by manually looking them up on google and seeing their search traffic combined with using wordtracker.com to check the volume of the web searches and competitiveness.

The words and phrases were used for:
* Description and keyword meta tags in html
* Informational alt tags

### Marketing Techniques
The types of marketing used for this app were social media marketing and email marketing. A facebook page was set up to advertise that this website exists.

Facebook Mockup: https://github.com/Keeganw3/Pianos-R-Us/blob/main/pianos_r_us/facebook_mockup/pianos_r_us_facebook_mockup.pdf

The email marketing was set up through Mailchimp which allowed users to subscribe to a newsletter from the website by entering their email address. This was placed in the footer of the website on each page. The subscribers list is maintained on Mailchimp.

Fig 31: Mailchimp Sub Section
![Mailchimp Subscription](static/screenshots/mailchimp.png)

Fig 32:Mailchimp Subs List

![Mailchimp Subscription List](static/screenshots)

### F15: Stripe Payment System
The service was used to give customers a guarenteed safe way to pay for products so they don't have to worry about losing their credit/debit card details or the payment not going through. Stripe works using payment intents to verify the legitimacy of a user's credit/debit card details when making a purchase but doesn't save this information.

### Custom 404 page
A custom 404 page was added to this application so that this page would aethestically fit in better with the rest of the site.

Fig 33: Custom 404 Page
![404 Page](static/screenshots)

# Future Features to be added
### Staff Page
This page would show the user all of the staff that work on this e-commerce application.

### Edit/Delete Reviews
A user could ask to have their reveiws edited or deleted.

### Toasts
Notifications that would tell the user whenever they add, update or remove items in their cart. They would also tell a user when a purchase has gone through or failed.

# Technologies Used
## Languages Used
* HTML - A mark-up language that uses semantic structures.
* CSS - Cascade style sheets are used to style the quiz and website.
* Python - Programming language used to create the databases, models, and views for this website.
* Javascript - Core programming language used for incorporating third-party libraries and client side webpage behaviour.

## Libraries, Frameworks and Programs
* Gitpod - Used as a platform for writing code. The command line commits and pushes to GitHub.
* GitHub - Used for agile development to track progress on the kanban board.
* Heroku - Cloud platform used to deploy this application and host the code.
* Django - Used for importing frameworks that sped up making the website.
* Bootstrap - Used to build webpages with pre-built css classes.
* AWS - Used to host the images used on the website indefinitely.
* Drawsql - Used to create the entitiy relationship diagram for this project.
* Balsamiq - Used to make the wireframes for the webpages.
* Allauth - Used for account registration.
* Font Awesome - Used to include the icons in the footer.
* Google Fonts - Used to allow different fonts when creating posts.
* Gunicorn - Used as a server to help run on Heroku.
* Django Crispy Forms - Used to easily create forms for logging in.

# Design
## Wireframes
* These wireframes are for the home, products, product_view, checkout, checkout_success registration, login, and logout pages. There are no wireframes for the Django admin pages used for creating posts, comments, and comment approval.

<details>
<summary>Wireframes</summary>

![Wireframes](static/wireframes/pianos-r-us-wireframes.pdf)

</details>

## Entity Relationship Diagrams
* The ER diagram shows the logic between the all class models present in this e-commerce application.

<details>
<summary>Entity Relationship Diagram for all Class Models</summary>

![ER Diagram](static/er_diagrams/pianos_r_us_er_diagrams.png)

</details>

## Planning
* A project in Github was used as an Agile Tool for tracking the building process of this project. Issues were tracked using a kanban board and linked to multiple Epics that would show the over all progress of this project's development. Each issue was tested to ensure that they could be considered completed. The criteria of these tests are outlined below.

Wireframes and a data schema were created so that I had a clear vision of the website that I'd want to make.

# Testing
### User Testing
The navbar was tested by clicking each link and icon with each type of user to see if they worked and expanded like intended.

## Manual Testing
### Media Queries
I tested the media queries by manually adjusting the screen size from 576px-1200px to make sure the appropriate changes were taking place at each media query.

At 576px 

At 768px 

At 1000px  

At 1200px 

## Known Bugs
* The text on the confirmation email page is hidden underneath the navbar.

# Deployment
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
## Credits
* Most of the code and issues were heavily influenced by the information on the "Boutique Ado" walkthrough project from Code Institute.
* My mentor Brian Macharia who supported me and provided me with both feedback and solutions to problems I faced while creating the website.
* Code institute for the classes, sources, and all of the tutors that they provided me and spent hours with me to help me find solutions when creating this website.
* Bootstrap for the media query sizes that I used: https://getbootstrap.com/docs/4.1/layout/overview/
* Mailchimp boilerplate taken from Mailchimp linked below. 
* Footer Boilerplate taken and edited from Code Institute linked below.

## Content
* The name, description and price for the wurlizter was taken from https://reverb.com/item/51972008-wurlitzer-200a-electric-piano-1970s-black?bk=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkNzA3MTM3Yy1mY2IzLTRkY2ItOGEzNS1hYmNjY2I3NmI3MjUiLCJpYXQiOjE2NTkzMDY2MDQsInVzZXJfaWQiOiIiLCJzZXNzaW9uX2lkIjoiIiwiY29va2llX2lkIjoiMjQxY2I1MmItNmQ1Zi00YTgwLTk4OGMtZmZjMzM3OWE0M2IyIiwicHJvZHVjdF9pZCI6IjUxOTcyMDA4Iiwic291cmNlIjoiTk9ORSJ9.4Di4E8R3fcYIBAobeneTxocOqhIR5b4s5nYk7V6lM_U
* The name, description and price for the Thomann DP-95 B was taken from https://www.thomann.de/ie/thomann_dp_95_b.htm
* The name, description and price for the Thomann DP-95 WH was taken from https://www.thomann.de/ie/thomann_dp_95_wh.htm
* The name, description and price for the Startone MK-400 was taken from https://www.thomann.de/ie/startone_mk_400.htm
* The name, description and price for the Thomann SP-5600 was taken from https://www.thomann.de/ie/thomann_sp_5600.htm
* The name, description and price for the Adjustable Keyboard / Piano Bench was taken from https://www.gear4music.ie/Keyboards-and-Pianos/Adjustable-Keyboard---Piano-Bench-by-Gear4music/8XQ?origin=product-ads&gclid=Cj0KCQjw0JiXBhCFARIsAOSAKqBRwUPbh-ZzOsHSpWUVCCy29czTLcon-TpYm-BdLxVTIrqh1BgQfX8aAqapEALw_wcB
* The name, description and price for Piano Time 1 was taken from https://www.amazon.co.uk/Piano-Time-1-Bk/dp/0193727846/ref=asc_df_0193727846/?tag=googshopuk-21&linkCode=df0&hvadid=310081590442&hvpos=&hvnetw=g&hvrand=15863075280230236291&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007850&hvtargid=pla-525138499170&psc=1&th=1&psc=1
* The name, description and price for the 65 Famous Pieces of Classical Music for Solo Piano Volume II was taken from https://www.amazon.com/dp/B09TWVDCMZ/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B09TWVDCMZ&pd_rd_w=e0NPT&content-id=amzn1.sym.3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_p=3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_r=5C0MD8ADE4XZ393WM8BR&pd_rd_wg=CQdZu&pd_rd_r=44c5a3ba-0fb8-4480-a71b-6923c6fe201e&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUkU1MkxITzVTMkdWJmVuY3J5cHRlZElkPUEwMzQwNDk0MVdGQTVZTE5YM1JYJmVuY3J5cHRlZEFkSWQ9QTA2NjMwNjgyN1MzQVlSN0tEUjlYJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==
* The name, description and price for the Classical Piano Sheet Music | 60 Famous Solos  was taken from https://www.amazon.com/dp/B09XDKH164/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B09XDKH164&pd_rd_w=e0NPT&content-id=amzn1.sym.3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_p=3be1c5b9-5b41-4830-a902-fa8556c19eb5&pf_rd_r=5C0MD8ADE4XZ393WM8BR&pd_rd_wg=CQdZu&pd_rd_r=44c5a3ba-0fb8-4480-a71b-6923c6fe201e&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUkU1MkxITzVTMkdWJmVuY3J5cHRlZElkPUEwMzQwNDk0MVdGQTVZTE5YM1JYJmVuY3J5cHRlZEFkSWQ9QTA0MDQ5NDAxWDZWU0o2MklUVDBPJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==

## Media
* The hero image came from https://unsplash.com/s/photos/grand-piano
* The Wurlizter image came from https://soundgas.com/wp-content/uploads/2020/12/Wurlitzer-Model-200-Electric-Piano-SN72352L-Cover-2.jpg
* The Thomann DP-95 B image came from https://a.storyblok.com/f/49568/3604x3420/a500c85994/002_neu.jpg/m/1600x0/filters:quality(80):format(jpeg)
* The Thomann DP-95 WH image came from https://a.storyblok.com/f/49568/3378x3194/5109b71e0b/002.jpg/m/1600x0/filters:quality(80):format(jpeg)
* The Startone MK-400 image came from https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/515755/16770214_800.jpg
* The Thomann SP-5600 image came from https://a.storyblok.com/f/49568/8130x2027/3fa10b8e4e/tps_fo1_378054_001.jpg/m/1600x0/filters:quality(80):format(jpeg)
* The Adjustable Keyboard / Piano Bench image came from https://d1aeri3ty3izns.cloudfront.net/media/43/435426/76/preview.jpg
* The Piano Time 1 image came from https://images-na.ssl-images-amazon.com/images/I/51SgFovOecL._AC_SX60_CR,0,0,60,60_.jpg
* The music masterpiece image came from https://images-na.ssl-images-amazon.com/images/I/41B9b+GuARL._AC_SX60_CR,0,0,60,60_.jpg
* The classical piano book image came from https://images-na.ssl-images-amazon.com/images/I/41C3WbeVgzL._AC_SX60_CR,0,0,60,60_.jpg
* The Waltons image on the facebook mockup came from https://www.facebook.com/waltonsmusic/
* The Lucan School of Music on the facebook mockup came from image came from https://www.facebook.com/lucanschoolofmusic/
* Beethoven image on the facebook mockup came from was taken from https://en.wikipedia.org/wiki/Ludwig_van_Beethoven
* To crop the images on the facebook mockup I used https://crop-circle.imageonline.co/

## Code Sources
* Boilerplate text taken for the footer of index.html is from https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRWM101+2021_T1/courseware/2b2a6057abf44272955637c09687ab43/acc4b7d56e3a400ebe110e5d734ce767/
* Mailchimp code in the footer in base.html was taken from Mailchimp at https://us10.admin.mailchimp.com/audience/forms/embedded-form/editor?id=900531