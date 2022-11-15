# importing pandas package
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv("users.csv")

# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)

# sort data frame by first name
csvData.sort_values(["First Name"],axis=0,ascending=[True],inplace=True)

# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)

# Creating new CSV file of sorted data
csvData.to_csv('users-sorted.csv', index=False)
print('Sorting Done')
