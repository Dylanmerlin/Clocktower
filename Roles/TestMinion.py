from .Role import *

class TestMinion(Role):
  def __init__(self):
    super().__init__('Test Minion', 'Test', 'Evil', 'Minions')