import datetime
import pytz
from spreadsheet import Spreadsheet
from cal import Calendar

class Parser:
    filter_by_name = [
        'Я.М. Котова',
        'Е.М. Мандрина',
        'А.В. Старцов',
        'Ю.Д. Козлова',
        'И.Л. Корочкова',
    ]
    filter_by_type = [
        'концертная программа',
    ]
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
    def __init__(self, month):
        month_dict = {
            '01' : 'январь',
            '02' : 'февраль',
            '03' : 'март',
            '04' : 'апрель',
            '05' : 'май',
            '06' : 'июнь',
            '07' : 'июль',
            '08' : 'август',
            '09' : 'сентябрь',
            '10' : 'октябрь',
            '11' : 'ноябрь',
            '12' : 'декабрь',
        }
        if int(month) < 12:
            page = 'План ' + month_dict[month] + ' 2025'
        else:
            page = 'План ' + month_dict[month] + ' 2024'
        self.sheet = Spreadsheet(page_name=page)
        self.all_values = self.sheet.get_all()
    
    # def get_event_from_filter(self, location='Концертный зал', 
    #             description_flag=False,
    #             link_flag=False,
    #             type_flag=False):
    #     ret = []
    #     for i in self.all_values:
    #         if i[7] in location:
    #             res =({'date'      : i[2],
    #                 'time'      : i[4],
    #                 'name'      : i[5],
    #                 'location'  : i[7],
    #                 'format'    : i[8]})
    #             if type_flag:
    #                 res['type'] = i[10]
    #             if description_flag:
    #                 res['description'] = i[12]
    #             if link_flag:
    #                 res['link'] = i[13]
    #             ret.append(res)
    #     return ret
#     event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2015-05-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2015-05-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=2'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }

    def dater(self, date, time):
        if time[-1] == '\n':
            time = time[:-1]
        if time[1].isdigit() == False:
            time = '00:00 - 00:00'
        if len(time) > 16:
            time = '00:00 - 00:00'

        start = '{0} {1}'.format(date, time[:5])
        end = '{0} {1}'.format(date, time[-5:])
        time_zone = pytz.timezone("Europe/Moscow")
        date_start = time_zone.localize(datetime.datetime.strptime(start, "%d.%m.%Y %H:%M"))
        date_end = time_zone.localize(datetime.datetime.strptime(end, "%d.%m.%Y %H:%M"))
        
        return {'start': date_start, 'end': date_end}

    def get_event_from_filter(self, location='Концертный зал', 
                description_flag=False,
                link_flag=False,
                type_flag=False):

        ret = []
        for i in self.all_values:
            if i[7] in location and i[6] in self.filter_by_name:
                if len(i[2]) > 10:
                    continue
                res =({
                    #'date'      : i[2],
                    #'time'      : i[4],
                    'summary'      : i[5],
                    'location'  : i[7],
                    #'format'    : i[8]
                    })
                if type_flag:
                    res['type'] = i[10]
                if description_flag:
                    res['description'] = i[12]
                if link_flag:
                    res['link'] = i[13]
                if len(i[4]) < 1:
                    event_date = self.dater(i[2], '00:00-00:00')
                else:
                    event_date = self.dater(i[2], i[4])

                res['start'] = {
                    'dateTime': event_date['start'].isoformat(),
                }
                res['end'] = {
                    'dateTime': event_date['end'].isoformat(),
                }
                ret.append(res)
        return ret
    
