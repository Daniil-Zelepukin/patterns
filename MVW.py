class User:
    def __init__(self, name):
        self.name = name

class UserViewModel:
    def __init__(self, user):
        self.user = user

    def update_user(self, new_name):
        self.user.name = new_name


class UserView:
    def __init__(self, view_model):
        self.view_model = view_model

    def display_user_details(self):
        print(f"User: {self.view_model.user.name}")

    def update_user_view(self, new_name):
        self.view_model.update_user(new_name)
        self.display_user_details()


if __name__ == "__main__":
    user = User("Daniil")
    view_model = UserViewModel(user)
    view = UserView(view_model)

    view.display_user_details()

    view.update_user_view("DA_NI_IL")