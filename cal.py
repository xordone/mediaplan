from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

class Calendar:
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    FILE_PATH = './secrets/cred.json'
    CALENDAR_ID = '56fff3d8835af0be855c3684c52d57f4a7ca71fb070f3f82ccc7b26a1dec18c4@group.calendar.google.com'
    now = datetime.utcnow()

    time_today = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
    time_month = now.replace(day=1,hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
    time_max = (now + timedelta(days=62)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
    time_min = (now + timedelta(days=-18000)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'


    def __init__(self) -> None:
        credentials = service_account.Credentials.from_service_account_file(self.FILE_PATH, scopes=self.SCOPES)
        self.service = build('calendar', 'v3', credentials=credentials)
    
    def calendar_list(self):
        return self.service.calendarList().list(showHidden=True).execute()
    
    def calendar_create(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }
        created_calendar_list_entry = self.service.calendarList().insert(
            body=calendar_list_entry).execute() 
    def event_list(self, timeMin=time_today, timeMax=time_max):
        return self.service.events().list(
            calendarId=self.CALENDAR_ID,
            maxResults=10000,
            timeMin=timeMin,
            timeMax=timeMax,
            ).execute()
    def event_list_month(self):
        return self.event_list(timeMin=self.time_month, timeMax=self.time_max)

    def event_insert(self, event):
        date, time = event['start']['dateTime'][:-9].split('T')
        print('add event:\n {0} {1} - {2}'.format(date, time, event['summary']))
        return self.service.events().insert(calendarId=self.CALENDAR_ID, body=event).execute()
    
    def event_delete(self, event_id):
        return self.service.events().delete(calendarId=self.CALENDAR_ID, eventId=event_id).execute()


    def event_delete_all(self):
        events = self.event_list(timeMin=self.time_min)
        for event in events['items']:
            print('delete event: {0}'.format(event['id']))
            self.event_delete(event['id'])
        return True
    
    def event_delete_all_from_now(self):
        events = self.event_list()
        for event in events['items']:
            print('delete event: {0}'.format(event['id']))
            self.event_delete(event['id'])
        return True
    
    
    
    
    def event_update(self, event_id, event):
        print('update {0} event:\n {1}'.format(event_id, event['summary']))
        return self.service.events().update(calendarId=self.CALENDAR_ID, eventId=event_id, body=event).execute()
