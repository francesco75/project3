

# Project Stream 3
## Overview
### Title Unicorn Attractor
## What Does it do ?
This Application create the account and after the ticket with bug or feature.
The bug vote is free and the feature vote provides the amount of money.
I used the chart to show the payment feature amd the most payment and the  most vote with the time date.
## Starter
 I started to create the Web Pages writing in the paper after i used the text file 
 to develop the text and focus different points of my Website pages. I created the Authentication and CRUD 
 manage the database to create the vote bug and feature single payment. 
 I create the charts using the database payment and vote bug.

## Features
- Index.html: 
     My Homepage shows the presentation application.
- Account :
     Authentication with Register Login Profile Logout
- Ticket:
    List  add and read the ticket with bugs and feature and button to see the single ticket
  - Ticket Detail:  vote the bug or feature with payment Paypal and count the vote for each ticket 
- Charts :
     Create the chart with data feature and vote: Rowchart,Piechart,Totalchart,SelectMenuChart
     
### Tech Used
- Python
- Django Framework
Unicorn uses the Model with Database, View,  Template with html file  Url links

- Bootstrap
     - Grid: The structure with rows and columns
     - Navbar: Navigation with links
     - Table: The ticket list with bugs and features
 
- Data : 
     - SQL Feature_payment
     - SQL Vote
- Javascript libraries: D3.js. Crossfilter.js, DC.js
     - PieChart Barchart 

- Payment
     - Paypal System

# Testing
## Testing Browser
 - The Testing Browser tests  the website on the different browser and
    checks the different like the picture size  and responsive navbar and charts 
 - Google Crome:
     - All the pages respond very well and jquery library work very well. 
       The Navigation Bar works perfect.The Charts work well  
       Final Testig is good
       
 - Microsoft Edge  
     - The pages respond very well . All the buttons work well.The Navigation Bar
       has the different size but the responsive is good.The Charts work well.
       Final Testing is good.
       
 - Mozilla Firefox
     - The pages respond very well . All the buttons work well.The Navigation Bar
       has the different size but the responsive is good.The Charts work well.
       Final Testing is good.
       
 - Interner Explorer     
      - All  the pages and navbar work well  
        The charts work well. 
        Final Testing is good
 ## Testing Devices Responsive
 ### Tech Used : Blisk 
   - This Testing responsive is used to test the website with
      the different devices and study the navbar reactive and the 
      table list ticket and their charts responsive.
   - Phones : 
               All the pages work well and navbar works perfect                 
               The Testing is Good.
   - Tablets :
               All the pages work well and navbar works perfect.
               The charts and buttons work perfect.
               The Testing is Good.
               
   - Desktop :
               **HIDPI**: All the pages work well and navbar works perfect.
               The Charts and buttons work perfect.
               The Testing is Good.
               **MDPI**: All the pages work well and navbar works perfect.
               The Charts and buttons work perfect.
               The Testing is Good.
               
   - Laptop M/S  :  All the pages work well and navbar works perfect.
               The Charts and buttons work perfect.
               The Testing is Good.
                          
 ## Testing Speed Pages               
 ### PageSpeed Tools
   - This Testing tests the speed pages and optimization betweeen the Desktop
      and Mobile checking almost the pages.
   - Home 
       - Desktop   
           Speed: Unavailable;
           Optimization: Good
       - Mobile
           Speed: Unavailable
           Optimization: Medium 79/100
   - Register
        - Desktop   
           Speed: Unavailable
           Optimization: Good 83/100
        - Mobile
           Speed: Unavailable
           Optimization: Medium 79/100
   - Chart
        - Desktop   
           Speed: Unavailable
           Optimization: Good 82/100
        - Mobile
           Speed: Unavailable
           Optimization: Medium 75/100
   - Log in                             
       - Desktop   
           Speed: Unavailable
           Optimization: Good 83/100
       - Mobile
           Speed: Unavailable
           Optimization: Medium 79/100
   - Ticket 
        - Desktop   
           Speed: Unavailable
           Optimization: Good 83/100
        - Mobile
           Speed: Unavailable
           Optimization: Medium 79/100  
   - Ticket Detail
        - Desktop   
           Speed: Unavailable
           Optimizaton: Good 83/100
        - Mobile
           Speed: Unavailable
           Optimization: Good 79/100     
### Deployment
  - GitHub
      - Initial Commit : Basic codec and template with ticket bug and payment
          feature .
      - Updated database: Load the database sql lite
      - Remove settings: remove settings.py
      - Removed Bootstrap files: remove some files that created the problem
          with deployment
      - some changes: Small changes the database.
      - changes commit: These changes manage the navbar and the security first the 
          registration and log in or log out.
      - final commit: The code with the last changes     
  - Heroku
      - base.py : Replace the settings.py 
      - Dev.py : Manage the debug_toolbar and debug = true and database sqlite
      - Staging.py : Manage the url config database and mysql-python
      - Requirements folder install all the dependencies base.txt, staging.txt,dev.txt
