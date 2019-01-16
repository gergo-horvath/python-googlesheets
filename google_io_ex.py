# open and write google sheets files

import httplib2
import os

from apiclient import discovery
from google.oauth2 import service_account

try:
    # where to look for spreadsheet
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file",
              "https://www.googleapis.com/auth/spreadsheets"]

    # path to credentials file
    secret_file = os.path.join(os.getcwd(), "creds.json")

    # get credentials from .json file
    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    service = discovery.build("sheets", "v4", credentials=credentials)

    # path of spreadsheet and worksheet
    spreadsheet_id = ''
    # spreadsheet_id is what comes after https://docs.google.com/spreadsheets/d/ in the address bar
    range_name = ''  # worksheet you want to edit selected as range

    # writing new values - letters and number (a1) are the position of the equivalent cell  
    values = [
        ["a1", "b1", "c1", "d1", "e1"],
        ["a2", "b2", "c2", "d2", "e2"]

    ]

    data = {
        "values": values
    }

    service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data,
                                           range=range_name, valueInputOption="USER_ENTERED").execute()

except OSError as e:
    print(e)
