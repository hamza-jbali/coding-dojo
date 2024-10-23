class User:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points
        self.is_member = False

    def display_info(self):
        print(f"User: {self.name}, Points: {self.points}, Member: {self.is_member}")
        return self  

    def enroll(self):
        if self.is_member:
            print("User already a member.")
        else:
            self.is_member = True
            print(f"{self.name} has been enrolled.")
        return self  

    def spend_points(self, amount):
        if self.points >= amount:
            self.points -= amount
            print(f"{self.name} spent {amount} points.")
        else:
            print(f"{self.name} does not have enough points to spend.")
        return self  
