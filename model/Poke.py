class Pokemon:
    def __init__(self, name, element, level, health, attack, defense, speed, weaknesses):
        self.name = name
        self.element = element
        self.level = level
        self.speed = speed
        
        self.health = health
        self.attack_power = attack
        self.defense = defense
        self.weaknesses = weaknesses
            
    def attack(self, target):
        if self.element in target.weaknesses:
            print(f"{target.name} is weak to {self.name}")
            damage = self.attack_power * 2 - target.defense
            
        else:
            damage = self.attack_power - target.defense
        
        target.health -= damage
        print(f"{self.name} dealt {damage} to {target.name} reducing their hp to: {target.health}")
        
        if target.health <= 0:
            print(f"{target.name} has feinted!")
              
