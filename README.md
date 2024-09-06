# Automated_UnitData_Processing
This program's purpose is to automation the functionality of the processing API. It is created on top of the pre-existing processing API. 

# SETUP
The processing API is not included with this program. In order to get this working, you must create a parent folder named 'Automation', move the API folder into the parent folder you just created. Then, on the same level, add the Automation_Files. Change the name of the API folder to "Data_Processing_Script". 

For the current version (as of 9/6/24), there is no config file. So, you must go into 'db_run.py' and adjust the variables 'dbr_path' and 'sql_path' to the actual path of the recovery tool and SQLite files in the API, on your local system. 

# HOW TO USE
Run from 'main.py', that's it for now. 
