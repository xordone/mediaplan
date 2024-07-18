import gspread


class Spreadsheet:
    def __init__(self, sheet_name='Медиаплан КЦК', page_name='План июль 2024 новый'):
        gc = gspread.service_account(filename='./secrets/cred.json')
#        self.sheet = gc.open(sheet_name).worksheet(page_name)
        sheeturl = 'https://docs.google.com/spreadsheets/d/1mtHQcGAS9mQW_l2EY5j0Iu38kUvkrSUUGGGIEPzl_Zc/edit?gid=1203960731#gid=1203960731'
        self.sheet = gc.open_by_url(sheeturl).worksheet(page_name)

    def get_all(self):
        return self.sheet.get_all_values()
