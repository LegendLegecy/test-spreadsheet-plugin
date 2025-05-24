import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the credentials and client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open your spreadsheet and select the first worksheet
sheet = client.open('YOUR_SPREADSHEET_NAME').sheet1

# Read value from B2
b2_value = sheet.acell('B2').value

# Write "Yes" or "NO" in F2
if b2_value:
    sheet.update('F2', 'Yes')
else:
    sheet.update('F2', 'NO')