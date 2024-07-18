from parser import Parser
import cal
import func

cal = cal.Calendar()
# удаляем всё события
cal.delete_all_events()

for i in func.list:
    events = Parser(i)  

    filter_list = [
        'Концертный зал',
        'Дягилев',
        'Площадь КЦ',
    ]
    for i in events.get_event_from_filter(filter_list, description_flag=True):
        cal.insert_event(i)

        