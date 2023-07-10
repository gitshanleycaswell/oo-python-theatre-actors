from .audition import Audition

class Role:
    all=[]
    def __init__(self,character_name):
        self.character_name = character_name

    @property
    def auditions(self):
        role_auditions = []
        for audition in Audition.all:
            if audition.role == self:
                role_auditions.append(audition)

        return role_auditions
    
    @property
    def actors(self):
        roles_actors = []
        for audition in self.auditions:
            roles_actors.append(audition.actor.name)
        return roles_actors
    
    @property
    def locations(self):
        roles_locations = []
        for audition in self.auditions:
            roles_locations.append(audition.location)
        return roles_locations
    
    @classmethod
    def silver_screen(cls):
        hired_character_names = set(audition.role.character_name for audition in Audition.all if audition.hired)
        return list(hired_character_names)
        
    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, new_character_name):
        if isinstance(new_character_name, str):
            self._character_name = new_character_name
        else:
            print("Character Name must be of type str")
    