import subprocess
import os

def run_db_recovery():
    # Path to the DBRecovery.bat file
    dbr_path = r"c:/Users/Reece Filteau/Desktop/Automation/Data_Processing_Script/DBRecovery.bat"
    sql_path = r"c:/Users/Reece Filteau/Desktop/Automation/Data_Processing_Script/sqlite3.exe"
    
    working_directory = r"C:/Users/Reece Filteau/Desktop/Automation/Data_Processing_Script"
    
    #This uses the os.system() method which is
    # a simple way to run a command in the command prompt.
    try:
        subprocess.call(dbr_path, shell=True, cwd=working_directory)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    run_db_recovery()