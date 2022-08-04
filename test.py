import unittest

from calc_figure_area import calc_figure_area


class TestCalcArea(unittest.TestCase):
    """Тестируем calc_figure_area"""

    def test_calc(self):
        """Тест на правильность ответа."""
        data = [(0, 0), (1, 1), (2, 2), (3, 1), (4, 2), (5, 3), (6, 4), (7, 2)]
        self.assertEqual(
            calc_figure_area(data),
            14,
            'Функция возвращает некорректное значение'
        )

    def test_incorrect_coordinate_points(self):
        data = [(1, 0)]
        self.assertRaises(ValueError, calc_figure_area, data)

    def test_tuple_isnt_couple_values(self):
        data = [(1, 0), (2, 3), (3, 2, 5)]
        self.assertRaises(ValueError, calc_figure_area, data)


if __name__ == '__main__':
    unittest.main()
