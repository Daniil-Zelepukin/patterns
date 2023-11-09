class User:
    def __init__(self, name):
        self.__name = name  
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


class UserView:
    def display_user_details(self, user):
        print(f"User: {user.get_name()}")


class UserPresenter:
    def __init__(self, user, view):
        self.user = user
        self.view = view

    def update_user_name(self, new_name):
        self.user.set_name(new_name)
        self.view.display_user_details(self.user)


if __name__ == "__main__":
    user = User("Daniil")
    view = UserView()
    presenter = UserPresenter(user, view)

    presenter.update_user_name("DANIIL")