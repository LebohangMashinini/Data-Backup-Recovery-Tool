import shutil
from datetime import datetime
import os

def backup_database(db_path, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.db")
    shutil.copy(db_path, backup_file)
    print(f"Backup created: {backup_file}")
    return backup_file

def upload_to_minio(file_path, bucket_name, client):
    file_name = os.path.basename(file_path)

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    client.fput_object(bucket_name, file_name, file_path)
    print(f"Uploaded {file_name} to bucket '{bucket_name}'")
