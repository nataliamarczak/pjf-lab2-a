import unittest
from solution import Vampire, Human

class TestVampire(unittest.TestCase):
    def setUp(self):
        self.vampire_a = Vampire('Vampire A', 'Worker', 10, 20)
        self.vampire_b = Vampire('Vampire B', 'Soldier', 5, 10)
        self.vampire_c = Vampire('Vampire C', 'Soldier', 5, 10)

    def test_initialization(self):
        self.assertEqual(self.vampire_a.get_health(), 300)
        self.assertEqual(self.vampire_a.get_birth_year(), 1900)

    def test_decrease_health(self):
        self.vampire_a.decrease_health(10)
        self.assertEqual(self.vampire_a.get_health(), 290)

    def test_is_alive(self):
        self.vampire_a.decrease_health(350)
        self.assertFalse(self.vampire_a.is_alive())

    def test_get_health_percent(self):
        self.vampire_a.decrease_health(150)
        self.assertEqual(self.vampire_a.get_health_percent(), 50.0)

    def test_attack(self):
        initial_health = self.vampire_b.get_health()
        self.vampire_a.attack(self.vampire_b)
        self.assertTrue(self.vampire_b.get_health() < initial_health)

    def test_attack_max_health(self):
        initial_health = self.vampire_b.get_health()
        expected_health = initial_health - 15  # Assuming attack decreases health by 20
        self.vampire_a.attack(self.vampire_b)
        self.assertEqual(self.vampire_b.get_health(), expected_health)

    def test_attack_min_health(self):
        self.vampire_b.decrease_health(290)  # Decrease health to 10
        initial_health = self.vampire_b.get_health()
        expected_health = 0  # Health should not go below 0
        self.vampire_a.attack(self.vampire_b)
        self.assertEqual(self.vampire_b.get_health(), expected_health)

    def test_attack_other_vampire(self):
        initial_health = self.vampire_c.get_health()
        expected_health = initial_health - 15  # Assuming attack decreases health by 15
        self.vampire_b.attack(self.vampire_c)
        self.assertEqual(self.vampire_c.get_health(), expected_health)

    def test_attack_human_with_less_than_50_health(self):
        human = Human('Human', 'Worker', 1900)
        human.decrease_health(60)
        self.vampire_a.decrease_health(91)
        self.vampire_a.decrease_health(50)
        initial_health = self.vampire_a.get_health()
        expected_health = initial_health + 10
        self.vampire_a.attack(human)
        self.assertEqual(self.vampire_a.get_health(), expected_health)

    def test_attack_human_with_more_than_50_health(self):
        human = Human('Human', 'Worker', 1980)
        self.vampire_a.decrease_health(91)
        initial_health = self.vampire_a.get_health()
        expected_health = initial_health
        self.vampire_a.attack(human)
        self.assertEqual(self.vampire_a.get_health(), expected_health)

if __name__ == '__main__':
    unittest.main()