# importing modules
import requests
import csv
import os
import time

# Url of Random Data API
url = "https://random-data-api.com/api/v2/users?size=2&is_xml=true"

# Requesting data from API
headers = {}
response = requests.request("GET", url, headers=headers, data={})

myjson = response.json() # Storing data in myjson variable
mydata = []             # Initializing a empty list
 
# Initializing header for CSV file
csvheader = ['ID', 'First Name', 'Last Name', 'Username','Email', 'Avatar', 'Gender', 'DOB', 'City', 'Street', 'State']

# Iterating in myjson and Adding necessary data fields in mydata list
for x in myjson[0:1]:

    list = [x['id'], x['first_name'], x['last_name'], x['username'], x['email'], x['avatar'], x['gender'],
            x['date_of_birth'], x['address']['city'], x['address']['street_address'], x['address']['state']]

    mydata.append(list)

# Creating a users.csv file and Appending data of mydata list in users.csv file
with open('users.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    if (os.stat('users.csv').st_size == 0):
        writer.writerow(csvheader)
        
    writer.writerows(mydata)

print("Data Added! Retry after 1 min")

# Sleep function for 1min time intervel
time.sleep(60)

