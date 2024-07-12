from parser import Parser
import cal
import datetime
from dateutil.relativedelta import relativedelta


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


month = datetime.datetime.now()
next_month = month + relativedelta(months=+1)
list = [month, next_month]

cal = cal.Calendar()
# удаляем всё события
cal.delete_all_events()

for i in list:
    events = Parser(i.strftime("%m"))

    filter_list= [
        'Концертный зал',
        'Дягилев',
        'Площадь КЦ',
    ]
    for i in events.get_event_from_filter(filter_list, description_flag=True):
        cal.insert_event(i)

