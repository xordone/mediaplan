import unittest
import datetime
from dateutil.relativedelta import relativedelta
from func import list  # Импорт списка дат из вашего модуля func

class TestFunc(unittest.TestCase):
    
    def test_list_contents(self):
        """Проверяем, содержит ли список корректные значения."""
        now = datetime.datetime.now()
        month1 = now.strftime("%m")
        month2 = (now + relativedelta(months=+1)).strftime("%m")
        # month3 = (now + relativedelta(months=+2)).strftime("%m")
        
        expected_list = [month1, month2]  # Список ожидаемых значений
        self.assertEqual(list, expected_list, "Список содержит некорректные данные")
    
    def test_list_length(self):
        """Проверяем, содержит ли список корректное количество элементов."""
        self.assertEqual(len(list), 2, "Некорректное количество элементов в списке")

if __name__ == '__main__':
    unittest.main()