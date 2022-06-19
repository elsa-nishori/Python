from pet import Pet

class Parrot(Pet):
    def __init__(self, name, type, tricks, talk, health=0, energy=0):
        super().__init__(name, type, tricks, health, energy)
        self.talk = talk

    def fly(self):
        print("Parrot's flying")
        self.health += 5
        return self

quaker = Parrot("Lui", "Quaker Parrots", "Imitate Humans", True)
quaker.fly()
print(f"{quaker.name}'s health: {quaker.health}")