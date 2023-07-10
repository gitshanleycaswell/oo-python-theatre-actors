

class Audition:
    all =[]
    def __init__(self, location, hired, role, actor):
        self.location = location
        self.hired = hired
        self.role = role
        self.actor = actor
        Audition.all.append(self)

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, new_role):
        from lib.role import Role
        if isinstance(new_role, Role):
            self._role = new_role
        else:
            print('not a valid role')

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, new_actor):
        from lib.actor import Actor
        if isinstance(new_actor, Actor):
            self._actor = new_actor
        else:
            print('not a valid actor')

    def call_back(self):
        if self.hired is False:
            self.hired = True


    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self._location = new_location
        else:
            print("Location must be of type String")

    @property
    def hired(self):
        return self._hired
    
    @hired.setter
    def hired(self, is_hired):
        if isinstance(is_hired, bool):
            self._hired = is_hired
        else:
            print('Hired must be of type Boolean')