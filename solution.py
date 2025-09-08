from __future__ import annotations
from typing import List, Optional


# ========= Core =========
class Creature:
    def __init__(self, name: str, max_health: int) -> None:
        self._name: str = name
        self._max_health: int = int(max_health)
        self._health: int = int(max_health)

    def get_name(self) -> str:
        return self._name

    def decrease_health(self, amount: int) -> None:
        dmg = max(0, int(amount))
        self._health = max(0, self._health - dmg)

    def is_alive(self) -> bool:
        return self._health > 0

    def get_health_percent(self) -> float:
        if self._max_health <= 0:
            return 0.0
        return (self._health / self._max_health) * 100.0

    def get_health(self) -> int:
        return self._health

    def get_max_health(self) -> int:
        return self._max_health

    # interfejs – nadpisują potomkowie
    def attack(self, attacked_creature: "Creature") -> None:
        raise NotImplementedError


# ========= Bat =========
class Bat(Creature):
    def __init__(self, name: str, wing_span: int, flight_speed: int) -> None:
        # jawne wywołanie bazowej (ważne przy wielodziedziczeniu z Vampire)
        Creature.__init__(self, name=name, max_health=40)
        self._wing_span: int = int(wing_span)
        self._flight_speed: int = int(flight_speed)

    def get_fly_speed(self) -> int:
        return self._flight_speed

    def get_wing_span(self) -> int:
        return self._wing_span

    def change_flight_speed(self, speed: int) -> None:
        self._flight_speed = int(speed)

    def attack(self, attacked_creature: Creature) -> None:
        # 5 bazowo +5 jeśli wing_span > 5 +5 jeśli flight_speed > 5
        dmg = 5
        if self._wing_span > 5:
            dmg += 5
        if self._flight_speed > 5:
            dmg += 5
        attacked_creature.decrease_health(dmg)


# ========= Human =========
class Human(Creature):
    def __init__(self, name: str, occupation: str, born_year: int) -> None:
        Creature.__init__(self, name=name, max_health=100)
        self._occupation: str = occupation
        self._born_year: int = int(born_year)

    def get_occupation(self) -> str:
        return self._occupation

    def get_birth_year(self) -> int:
        return self._born_year

    def attack(self, attacked_creature: Creature) -> None:
        # 10 bazowo; Soldier = 100; jeśli urodzony > 2000 to 5
        if self._occupation == "Soldier":
            dmg = 100
        elif self._born_year > 2000:
            dmg = 5
        else:
            dmg = 10
        attacked_creature.decrease_health(dmg)


# ========= Vampire (multiple inheritance) =========
class Vampire(Human, Bat):
    def __init__(self, name: str, occupation: str, wing_span: int, flight_speed: int) -> None:
        # Wszystkie wampiry: born_year = 1900
        Human.__init__(self, name=name, occupation=occupation, born_year=1900)
        Bat.__init__(self, name=name, wing_span=wing_span, flight_speed=flight_speed)
        # Nadpisz parametry HP dla wampira
        self._max_health = 300
        self._health = 300

    def attack(self, attacked_creature: Creature) -> None:
        # Wampir zadaje stałe 15
        attacked_creature.decrease_health(15)

        # Heal +10 TYLKO jeśli atakujemy Human i PO ciosie Human ma < 50% HP
        if isinstance(attacked_creature, Human) and attacked_creature.get_health_percent() < 50.0:
            self._health = min(self._max_health, self._health + 10)


# ========= Team =========
class Team:
    def __init__(self) -> None:
        self._creatures: List[Creature] = []

    def add(self, creature: Creature) -> None:
        self._creatures.append(creature)

    def get_alive_members(self) -> List[Creature]:
        return [c for c in self._creatures if c.is_alive()]

    def get_defender(self) -> Optional[Creature]:
        alive = self.get_alive_members()
        return alive[0] if alive else None

    def is_at_least_one_alive_member(self) -> bool:
        return any(c.is_alive() for c in self._creatures)

    def attack(self, other_team: "Team") -> None:
        if not other_team.is_at_least_one_alive_member():
            return
        for attacker in self.get_alive_members():
            defender = other_team.get_defender()
            if defender is None:
                break
            attacker.attack(defender)


# ========= Simulation =========
class Simulation:
    def __init__(self, team_a: Team, team_b: Team) -> None:
        self._teamA = team_a
        self._teamB = team_b

    def execute_round(self) -> None:
        # najpierw A w B, potem B w A
        self._teamA.attack(self._teamB)
        self._teamB.attack(self._teamA)

    def has_ended(self) -> bool:
        return not (
            self._teamA.is_at_least_one_alive_member() and
            self._teamB.is_at_least_one_alive_member()
        )

    def execute(self) -> None:
        while not self.has_ended():
            self.execute_round()

    def get_winner(self) -> Optional[Team]:
        a_alive = self._teamA.is_at_least_one_alive_member()
        b_alive = self._teamB.is_at_least_one_alive_member()
        if a_alive and not b_alive:
            return self._teamA
        if b_alive and not a_alive:
            return self._teamB
        return None
