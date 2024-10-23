class User :
    def __init__(self,first_name,last_name,email,age) :
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_point=0
    def display_info(self):
        print(f"hello, my name is {self.first_name} and my last name is {self.last_name} i have {self.age} my email is {self.email} reward member is {self.is_rewards_member} and gold card point is {self.gold_card_point}")
    def enroll(self,user) :  
    
         
        self.is_rewards_member=True
        self.gold_card_point=200
        
    def spend_points(self,amout) :
        self.gold_card_point=self.gold_card_point - amout
        
        

        