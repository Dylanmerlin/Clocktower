from .Role import *

class TestDemon(Role):
  def __init__(self):
    super().__init__('Test Demon', 'Test', 'Evil', 'Demons')