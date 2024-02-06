class Role:

    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        self.__class__.all.append(self)

    @property
    def character_name(self):
        return self._character_name

    @character_name.setter
    def character_name(self, value):
        if type(value) == str and len(value) > 0:
            self._character_name = value
        else:
            raise Exception("Invalid character name")

    def auditions(self):
        from lib.audition import Audition

        return [audition for audition in Audition.all if audition.role == self]

    def actors(self):
        return [audition.actor for audition in self.auditions()]

    def locations(self):
        return [audition.location for audition in self.auditions()]

    def lead(self):
        hired_auditions = [audition for audition in self.auditions() if audition.hired]
        if not hired_auditions:
            return "No actor has been hired for this role"
        else:
            return hired_auditions[0]

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions() if audition.hired]
        if len(hired_auditions) <= 1:
            return "No understudy has been hired for this role"
        else:
            return hired_auditions[1]

    @classmethod
    def not_cast(cls):
        return [
            role
            for role in cls.all
            if not any([audition.hired for audition in role.auditions()])
        ]

    def __repr__(self):
        return f"<Role {self.character_name}>"
