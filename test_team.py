import unittest

from solution import Team, Bat, Human, Vampire


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team()
        self.bat = Bat("Bat", 5, 10)
        self.human = Human("Human", "Soldier", 2000)
        self.vampire = Vampire("Vampire", "Unemployed", 6, 15)

    def test_add(self):
        self.team.add(self.bat)
        self.assertIn(self.bat, self.team._creatures)

    def test_get_alive_members(self):
        self.team.add(self.bat)
        self.team.add(self.human)
        self.human.decrease_health(100)
        self.assertEqual(self.team.get_alive_members(), [self.bat])

    def test_get_defender(self):
        self.team.add(self.bat)
        self.team.add(self.human)
        self.assertEqual(self.team.get_defender(), self.bat)

    def test_is_at_least_one_alive_member(self):
        self.assertFalse(self.team.is_at_least_one_alive_member())
        self.team.add(self.bat)
        self.assertTrue(self.team.is_at_least_one_alive_member())

    def test_attack(self):
        team2 = Team()
        team2.add(self.vampire)
        self.team.add(self.bat)
        self.team.attack(team2)
        self.assertLess(self.vampire.get_health(), 300)

if __name__ == '__main__':
    unittest.main()