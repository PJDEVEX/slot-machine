<h1 align="center">Slot Machine App</h1>

<a href="https://slot-machine-pj.herokuapp.com/" target="_blank" rel="noopener" alt="Slot Machine App, click here to open the website"><img src="/workspace/slot-machine/images/slot-machine.png" alt="Slot machines" max-height="650px" max-width="1300px"></a>
<hr>
View the repository in GitHub
<a href="https://github.com/PJDEVEX/slot-machine" target="_blank" rel="noopener">here</a>

View the live project
<a href="https://slot-machine-pj.herokuapp.com/" target="_blank" rel="noopener">here</a>

# **Slot Machine App**

Slot Machine App, is a Python terminal app that runs on Heroku.

Slot Machine App is a replication of gambling slot machine with a text based application.

This App allows a user to have some entertainment and spend his/ her spaire time.

## How to use the App

* User is asked to enter an amount he/ she would like to deposit to start the game
* it  confirms the balance and get a reconfirmation to contiune the game asking to press enter to continue or "q" to quit
* Then user is asked to enter the number of line to be bet in the range of 1-3
* After that the user shall decide on the bet per line with the ceiling of $ 200
* IT reconfirms the amount per line, number of lines and total bet
* The results deplay to the user along with winning or losing results followed by available current available balance.
* Again, requst for a confirmation for a contiunation
* If deciced to quit, thanking note is displayed while requeting to collect the balance amount.


## User Experience (UX)

### User Stories

Target Audience – Adults (above 18) who are interested in stimulating gambling environment for entertaintment and spend spair time 

As a User I want to:
* User friendly app with ease of navigation
* spend some free time for entertainment purpose 

### User Experience in this Game
The app stimulates a gambling enviroment that user can enjoy

## Features

* User can deposit money
* Validating the data entered when depositing money
* Confirms the balance
* Gets confirmation to proceed or quit
* Allows user to enter number of lines to be bet on
* Validating the data entered on betting
* Allows user to enter amount to be bet on per line
* Validating the data entered for number of lines
* Returns with slot results, amount won/ lost, and line won
* Gives a confirmation on available balance


### Data Model Design

**Use Case Diagram and Flow Control**

A flow control was used to visualize the whole process of the app.

* The Diagram was drafted to capture the app's functionality and the user interaction.

* This also allowed the design of the user input validation checks to be visually clear before the code was written.

![Flowchart](/images/processchart.png)

**Wireframes**

Wireframes were drawn to have the basic idea of what needs to be build.

![User Interface](/images/wireframe.jpg)


**Future Developments**

* Major developments to be identified

**Classes and functions**

* All the functions are given description on each of their functionality
* Functions are grup for execution as a main function
* Separate function was created for iteration of related when running the program



## Libraries & Technology Used

**Python Libraries**
* random 

    pip install was used to install Python Libraries via terminal using the command `pip install 'package name'` to install packages in gitpod.
    
    The command `pip3 freeze > requirements.txt` was used to install dependencies for proper deployment on heroku. 

* random

    Python inbuit random library was used to generate random unmbers and their functionality 


* [LucidCharts](https://www.lucidchart.com/) was used to create the UML Case Diagram and the Flowchart.


## Testing
*   Methods such as print() as the code developed was used to check for errors.  This helped check that everything was behaving as expected.

### Manual Progresive Testing of Functions ###

* Get Deposit
![get-deposit](/images/deposit.png)
Note: Function performs as expeted

* Get the number of lines

![get-the number of lines to bet on](/images/get-no-of-lines.png)
Note: Function performs as expeted

* Get bet

![get-bet-per-line](/images/get-bet.png)
Note: Function performs as expeted

* Slot machine spin

![slot-machine-spin](/images/slot-machine-spin.png)
Note: Function performs as expeted

* Check winnings

![check-winnigs](/images/check-winnings.png)
Note: Function performs as expeted

* Spin function and revised main

![Spin-function-and-revised-main](/images/revised-main.png)
Note: Function performs as expeted


*   Errors or warnings were fixed as they appeared such as indentation errors, extra space issues.  It helped keep the code clean and readable so other errors or bugs that arose were identified more easily.

*   After deployment all features were checked on Chrome, Firefox, Brave and Edge.

*   The app was deployed early on in development and checked regularly to ensure app working corectly and any errors were handled early on.

*   Testing inputs were used to ensure user inputs would be handled correctly and appropriate feedback to the user was shown on screen.  As mentioned above in the Features Section for how user inputs were handled.
           
 
### Bugs Found

* No major bugs identified during the deplyment 
* Almost all of the bugs have been fixed during the development stage as and when they were identified

### Validator Testing

[pythonchecker.com](https://www.pythonchecker.com/) was used for validating the code.  
Receive 68% (Good) 

![pep8 online](/images/code-validation.png)

## Deployment

The site was deployed via [Heroku]( https://id.heroku.com/login), and the live link can be found here: [Slot-machine-pj](https://slot-machine-pj.herokuapp.com/) 

This project was developed utilizing the [Code Institute Template]( https://github.com/Code-Institute-Org/python-essentials-template).  Some of the deployment steps below are specifically required for the new CI template and may not be applicable to older versions, or different projects.

Before deploying to Heroku pip3 freeze > requirements.txt was used to install dependencies.

1.	Log in to [Heroku]( https://id.heroku.com/login) or create an account if required.
2.	Then, click the button labeled **New** from the dashboard in the top right corner and from the drop-down menu select **Create New App**.
3.	You must enter a unique app name, (slot-machine-pj).
4.	Next, select your region, (I chose Europe as I am in Sweden).
5.	Click on the **Create App** button.
6.	The next page you will see is the project’s Deploy Tab.  Click on the **Settings Tab** and scroll down to **Config Vars**.
7.	Click **Reveal Config Vars** and enter **port** into the **Key** box and **8000** into the **Value** box and click the **Add** button.
8.	Next, scroll down to the Buildpack section click **Add Buildpack** select **python** and click **Save Changes**.
9.	Repeat step 8 to add **node.js**.
o	**Note:** The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10.	Scroll to the top of the page and now choose the **Deploy** tab.
11.	Select **Github** as the deployment method.
12.	Confirm you want to connect to GitHub.
13.	Search for the repository name and click the connect button.
14.	Scroll to the bottom of the deploy page and select preferred deployment type:

* Click either **Enable Automatic Deploys** for automatic deployment when you push updates to Github.

* Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.


### Version Control
*   Git was used as the version control software. Commands such as git add ., git status, git commit and git push were used to add, save, stage and push the code to the GitHub repository where the source code is stored.

## Credits

Some helpful tutorials I used to help me with coding some of the design ideas were:

**Documentation used**

* https://www.w3schools.com/

* [Python Tutorial - Python Full Course for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=21423s)


## Acknowledgements

A big shout out to [Code Institute](https://codeinstitute.net/ie/) for providing me with the opportunity to create this project.

I'd like to thank my mentor [Daisy McGirr](https://github.com/Daisy-McG) for invaluable guidance and for reviewing my website.

This project was made possible due to the Google Search.