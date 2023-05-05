# Tutorial Report - PostgreSQL Python: Inserting Data Into a Table
This tutorial report aims to create a table and insert data in PostgreSQL using Python.

## Installing PostgreSQL
Download PostgreSQL in your respective OS using [this link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and follow the installation wizard.  

Note: we do not need to install Stack Builder. Ensure that you remember your password, use port 5432, and use the default locale.  

Next, verify the installation by launching SQL Shell (psql). Enter the necessary information (accept the default by pressing enter), and provide the password you entered during installation.
Type in:  

```SELECT version();```  

and you should see a line containing information with your version number.

## Creating a Database
Before running our Python files, we must create a database called "TestDB" in psql. Run the following command in psql:  
```CREATE DATABASE "TestDB";```  
Next, switch into our newly created databse by typing:  
```\c "TestDB"```  

## Running our Python Files
First, ensure that you have entered your password into the password_str global variable at the top of each python file.  
Next, open a terminal/cmd window and switch to the directory containing the 2 python files.  
Finally, run create_table.py by typing in ```python create_table.py``` and then run insert_data.py by typing ```python insert_data.py```.

## Verifying Table Creation
After running create_table.py, enter the following into psql:  
```\dt```  
NOTE: ensure that you are in the correct database.

## Verifying Data Insertion
After running insert_data.py, enter the following into psql:  
```SELECT * FROM vendors;```  

## create_table.py
The create_tables function takes a tuple of strings called command, and is executed using the cursor.execute(command) in a for loop (since we have multiple commands).  
Note that the cursor object is created after establishing our connection with the database, and then closed before committing the changes.

## insert_data.py
Here, the insert_vendor_list function only has 1 SQL statement, but takes in a list of strings.  
To execute our statement, we use cursor.executemany() to add multiple rows into the table.