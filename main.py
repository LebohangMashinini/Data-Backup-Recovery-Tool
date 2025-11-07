import sqlite3
import argparse
from backup.backup_manager import backup_database, upload_to_minio
from backup.restore_manager import restore_database
from minio import Minio

# MinIO setup
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

db_path = "data.db"
backup_dir = "backups"
bucket_name = "database-backups"

# CLI setup
parser = argparse.ArgumentParser(description="Database Backup & Restore Tool")
parser.add_argument("action", choices=["backup", "restore", "preview"], help="Action to perform")
parser.add_argument("--file", help="Backup file name to restore (required for restore)")

args = parser.parse_args()

if args.action == "preview":
    # Preview first 10 rows
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users LIMIT 10")
    for row in cur.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, DOB: {row[2]}, Email: {row[3]}, City: {row[4]}")
    conn.close()

elif args.action == "backup":
    # Backup and upload
    backup_file = backup_database(db_path, backup_dir)
    upload_to_minio(backup_file, bucket_name, client)

elif args.action == "restore":
    if not args.file:
        print("Error: --file argument is required for restore")
    else:
        restore_database(args.file, db_path)
