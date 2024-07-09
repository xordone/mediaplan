from parser import Parser


events = Parser()

filter_list= [
    'Концертный зал',
    'Дягилев',
]
for i in events.get_event(filter_list):
    print(i[1])