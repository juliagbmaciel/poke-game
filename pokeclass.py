
class Pokemon:

    def __init__(self, name, speed, hp, attack):
        self.name = name
        self.speed = speed
        self.hp = hp
        self.attack = attack


class Grass(Pokemon):
    type = 'Grass'

    def __init__(self, name, speed, hp, attack, user='player'):
        super(Grass, self).__init__(name, speed, hp, attack)
        self.user = user

    @property
    def attacks(self):
        return self.attack


    def advantages(self, opponent_type):
        if opponent_type == 'Grass':
            return 'same'
        elif opponent_type == 'Water':
            return True
        elif opponent_type == 'Fire':
            return False


class Fire(Pokemon):
    type = 'Fire'

    def __init__(self, name, speed, hp, attack, user='player'):
        super(Fire, self).__init__(name, speed, hp, attack)
        self.user = user

    @property
    def attacks(self):
        return self.attack


    def advantages(self, opponent_type):
        if opponent_type == 'Grass':
            return True
        elif opponent_type == 'Water':
            return False
        elif opponent_type == 'Fire':
            return 'same'


class Water(Pokemon):
    type = 'Water'

    def __init__(self, name, speed, hp, attack, user='player'):
        super(Water, self).__init__(name, speed, hp, attack)
        self.user = user

    @property
    def attacks(self):
        return self.attack


    def advantages(self, opponent_type):
        if opponent_type == 'Grass':
            return False
        elif opponent_type == 'Water':
            return 'same'
        elif opponent_type == 'Fire':
            return True
