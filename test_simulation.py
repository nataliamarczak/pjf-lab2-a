import unittest

from solution import Team, Bat, Human, Vampire, Simulation


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.human_a = Human('Human', 'Worker', 1980)
        self.human_b = Human('Other Human', 'Soldier', 1980)
        self.human_c = Human('Other Human', 'Soldier', 2001)
        self.bat_a = Bat('Bat A', 5, 5)
        self.bat_b = Bat('Bat B', 10, 5)
        self.bat_c = Bat('Bat C', 10, 10)
        self.vampire_a = Vampire('Vampire A', 'Worker', 10, 20)
        self.vampire_b = Vampire('Vampire B', 'Soldier', 5, 10)
        self.vampire_c = Vampire('Vampire C', 'Soldier', 5, 10)

        self.team1 = Team()
        self.team2 = Team()
        self.team1.add(self.vampire_a)
        self.team1.add(self.vampire_b)
        self.team2.add(self.vampire_c)
        self.team1.add(self.human_a)
        self.team2.add(self.human_b)
        self.team2.add(self.human_c)
        self.team1.add(self.bat_a)
        self.team1.add(self.bat_b)
        self.team1.add(self.bat_c)

        self.simulation = Simulation(self.team1, self.team2)

    def test_execute_round(self):
        self.simulation.execute_round()
        self.assertTrue(any(creature.get_health() < creature.get_max_health() for creature in self.team2.get_alive_members()))

    def test_has_ended(self):
        self.assertFalse(self.simulation.has_ended())
        for creature in self.team2.get_alive_members():
            creature.decrease_health(creature.get_max_health())
        self.assertTrue(self.simulation.has_ended())
        self.assertTrue(self.simulation.get_winner() == self.team1)

    def test_execute(self):
        self.simulation.execute()
        self.assertTrue(self.simulation.has_ended())

    def test_no_public_attributes_in_classes(self):
        for instance in [self.human_a, self.bat_a, self.vampire_a, self.team1, self.simulation]:
            attributes_and_methods = [attr for attr in dir(instance) if not attr.startswith('__')]
            non_methods = [attr for attr in attributes_and_methods if not callable(getattr(instance, attr))]
            self.assertTrue(all(attr.startswith('_') for attr in non_methods))
            

if __name__ == '__main__':
    unittest.main()