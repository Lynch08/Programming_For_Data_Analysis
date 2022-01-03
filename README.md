# Programming_For_Data_Analysis 


![](https://upload.wikimedia.org/wikipedia/en/6/6b/GMIT_Logo_2011a.jpg)

Lecturer: : Dr Brian McGinley 
Module: Programming For Data Analysis 
Author: Enda Lynch  
Github Username: Lynch08  
GMIT Email: G003987951@gmit.ie  
Personal Email: E.Lynch@Kostal.com  

This repository contains one jupter notebook where I looked at a data set containg values related to movie attendence since 1995. (movie_ticket_sales.ipynb)


## Table of Contents
See  - main headings are hyperlinked.    
    

## Planned Project Outcomes
1. To break the project and assignment down into small manageable tasks
2. To gain an understanding of how to simulate relevent data
3. To integrate the skills I had acquired so far in this course to visualise and analyse my "datasets", and display my findings
4. To expand my knowledge of the python libraries and tools to make the code as simple and readable as possible for the reader
5. To learn how to best optimise my time between research, programming, problem-solving and analysis.

## The Task and Expectations
[Assessment Sheet](https://github.com/Lynch08/Programming_For_Data_Analysis/blob/main/ProgDAProject.pdf)

## The Repository Content 
 - 1 jupyter notebooks (movie_ticket_sales.ipynb) that holds the explanation, code, visuals and citeations for the assignment and project.
 - The assignment and project details in PDF form from Dr. Brian McGinley
 - A requirments.txt file that contains all of the dependancies required to run the both notebooks from the repository in the same environment
 - A readme file explaining the objectives, outcomes and instructions on how to view the notebook in both editable and static format.
 - A data folder that contains yearly_ticket_sales.csv. A csv file that I read in to analyse so I can simulate similar data.
 - An images folder for any images I have used


## View Notebook in Static Format(Online)
If you wish to view the pyplot.ipynb notebook in static (uneditable) format click here:  
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)(https://nbviewer.org/github/Lynch08/Fundementals_Of_Data_Analysis/blob/main/pyplot.ipynb)  



## How to download this repository (editable version)
Go to GitHub.com.
Go to my repository: https://github.com/Lynch08/Programming_For_Data_Analysis
Click the clone/download button.
Save the repository to a local folder location on your machine.
You will need to navigate to this folder location on the command line in order to run the program.
Details on how to run each individual script in this repository is included later in this Readme file.

### Python Dependancies 

I have a requirements.txt file that you can use to install all of the dependencies required to run the notebook in the exact same environment - however below are the main dependencies if you would like to do that manually. After cloning the repository navigate to the folder using the command prompt and use the ```pip install``` command if you want to use the requirments.txt file.
See this video for full instructions on how to install: https://www.youtube.com/watch?v=mBcmdcmZXJg 


**Required**
- Download Python environment - I recommend ([Anaconda](https://www.anaconda.com/products/individual)) 
    - Libraries to import within the python environment (all are linked to official documentation - **only first 4 required for pyplot.ipynb, all required for cao.ipynb**)
        - [Numpy](https://numpy.org/doc/)
        - [Pandas](https://pandas.pydata.org/docs/)
        - [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
        - [Seaborn](https://seaborn.pydata.org/)
        - [Random](https://docs.python.org/3/library/random.html)
        - [Scipy](https://docs.scipy.org/doc/scipy/reference/)        
        - [Scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
        - [Numpy.random](https://numpy.org/doc/stable/reference/random/index.html)
   
**Not required but helpful**  
cmder - this is a command line emulator that in my opinion is easier to use and cleaner than the windows cmd window. [Download Cmder Here](https://cmder.net/)


### Notebook Dependancies  
##### movie_ticket_sales.ipynb  
yearly_ticket_sales.csv - located in the data folder

### Running the Jupyter Notebook
 - On the command line navigate to the folder location where the repository has been downloaded and saved to using the cd command to change directory.  
 - Type jupyter lab on the command line and press enter.  
 - After a short wait jupyter notebook will open in your web browser (I would suggest Chrome).  
 - Open the required notebook in the browser and the notebook containing the code and comments that I wrote for this assignment will be displayed.  
 - Before beginning I would suggest going to the Kernel option on the menu bar and if you want to run the notebook yourself choose "Restart Kernel and Clear Outputs". If you want the notebook to run automatically choose "Restart Kernel and Run All Cells".  
 - If you want to run the code in any particular cell, click into the cell, hold down the shift key, press enter and the command will run and the output wil be displayed in the next cell - please note the cells are not ready to be run so you cannot begin trying to run cells halfway down the note book.  
 - To change between edit and read mode at any time click into a cell and press the ESC key.  
 - When you have finished viewing the jupyter notebook close the web browser and return to the command line. Press Ctrl + C on the command line to kill the program.  



## Citations
See bottom of Notebook
