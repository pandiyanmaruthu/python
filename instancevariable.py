class dept:
    mydept="cse"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
user1=dept("maruthu",1212)
user2=dept("pandiyan",2131)
print(user1.name)
print(user2.roll)
print(user1.mydept)
print(user2.mydept)
dept.mydept="ece"
print (user1.mydept)
print (user2.mydept)