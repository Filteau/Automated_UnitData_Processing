import filehandler as fh
import db_run as dbr
import time

def main():
    fh.check_path(fh.path_to_TBC, ".db")
    fh.check_path("Data_Processing_Script/", ".bat")
    fh.move_file_by_type(fh.path_to_TBC, fh.path_to_data, ".db")
    time.sleep(2)
    dbr.run_db_recovery()
    
    
    
if __name__ == "__main__":
    main()