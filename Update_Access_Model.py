#!/usr/bin/python3
import requests
import csv
import os
from xml.etree import ElementTree as ET

# Configs #####################################################################

# API key must have electronic read/write permissions.
apikey = ''

# Set the access model you want to change all the portfolios to
access_model_code = ''

# Set location of csv file the script will process
spreadsheet_directory = 'C:\Update_Access_Model'

# CSV file should be in the following format:
# Collection Id,Service Id,Portfolio Id
# 61176767260005201,62176767250005201,53195012660005201
# 61176767260005201,62176767250005201,53195123680005201
# 61176767260005201,62176767250005201,53195123680005201

# Open CSV spreadsheet and process
with open(f'{spreadsheet_directory}\\Access_Model.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # skip header
    for row in csv_reader:
        # parse
        collection_id = row[0]
        service_id = row[1]
        portfolio_id = row[2]
        
        # get portfolio
        r = requests.get(f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/electronic/e-collections/{collection_id}/e-services/{service_id}/portfolios/{portfolio_id}?apikey={apikey}')
    
        # check for errors, log if needed
        if r.status_code != 200:
            with open('log.txt', 'a', encoding="utf-8") as log:
                log.write(portfolio_id + " Could not retrieve, skipped --" + r.text + "\n")
            continue

        # converts API output to XML Element Tree
        xml = ET.fromstring(r.text) 

        # find public_access_model field and store in variable
        public_access_model = xml.find('public_access_model')

        # find material type and store in variable
        material_type = xml.find('material_type')

        # skip if not found, check for errors, log if needed
        if public_access_model.text != None:
            with open('log.txt', 'a', encoding="utf-8") as log:
                log.write(portfolio_id + " already has a public access level, skipped" + "\n")
            continue   

        # modify public_access_model field, edit the code to the public access model you want to change the portfolios to
        public_access_model.text = access_model_code
        
        # api errors out if material type is not all caps, this sets it to that if it isn't already
        if material_type.text == "Book": material_type.text = "BOOK"

        # converts API output back to string
        xml_final = ET.tostring(xml, encoding="utf-8", method="xml")   
        
        # defines headers for PUT API call
        headers = {'Content-Type': 'application/xml'} 

        # update portfolio
        r = requests.put(f'https://api-na.hosted.exlibrisgroup.com/almaws/v1/electronic/e-collections/{collection_id}/e-services/{service_id}/portfolios/{portfolio_id}?apikey={apikey}', data=xml_final, headers=headers)
        
        if r.status_code != 200:
            with open('log.txt', 'a', encoding="utf-8") as log:
                log.write(portfolio_id + " was not updated, skipped --" + r.text + "\n")

        if r.status_code == 200:
            with open('log.txt', 'a', encoding="utf-8") as log:
                log.write(portfolio_id + " was successfully updated, --" + r.text + "\n")

        # write original xml to backup file
        with open('backup.txt', 'ab') as backup:
            backup.write(str(xml_final).encode("ascii") + b"\n--------------------------------------------------------------------------------------------------------------------\n\n")

        # provides real-time feedback in command line while script is running
        print (portfolio_id + ' SUCCESS!')
        print("--------------------------------------------------------------")