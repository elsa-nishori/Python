from pet import Pet

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def food(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self, sound):
        self.pet.noise(sound)
        return self

dog = Pet("Maxi", "Dog", "Roll Over")
ninja = Ninja("Elsa", "Nishori", "", "", dog).walk().food().bathe("Hau-hau")
print(f"{dog.name}'s health: {dog.health}, energy: {dog.energy}")


