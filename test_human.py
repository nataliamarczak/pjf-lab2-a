import unittest
from solution import Human

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.human_a = Human('Human', 'Worker', 1980)
        self.human_b = Human('Other Human', 'Soldier', 1980)
        self.human_c = Human('Other Human', 'Python Developer', 2001)

    def test_initialization(self):
        self.assertEqual(self.human_a.get_occupation(), 'Worker')
        self.assertEqual(self.human_a.get_birth_year(), 1980)

    def test_decrease_health(self):
        self.human_a.decrease_health(10)
        self.assertEqual(self.human_a.get_health(), 90)

    def test_is_alive(self):
        self.human_a.decrease_health(100)
        self.assertFalse(self.human_a.is_alive())

    def test_get_health_percent(self):
        self.human_a.decrease_health(50)
        self.assertEqual(self.human_a.get_health_percent(), 50.0)

    def test_attack_bat_a(self):
        initial_health = self.human_b.get_health()
        expected_health = initial_health - 10
        self.human_a.attack(self.human_b)
        self.assertEqual(self.human_b.get_health(), expected_health)

    def test_attack_human_b(self):
        initial_health = self.human_c.get_health()
        expected_health = initial_health - 100
        self.human_b.attack(self.human_c)
        self.assertEqual(self.human_c.get_health(), expected_health)

    def test_attack_human_c(self):
        initial_health = self.human_b.get_health()
        expected_health = initial_health - 5
        self.human_c.attack(self.human_b)
        self.assertEqual(self.human_b.get_health(), expected_health)

if __name__ == '__main__':
    unittest.main()