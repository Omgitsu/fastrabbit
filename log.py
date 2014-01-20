import os
import gspread

def log_job(values):
	key = os.environ['GDRIVE_SPREADSHEET']
	email = os.environ['GDRIVE_EMAIL']
	password = os.environ['GDRIVE_PASSWORD']
	gc = gspread.login(email, password)
	sh = gc.open_by_key(key)
	worksheet = sh.worksheet("log")
	worksheet.append_row(values)
