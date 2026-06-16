class User():
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.followers_info = []
        self.following_info = []

    def follow(self, user):
        user.followers += 1
        self.following += 1
        self.following_info.append(user.username)


class Car():
    def __init__(self):
        self.seats = 5

    def enter_race_mode(self):
        self.seat = 2

user1 = User("001", "Rai")
user2 = User("002", "Melody")

user1.follow(user2)

print(f"{user1.username} has {user1.followers} followers on Mate.io")
print(f"{user1.username} has {user1.following} following on Mate.io")
print(f"{user1.username} is following {user1.following_info} on Mate.io")