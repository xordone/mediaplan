import gspread
class Spreadsheet:
    def __init__(self, sheet_name='Медиаплан КЦК', page_name='План июль 2024 новый'):
        gc = gspread.service_account(filename='./secrets/cred.json')
        self.sheet = gc.open(sheet_name).worksheet(page_name)
    
    def get_all(self):
        return self.sheet.get_all_values()