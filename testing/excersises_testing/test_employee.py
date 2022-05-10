import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов."""

        self.first_name = 'Yauheni'
        self.last_name = 'Filipchanka'
        self.salary = 1600

    def test_give_default_raise(self):
        """Проверяет, что обычный ответ сохранен правильно."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)



unittest.main()