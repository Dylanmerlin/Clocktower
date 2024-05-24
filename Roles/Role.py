class Role:
  def __init__(self, name:str, ability:str, alignment:str, team:str, chance:str="Common", order:int=10):
    self.role_name = name
    self.role_ability = ability

    self.chance = chance #Common, Rare, Legendary, Guaranteed and Never
    self.order = order

    self.alignment = alignment #Good, Evil
    self.team = team #Townfolk, Outsiders, Minions, Demons

    self.img = None #Deal with this later