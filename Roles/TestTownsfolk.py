from .Role import *

class TestTownsfolk(Role):
  def __init__(self):
    super().__init__('Test Townsfolk', 'Test', 'Good', 'Townsfolk')