class User:
    def __init__(self, name):
        self.name = name


class UserProfile:
    def __init__(self, user, age):
        self.user = user
        self.age = age


class UserView:
    def display_user_details(self, user, user_profile):
        print(f"User: {user.name}, Age: {user_profile.age}")


class UserController:
    def __init__(self, user, user_profile, view):
        self.user = user
        self.user_profile = user_profile
        self.view = view

    def update_user_details(self, name, age):
        self.user.name = name
        self.user_profile.age = age
        self.view.display_user_details(self.user, self.user_profile)


if __name__ == "__main__":
    user = User("Daniil")
    user_profile = UserProfile(user, 18)
    view = UserView()
    controller = UserController(user, user_profile, view)

    controller.update_user_details("DANIIL", 20)