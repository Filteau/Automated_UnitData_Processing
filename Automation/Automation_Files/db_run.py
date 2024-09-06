import subprocess
import os

def run_db_recovery():
    # Path to the DBRecovery.bat file
    dbr_path = r"insert/complete/path/here"
    sql_path = r"insert/complete/path/here"

    # change the below to your path to Data_Processing_Script
    working_directory = r"Automation/Data_Processing_Script"
    
    #This uses the os.system() method which is
    # a simple way to run a command in the command prompt.
    try:
        subprocess.call(dbr_path, shell=True, cwd=working_directory)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    run_db_recovery()
