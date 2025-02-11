import gspread


class Spreadsheet:
    def __init__(self, page_name='План июль 2024 новый'):
        gc = gspread.service_account(filename='./secrets/cred.json')
#        self.sheet = gc.open(sheet_name).worksheet(page_name)
#        sheeturl = 'https://docs.google.com/spreadsheets/d/1mtHQcGAS9mQW_l2EY5j0Iu38kUvkrSUUGGGIEPzl_Zc/edit?gid=1203960731#gid=1203960731'
        sheeturl = 'https://docs.google.com/spreadsheets/d/1dmHYL0z5P8ky0n4oS_s365LbELy-Y4qRvkR4WeaoHWA/edit?gid=1285510395#gid=1285510395'
        
        self.sheet = gc.open_by_url(sheeturl).worksheet(page_name)

    def get_all(self):
        return self.sheet.get_all_values()
