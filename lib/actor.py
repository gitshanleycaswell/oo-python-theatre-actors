from .audition import Audition

class Actor:
    all =[]
    def __init__(self, name):
        self.name=name

    @property
    def auditions(self):
        actors_auditions = []
        for audition in Audition.all:
            if audition.actor == self:
                actors_auditions.append(audition)

        return actors_auditions
    
    @property
    def roles(self):
        actors_roles = []
        for audition in self.auditions:
            actors_roles.append(audition.role)
        return actors_roles
    
    @property
    def characters(self):
        actors_characters = []
        for audition in self.auditions:
            actors_characters.append(audition.role.character_name)
        return actors_characters
    
    @property
    def paychecks(self):
        actors_paychecks = []
        for audition in self.auditions:
            if audition.hired == True:
                actors_paychecks.append(audition.role.character_name)
        return actors_paychecks

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('Name must be of type str')