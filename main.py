class  User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Reiquel")
user_2 = User("002", "Melina")
user_3 = User("003", "Frederick")
user_4 = User("004", "Miguel")
user_5 = User("005", "Alba")
user_6 = User("006", "Carela")

user_1.follow(user_2)
user_1.follow(user_3)
user_1.follow(user_4)
user_1.follow(user_5)
user_2.follow(user_1)
user_2.follow(user_6)

print(f"Followers {user_1.followers}")
print(f"Following {user_1.following}")



#user_2 = User()
#user_2.id = "0002"
#user_2.username = "Melina"


