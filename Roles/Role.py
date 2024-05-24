class Role:
  def __init__(self, name:str, ability:str, alignment:str, team:str, chance:str="Common", order:int=10):
    self.role_name = name
    self.role_ability = ability

    self.chance = chance #Common, Rare, Legendary, Guaranteed and Never

    self.alignment = alignment #Good, Evil
    self.team = team #Townfolk, Outsiders, Minions, Demons

    self.img = None #Deal with this later
    self.Player = None #Deal with this later

  def check_allowed(Game):
    #Check there are enough slots on the team
    #Maybe seperate into a generic one (for each Team) and a specific one for each minion
    return True
  
  def add_to_game(Game):
    pass
    # See check_allowed - add one to the relevant team and then any specific abilities