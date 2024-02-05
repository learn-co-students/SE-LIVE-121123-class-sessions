class Audition:

    all = []  ## SSOT

    def __init__(self, role, actor, location, phone):
        self.role = role  # TODO: check if is Role instance
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = False
        self.__class__.all.append(self)

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        if isinstance(value, str) and 3 <= len(value) <= 20:
            self._actor = value
        else:
            raise Exception("Invalid actor")

    def call_back(self):
        self.hired = True
