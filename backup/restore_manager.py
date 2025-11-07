import shutil

def restore_database(backup_file, db_path):
    shutil.copy(backup_file, db_path)
    print(f"Database restored from {backup_file}")
