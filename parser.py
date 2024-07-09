import datetime
from spreadsheet import Spreadsheet
class Parser:
# struct:
#[0] '№ п/п'
#[1] 'Внесено в ЦЭК',
#[2] 'Дата\n(период)',
#[3] 'День недели',
#[4] 'Время проведения (начало-окончание)',
#[5] 'Наименование мероприятия  ',
#[6] 'Ответственный исполнитель',
#[7] 'Место проведения \n',
#[8] 'Форма мероприятия ',
#[9] 'Охват мероприятия, чел. ',
#[10] 'Форма участия: Платная/\nБесплатная',
#[11] 'Возрастной ценз',
#[12] 'Краткое описание мероприятия',
#[13] 'Ссылка на мероприятие'
    def __init__(self):
        self.sheet = Spreadsheet()
        self.all_values = self.sheet.get_all()
    
    def get_event(self, location='Концертный зал', 
                description_flag=False,
                link_flag=False,
                type_flag=False):
        ret = []
        for i in self.all_values:
            if i[7] in location:
                res =({'date'      : i[2],
                    'time'      : i[4],
                    'name'      : i[5],
                    'location'  : i[7],
                    'format'    : i[8]})
                if type_flag:
                    res['type'] = i[10]
                if description_flag:
                    res['description'] = i[12]
                if link_flag:
                    res['link'] = i[13]
                ret.append(res)
        return ret