# User class with its attributes and methods
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nReward Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points} ")
    
    def enroll(self):
        self.gold_card_points = 200
        if (self.is_rewards_member):
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            return True
    
    def spend_points(self, amount):
        if (self.gold_card_points > amount):
            self.gold_card_points -= amount

first_user = User("Ada", "Lovelace", "alovelace@codingdojo.com", 30)
second_user =  User("Anne", "Bill", "abill@codingdojo.com", 21)
third_user = User("Test", "Test", "test@gmail.com", 25)

first_user.enroll()
first_user.enroll()

first_user.spend_points(50)

second_user.enroll()
second_user.spend_points(80)

third_user.spend_points(40)

first_user.display_info()
second_user.display_info()
third_user.display_info()