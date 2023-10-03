from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import datetime as dt
from time import sleep


x = dt.date.today()
y = str(x)
dia = y[-2]+y[-1]
mes = y[-5]+y[-4]

def hora():
    hora = dt.datetime.now().time()
    hora = str(hora)
    hora= list(hora)
    hora = hora[0]+hora[1]+hora[2]+hora[3]+hora[4]+hora[5]+hora[6]
    return hora

tokenn = '6373023491:AAFEpbXAjIQ9fHJczjegtxy1PrF6Q6p8s0M'
#chat_id = '6314962487' my id
chat_id = '-4028430982'


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
dici_mes = {'01':'A','02':'B','03':'C','04':'D','05':'E','06':'F','07':'G','08':'H','09':'I','10':'J','11':'K','12':'L'}
mes = dici_mes[mes]
SAMPLE_SPREADSHEET_ID = '1zgAX3q87JRIqAkPON6bK2tCYVHgRkCEfY98W0ANxa6Q'
SAMPLE_RANGE_NAME = f'niver!{mes+dia}'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        values =values[0]
        values =values[0]
        print(values)
        mensagem = values
        url = f'https://api.telegram.org/bot{tokenn}/sendmessage?chat_id={chat_id}&text={mensagem}'
        requests.get(url)
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    while True:
        hour = hora()
        if hour == '06:00:0':
            main()
            sleep(9.5)
            
# [END sheets_quickstart]