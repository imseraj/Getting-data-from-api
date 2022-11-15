# importing pandas package
import pandas as pd 

# Taking input of Id
try:
 inputId = int(input('Enter an id in INTEGER\n'))

except :
    print("Exception occoured! please input a vild user ID in Integer")
    exit()

# Reading csv file
csvData=pd.read_csv('users-sorted.csv')

# Finding & Displaying the matching data 
reqFrame= csvData[csvData.ID == inputId ]

if len(reqFrame)==0:
  print(f"NO any user found of this {inputId} user ID") 
else:  
 print(reqFrame)
 print("Here is your USER")