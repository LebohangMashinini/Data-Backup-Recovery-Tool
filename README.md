# Data Backup & Recovery Tool

A Python tool to **backup, restore, and preview** a SQLite database. Integrates with **MinIO** for virtual storage, simulating cloud backups.

---

## Features

- Preview the first 10 rows of your database  
- Backup database locally with timestamped files  
- Upload backups to MinIO (S3-compatible object storage)  
- Restore database from a specific backup  
- CLI interface for easy usage  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/LebohangMashinini/Data-Backup-Recovery-Tool.git
cd Data-Backup-Recovery-Tool
Create a virtual environment:

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Create database and table:

bash
Copy code
python sqlite_db.py
Seed fake data:

bash
Copy code
python seed_data.py
Preview database:

bash
Copy code
python main.py preview
Backup database:

bash
Copy code
python main.py backup
Restore database:

bash
Copy code
python main.py restore --file backups/backup_YYYYMMDD_HHMMSS.db
Folder Structure
bash
Copy code
data-backup-tool/
│
├── main.py                # CLI interface
├── sqlite_db.py           # Database & table creation
├── seed_data.py           # Insert fake data
├── backup/
│   ├── backup_manager.py  # Backup & upload functions
│   ├── restore_manager.py # Restore functions
├── backups/               # Stores backup files
└── data.db                # SQLite database file
Notes
Each backup file is timestamped for easy tracking

MinIO bucket is created automatically if it does not exist

CLI actions: preview, backup, restore
