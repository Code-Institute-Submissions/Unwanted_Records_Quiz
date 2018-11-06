# Unwanted Premier League records quiz

This application is a football trivia quiz, testing the user's knowledge of obscure and unwanted football records from the 
English Premier League. users are invited to create a username in order to take the quiz, which tracks their progress and 
awards them three points for each correct answer. The ultimate goal for the user is to 'secure Premier League survival' by 
scoring 36 points or more. Once the user has completed the quiz, their final score will be revealed, and they will be able 
to see where they rank among other players on the leaderboard.

### UX

This application was developed for football fans to test their knowledge of obscure facts. I personally know quite a lot of 
people who are quite competitive when it comes to football knowledge. This application is perfect for these individuals, as 
it provides a platform whereby they can challenge their friends and see where they rank among one another. The application 
also provides links to various social media sites, to promote circulation of the quiz among friends.

- As an end user, I want to take a football trivia quiz, to test my knowledge
- As an end user, I want to take a football trivia quiz, as a means of entertainment
- As an end user, I want my score to be documented, to see how it compares with others
- As an end user, I want to be able to challenge my friends to play, to see if they can beat me

Mockups created for this project can be found within the 'planning' folder.

### Features

- User form: enables users to initiate the quiz and create user instances which are saved in the session, simply by entering a user name
- Answer input: allows for correct answers with minor discrepancies, such as answers beginning with lower case letters, meaning users don't have to be as attentive
- Score counting function: allows users to publicise their scores by saving individual scores to a csv file and presenting them in the browser
- Leaderboard function: enables users to compare scores, by calculating individual scores and ranking them within the browser
- Score summary: provides the user with a summary of their performance, based on their final score

### Technologies used

Python was used to write the underlying code, including all functions, routes and logic. The project was built inside the Flask 
framework, which helped display the output from the Python logic. The website was developed upon a basic Bootstrap template found 
online.

HTML and CSS (see 'style.css') were used to enhance the structure and appearance of the website, while jQuery was used to enhance 
aspects of the game - specifically by revealing the answer options to the user through a slidedown function on click (see 'script.js'). 
Each page also includes sticky social media sidebars, instructions on how to create which were found online.

### Testing

Both automated and manual tests were conducted to ensure that all features are fully functional. Manual tests were created to make sure 
that the 'lowercase' and 'strip' functions worked alone and in tandem.Unit tests can be found in the 'unittests' folder, demonstrating 
testing of:

- Lowercase and strip functions for user form input
- Score sorting functionality
- Functionality for updating question number and user score upon completion of answers
- Score and question number reset function
- Score summary function output based on user score

This project was developed using a mobile-first approach. A Google Chrome screen resolution tester was consistently used throughout 
development to ensure that pages and functionalities were easy to navigate and use via various platforms and screen sizes.

The app was extensively tested across a range of browsers across both Windows and Mac operating systems, including Chrome, IE, Firefox, 
Microsoft Edge, and Opera, using CrossBrowserTesting.com's free service. No bugs or issues were encountered during the testing process.

### Deployment

This application has been both pushed to Gitub and deployed to Heroku. Config variables have been added to the Heroku dashboard to ensure 
that the application works. A Procfile and requirements.txt file have also been included for assistance with setting up the app. As data 
is stored in a csv file, there is have been no complications with regards to databases.

### Credits

## Content

The social media sidebar was based on a how to guide by w3schools... https://www.w3schools.com/howto/howto_css_sticky_social_bar.asp

## Media

Images used within this project were accessed via a Google search for images labeled for noncommercial reuse.