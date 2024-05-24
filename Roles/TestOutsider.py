from .Role import *

class TestOutsider(Role):
  def __init__(self):
    super().__init__('Test Outsider', 'Test', 'Good', 'Outsiders')