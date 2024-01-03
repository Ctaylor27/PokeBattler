from Util import data

class Battle:
    def __init__(self, pk1, pk2):
        self.pk1 = pk1
        self.pk2 = pk2
        if pk1.speed > pk2.speed:
            self.initiative = pk1
            self.deck = pk2
        else:
            self.initiative = pk2
            self.deck = pk1
            self.transfer = ""
        self.turn_counter = 0
        print(f"{pk1.name} and {pk2.name} have entered the battlefield!")
        
    def take_turn(self):
        self.return_string = self.initiative.attack(self.deck)
        self.transfer = self.initiative
        self.initiative = self.deck
        self.deck = self.transfer
        self.transfer = ""
        self.turn_counter += 1
        if self.initiative.health <= 0:
            data.battle_over_text = (f"Battle Over! {self.deck.name} has won the battle in {self.turn_counter} turns!")
            print("In battle func " + data.battle_over_text)
            data.winner = self.deck
            return (data.battle_over_text)
        return self.return_string
        
    def run_battle(self):
        gameover = False
        while not gameover:
            self.take_turn()
            if self.initiative.health <= 0:
                print(f"Battle Over! {self.deck.name} has won the battle in {self.turn_counter} turns!")
                gameover = True