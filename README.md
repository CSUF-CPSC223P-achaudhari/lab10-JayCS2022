[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/NPwDe4J7)
# Laboratory 10

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. threading
1. Run and test a Python program.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/aadi1720/lab10-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab10-username
     ```
     
## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Warehouse Robot.  Think of the warehouse similar to a large Amazon Fulfillment Center with thousands of robots moving around the facility to fill up a physical shopping cart.  A user via the web or an app selects several items they want to purchase.  The list is sent to a robot clerk, who in turns dispatches several robots that fetch the items and bring them back to the cart.  The robots work simultaneous i.e. in parallel with each other.  Once all the items are returned to the cart the items in the cart get shipped out for delivery.  The Tuffy Titan Warehouse Robot will simulate this workflow using multiple threads (each fetch robot will use a different thread).
1. Your are given an `inventory.dat` file which contains a dictionary of inventory items.  The data structure and file contents is as follows:
     ```
	inventory dictionary:
		key: item number as a string
		value : item list

	item list:
        element 0: item description as a string
        element 1: seconds as an integer
	
	actual file contents:
	{
	"101": ["Notebook Paper", 2],
	"102": ["Pencils", 2],
	"103": ["Pens", 6],
	"104": ["Graph Paper", 1],
	"105": ["Paper Clips", 1],
	"106": ["Staples", 4],
	"107": ["Stapler", 7],
	"108": ["3 Ring Binder", 1],
	"109": ["Printer Paper", 1],
	"110": ["Notepad", 1]
	}
     ```
1. Create a `bots` module to meet the following requirements:
     1. Create a file named `bots.py`.
          1. Define a function named `bot_clerk` to meet the following requirements:  
               1. Take an items list as a positional parameter.  This a list of item numbers to be fetched and placed in the cart. Example format is `['101','102','103']`.
               2. Define a cart list and a thread lock.  All bots will use the same cart and lock.
               4. Separate the items that have been passed to the clerk into 3 robot fetcher lists (for simplification, we will assume each clerk will have a maximum of 3 robots).  The algorithm to separate the items should follow this:
                    1. item 1 goes to robot fetcher list 1
                    1. item 2 goes to robot fetcher list 2
                    1. item 3 goes to robot fetcher list 3
                    1. item 4 goes to robot fetcher list 1
                    1. item 5 goes to robot fetcher list 2
                    1. item 6 goes to robot fetcher list 3
                    1. item 7 goes to robot fetcher list 1
                    2. etcetera
               6. Launch each robot fetcher using a new thread and passing it the robot fetcher list (1 through 3 respectively), the cart list, and the lock.
               7. Return the cart list to the calling program.  The final cart list should have all the items that were fetched and in the order that they were placed in the cart. 
          1. Define a function named `bot_fetcher` to meet the following requirements:  
               1. Take an items list as a positional parameter.  This a list of item numbers to be fetched and placed in the cart. Example format is `['101','102','103']`.
               1. Take a cart list as a positional parameter.  This is a list of items that have been placed in the cart.  Example format is `[['109', 'Printer Paper'], ['102', 'Pencils']]`.
               2. Take a thread lock as a positional parameter.
               3. Loop through each item in the item list.
               4. Sleep for the number of seconds corresponding to the item from the inventory (this simulates the robot going out into a particular zone in the warehouse and returning to the cart, the farther the zone the larger the seconds).
               5. Append the item number and description to the cart list using the format `['102', 'Pencils']` (this simulates the robot dropping the item in the cart).  Ensure that proper locks are placed around this task to ensure that no other robots are appending at the same time.
1. You do not need to submit a main.py program but it is suggested that you create one and use the below typical input and output to call the `bot_clerk` function as you are developing the bots module.
1. Typical input and output for the `bot_clerk` function (the input is what is passed to the function and the output is what is returned):
     ```
     INPUT  : []
     OUTPUT : []
     
     INPUT  : ['104']
     OUTPUT : [['104', 'Graph Paper']]

     INPUT  : ['106','109','102']
     OUTPUT : [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']]

     INPUT  : ['103','108','102','110','106']
     OUTPUT : [['108', '3 Ring Binder'],['102', 'Pencils'],['106', 'Staples'],['103', 'Pens'],['110', 'Notepad']]

     INPUT  : ['106','102','108','109','103','101','110','104','107','105']
     OUTPUT : [['108', '3 Ring Binder'], ['102', 'Pencils'], ['101', 'Notebook Paper'], ['106', 'Staples'], ['109', 'Printer Paper'], ['110', 'Notepad'], ['105', 'Paper Clips'], ['103', 'Pens'], ['104', 'Graph Paper'], ['107', 'Stapler']]

     ```

1. Run the unit testing program to ensure that your program runs as expected.  **NOTE: This may take approximately 45 seconds to complete due to the many sleeps that will be executed. It may appear to hang at the end, however it is actually going through the complete process a second time after the unit test finishes - be patient**  

    ```
    python3 -m unittest -v test1
    python3 -m unittest -v test2
    python3 -m unittest -v test3
    python3 -m unittest -v test4
    python3 -m unittest -v test5
    
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
bots.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|5|bots.py file submitted contains the bots module and meets the program requirements|
|5|unit test passes Test01_EMPTY_ITEM|
|10|unit test passes Test02_ONE_ITEM|
|10|unit test passes Test03_THREE_ITEMS|
|10|unit test passes Test04_FIVE_ITEMS|
|10|unit test passes Test05_TEN_ITEMS|
