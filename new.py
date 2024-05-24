from Roles import Chambermaid
from Roles import TestDemon
from Roles import TestMinion
from Roles import TestOutsider
from Roles import TestTownsfolk

Players = ["Dylan", "Josh Megagames", "Jo Castle", "Bottom Josh", "Evie", "Bilal", "Gwen", "School Shooter (Ronik)", "Dot", "Jess Fifield"]
num_players = len(Players)

num_townsfolk = 4
possible_townsfolk = [TestTownsfolk(), TestTownsfolk(), TestTownsfolk(), TestTownsfolk(), TestTownsfolk()]
townsfolk = []

num_outsiders = 1
possible_outsiders = [TestOutsider(), TestOutsider()]
outsiders = []

num_minions = 2
possible_minions = [TestMinion(), TestMinion()]
outsiders = []

num_demons = 1
possible_demons = [TestDemon(), TestDemon()]
demons = []

