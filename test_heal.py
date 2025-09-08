# test_heal.py
import unittest
from solution import Human, Vampire, Bat

class TestVampireHeal(unittest.TestCase):
    def setUp(self):
        self.v = Vampire("Drac", "Count", 6, 7)   # 300 HP
        self.h = Human("Jan", "Worker", 1980)     # 100 HP
        self.b = Bat("Batty", 10, 10)             # 40 HP

    def test_heal_only_vs_human_and_only_when_below_50_after_hit(self):
        # Najpierw brak leczenia (po ciosie Human ma 85% HP)
        self.v.decrease_health(50)                # 250/300
        self.v.attack(self.h)                     # 15 dmg -> 85 HP, brak leczenia
        self.assertEqual(self.v.get_health(), 250)

        # Teraz Human już <50% — po kolejnym ciosie wampir leczy się +10
        self.h.decrease_health(40)                # 45/100
        self.v.attack(self.h)                     # heal +10
        self.assertEqual(self.v.get_health(), 260)

    def test_no_heal_vs_bat_and_capped_at_max(self):
        # Brak leczenia przy ataku na Bat
        self.v.decrease_health(5)                 # 295/300
        self.v.attack(self.b)                     # brak leczenia vs Bat
        self.assertEqual(self.v.get_health(), 295)

        # Leczenie nie przekracza max_health
        low = Human("Low", "Worker", 1980)
        low.decrease_health(60)                   # 40/100 (<50%)
        for _ in range(10):                       # wiele razy poniżej 50%
            self.v.attack(low)                    # potencjalnie > max bez ograniczenia
        self.assertEqual(self.v.get_health(), self.v.get_max_health())

if __name__ == "__main__":
    unittest.main()
