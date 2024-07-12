from google.oauth2 import service_account
from googleapiclient.discovery import build
class Calendar:
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    FILE_PATH = './secrets/cred.json'
    CALENDAR_ID = '56fff3d8835af0be855c3684c52d57f4a7ca71fb070f3f82ccc7b26a1dec18c4@group.calendar.google.com'

    def __init__(self) -> None:
        credentials = service_account.Credentials.from_service_account_file(self.FILE_PATH, scopes=self.SCOPES)
        self.service = build('calendar', 'v3', credentials=credentials)
    
    def get_calendar_list(self):
        return self.service.calendarList().list().execute()
    
    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        created_calendar_list_entry = self.service.calendarList().insert(
            body=calendar_list_entry).execute() 
    def list_events(self):
        return self.service.events().list(calendarId=self.CALENDAR_ID).execute()
    def insert_event(self, event):
        date, time = event['start']['dateTime'][:-9].split('T')
        print('add event:\n {0} {1} - {2}'.format(date, time, event['summary']))
        return self.service.events().insert(calendarId=self.CALENDAR_ID, body=event).execute()
    
    def delete_event(self, event_id):
        return self.service.events().delete(calendarId=self.CALENDAR_ID, eventId=event_id).execute()
    
    def delete_all_events(self):
        events = self.list_events()
        for event in events['items']:
            self.delete_event(event['id'])
        