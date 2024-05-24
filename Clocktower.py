import random

class Clocktower:
    def __init__(self, player_names:list, Script, start_num_townsfolk:int, start_num_outsiders:int, start_num_demons:int, start_num_minions:int):
        
        self.Script = Script

        self.player_names = player_names
        self.num_players = len(player_names)
        self.unassigned_players = random.shuffle(player_names.copy()) #Shuffle List

        self.Possible_Roles = Script.Townsfolk.copy() + Script.Outsiders.copy() + Script.Minions.copy() + Script.Demons.copy()
        self.Possible_Roles = random.shuffle(self.Possible_Roles) #Shuffle List
        self.Roles = []

        self.num_townsfolk = start_num_townsfolk
        self.num_outsiders = start_num_outsiders
        self.num_minions = start_num_minions
        self.num_demons = start_num_demons

    def assign_players(self):
        for player in self.unassigned_players:
            self.unassigned_players.remove(player)
            Role = self.get_valid_role()
            if not Role:
                return False
            self.set_role(Role, player)
        return True

    def set_role(self, Role, player):
        Role.set_player(player)
        Role.add_to_game(self)

    def get_bluffs(self):
        for i in range(3):
            self.get_random_townsfolk_or_outsider() #Add to list for bluffs

    def get_random_townsfolk_or_outsider(self):
        for Role in self.Possible_Roles:
            if Role.Team == 'Townsfolk' or Role.Team == 'Outsider':
                self.Possible_Roles.remove(Role) # Remove it from the possible roles pool
                return Role #Return role
        return False

    def get_random_townsfolk(self):
        for Role in self.Possible_Roles:
            if Role.Team == 'Townsfolk':
                self.Possible_Roles.remove(Role) # Remove it from the possible roles pool
                return Role #Return role
        return False
                
    def get_valid_role(self):
        for Role in self.Possible_Roles:
            if Role.check_allowed(self):
                self.Possible_Roles.remove(Role) # Remove it from the possible roles pool
                return Role #Return role      
        return False