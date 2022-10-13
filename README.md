# Bulk Updating Public Access Models 

Alma does not currently support updating public access models in bulk, such as with the Change Portfolios Information job.

This script iterates through a CSV file of portfolios and sets all of them to the public access model that you choose.

# How it Works

Using the values in the CSV file, the script calls the Retrieve Portfolio API. Then the script searches for the access model field in the retrieved XML and sets the access model.

Lastly, the script constructs calls the Update Electronic Portfolio API to update the portfolio in Alma. 

# Installation With Visual Studio Code

Install Visual Studio Code

Download repo from Github (folder)

Place folder in C drive (or edit path in script to wherever you want to put the folder)
File > Open Folder > Select repo folder

Install Python 3.10.8 on your computer (https://www.python.org/downloads/release/python-3108/)
Select "Add python.exe to PATH" in installer
Customize installaion > make sure everything is checked > select install python 3.10 for all users and  make note of the location.

Open update_access_model.py in Visual Studio, and click "Select Interpreter" on bottom-right hand side of screen. Find Python310 folder on local computer (likely in C:\Program Files) select Python 3.10 (64-bit) executable as interpreter.

To install required libraries, click "Terminal > New Terminal" (terminal should say your location is "PS C:\Change_Access_Model>", depending on where you saved it). Enter command "pip3 install -r requirements.txt". If you have any trouble, see what libraries failed to install you could try changing the version of certain libraries in requirements.xml if they are out of date by looking them up.

#API Key 

Log in as your institution in the developer's network and create an API key with the following permissions:

ELECTRONIC

READ/WRITE (Production)

Keep copy of key in secure location, add to script only when running it.

# Setup

Set access model code in script which will update all portfolios in CSV file to that value.

Set the path of the CSV in the script, or place it where it is expecting in C:\Change-Access-Model.

Format of CSV should be as follows (the script skips the header). 

Collection Id,Service Id,Portfolio Id
61176767260005201,62176767250005201,53195012660005201
61176767260005201,62176767250005201,53195123680005201