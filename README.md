# DS3Backup
A backup tool for Dark Souls 3 save data.

# Instalation
1. Install Python (https://www.python.org)
2. Download the win32ui module with the following command: `pip install pypiwin32`
3. Fill out the variables in `DS3BackupConfig.py.EXAMPLE` and rename it to `DS3BackupConfig.py`
4. Run the backup tool by double-clicking `DS3Backup.py`, or via command prompt: `python DS3Backup.py`

# Information
This tool will automatically launch Dark Souls 3 when run, and will automatically exit when it detects that the game has closed.
Save files can be restored by copying a backup to your DS3 save location and renaming it to `DS30000.sl2`
