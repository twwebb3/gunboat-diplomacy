

class Unit:
    def __init__(self, unit_type, location, owner):
        self.type = unit_type  # 'army' or 'fleet'
        self.location = location
        self.owner = owner