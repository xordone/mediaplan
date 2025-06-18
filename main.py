from parser import Parser
import cal
import func

cal = cal.Calendar()
# cal.event_delete_all()
events_from_cal = cal.event_list_month().get('items')
for i in func.list:
    events = Parser(i)  

    filter_list = [
        'Концертный зал',
        'Дягилев',
        'Площадь КЦ',
        'Милонга',
    ]
    for i in events.get_event_from_filter(filter_list, description_flag=True):
        for j in events_from_cal:
            if 'summary' not in j:
                break
            if i['summary'] == j['summary'] and i['start']['dateTime'] == j['start']['dateTime']:
                cal.event_update(j['id'], i)
                break
        else:
            cal.event_insert(i)
        
            
        # cal.event_insert(i)

