
# Storing, Sorting & Displying API Data

I am creating this repository for an Assignment.In this repository I creates three PYTHON files for Getting random data of an user and write it in a CSV File, A program for sorting a CSV file and A program for Displying a data of a user. 



## Files

  ## 1. getData.py

   This program file GET a random user data from an open source mock rest
   api and store this data in a users.csv file. The users.csv file creates on frist time of running this program after that you can run this program for appending another user data in same users.csv file. The time interveal between adding 2 datas are 1minute.

## output

```
Data Added! Retry after 1 min
```
After successfully running this output generated

## Files

  ## 1. getData.py

   This program file GET a random user data from an open source mock rest
   api and store this data in a users.csv file. The users.csv file creates on frist time of running this program after that you can run this program for appending another user data in same users.csv file. The time interveal between adding 2 datas are 1minute.

## 2. sorting.py
   
   This is the second programe for sorting the users.csv file and create a new users-sorted.csv file.
   This programe sorts users.csv file on the base of FRIST NAME and also displays the output in terminal.

## output

```
Before sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona

[4 rows x 11 columns]

After sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado

[4 rows x 11 columns]
Sorting Done
```
After successfully running this output generated
## 3. display.py

  this is the third porgram for displaying hole data of a user by inputing there user ID. It takes a ID as an input and displays the data on terminal and also i am handling some error. 
## output

```
Before sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona

[4 rows x 11 columns]

After sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado

[4 rows x 11 columns]
Sorting Done
```
After successfully running this output generated
## output

```
Before sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona

[4 rows x 11 columns]

After sorting:
     ID First Name Last Name          Username  ...         DOB                City               Street           State
3  5085       Alia  Lubowitz     alia.lubowitz  ...  1976-05-29        South Rashad    6607 Kiana Greens         Arizona
2  7809     Krissy    Graham     krissy.graham  ...  1969-10-13           Haagburgh  5861 Nienow Mission  South Carolina
0   750     Roscoe  Schmeler   roscoe.schmeler  ...  2003-07-03            Kubshire    97886 Suzi Course      California
1  7709    Sharice  McKenzie  sharice.mckenzie  ...  1965-08-17  West Lakeshiamouth   6025 Wisoky Ridges        Colorado

[4 rows x 11 columns]
Sorting Done
```
After successfully running this output generated
## output

```
Enter a id in INTEGER
5085
     ID First Name Last Name       Username                    Email  ...       Gender         DOB          City             Street    State
0  5085       Alia  Lubowitz  alia.lubowitz  alia.lubowitz@email.com  ...  Genderfluid  1976-05-29  South Rashad  6607 Kiana Greens  Arizona

[1 rows x 11 columns]
Here is your USER
```
After successfully running this output generated


- I am providing users.csv and users-sorted.csv as example. You can delete these file but make sure to run these program in order of 1,2 and 3. 