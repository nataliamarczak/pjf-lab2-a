import unittest
from solution import Bat

class TestBat(unittest.TestCase):
    def setUp(self):
        self.bat_a = Bat('Bat A', 5, 5)
        self.bat_b = Bat('Bat B', 10, 5)
        self.bat_c = Bat('Bat C', 10, 10)

    def test_initialization(self):
        self.assertEqual(self.bat_a.get_health(), 40)
        self.assertEqual(self.bat_a.get_max_health(), 40)
        self.assertEqual(self.bat_a.get_wing_span(), 5)
        self.assertEqual(self.bat_a.get_fly_speed(), 5)

    def test_change_flight_speed(self):
        self.bat_a.change_flight_speed(15)
        self.assertEqual(self.bat_a.get_fly_speed(), 15)

    def test_decrease_health(self):
        self.bat_a.decrease_health(10)
        self.assertEqual(self.bat_a.get_health(), 30)

    def test_is_alive(self):
        self.bat_a.decrease_health(40)
        self.assertFalse(self.bat_a.is_alive())

    def test_get_health_percent(self):
        self.bat_a.decrease_health(20)
        self.assertEqual(self.bat_a.get_health_percent(), 50.0)

    def test_attack_bat_a(self):
        initial_health = self.bat_b.get_health()
        expected_health = initial_health - 5
        self.bat_a.attack(self.bat_b)
        self.assertEqual(self.bat_b.get_health(), expected_health)

    def test_attack_bat_b(self):
        initial_health = self.bat_b.get_health()
        expected_health = initial_health - 10
        self.bat_b.attack(self.bat_b)
        self.assertEqual(self.bat_b.get_health(), expected_health)

    def test_attack_bat_c(self):
        initial_health = self.bat_b.get_health()
        expected_health = initial_health - 15
        self.bat_c.attack(self.bat_b)
        self.assertEqual(self.bat_b.get_health(), expected_health)



if __name__ == '__main__':
    unittest.main()