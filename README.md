# Bulk Updating Public Access Models 

Alma does not currently support updating public access models in bulk, such as with the Change Portfolios Information job.

This script iterates through a CSV file of portfolios and sets all of them to the public access model that you choose.

# How it Works

Using the values in the CSV file, the script calls the Retrieve Portfolio API. Then the script searches for the access model field in the retrieved XML and sets the access model.

Lastly, the script calls the Update Electronic Portfolio API to update the portfolio in Alma (access model may not immediately appear in Alma). 

# Installation With Visual Studio Code

Install Visual Studio Code

Download script files from Github (Code > Download ZIP)

Place extracted folder in C: drive (or edit path in script to wherever you want to put the folder; be sure folder is called Update_Access_Model).

In Visual Studio, select File > Open Folder > Select the folder.

Install Python 3.10.8 on your computer (https://www.python.org/downloads/release/python-3108/)
Select "Add python.exe to PATH" in installer
Customize installaion > make sure everything is checked > select install python 3.10 for all users and make note of the location where it is saved.

Open update_access_model.py in Visual Studio, click "Select Interpreter" on bottom-right hand side of screen. Find Python310 folder on local computer (likely in C:\Program Files) and select Python 3.10 (64-bit) executable as the interpreter.

To install required libraries, click "Terminal > New Terminal" (terminal should say your location is "PS C:\Change_Access_Model>", depending on where you saved it). Enter command "pip3 install -r requirements.txt". If it doesn't recognize the pip command, you might have an issue with the Python PATH environment variable.

If you have any trouble installing the libraries, see what libraries failed to install. You could try changing the version of certain libraries in requirements.xml if they are out of date by looking them up, although the script may only work with the version listed.

#API Key 

Log in as your institution in the developer's network and create an API key with the following permissions:

ELECTRONIC

READ/WRITE (Production) *select sandbox if testing in sandbox

Keep copy of key in secure location, and add to script only when running it.

# Setup

Set access model code in script which will update all portfolios in CSV file to that value.

Set the path of the CSV file in the script, or place it where the script is expecting in C:\Change_Access_Model. Be sure that .csv is not in the title of the file, just that it is a csv type file

Format of CSV should be as follows (the script skips the header). 

Collection Id,Service Id,Portfolio Id<br />
61176767260005201,62176767250005201,53195012660005201<br />
61176767260005201,62176767250005201,53195123680005201<br />
61176767260005201,62176767250005201,53195123680005201
