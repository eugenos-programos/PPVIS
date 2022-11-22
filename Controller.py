from Model import *
from Data import UserData
from View import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.user_data = UserData()
        self.user_manager = UserManager()
        self.test_manager = TestManager()

    def save(self, email):
        try:

            self.model.email = email
            self.model.save()

            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            self.view.show_error(error)

class UserManager():

    user_data : UserData
    teacher_ui : TeacherUI
    student_ui : StudentUI

    def __init__(self):
        pass

    def add_user(self, login : str, password : str, email : str):
        'called'
        pass

    def delete_user(self, user : User):
        pass

    def sign_in(self, login : str, password : str):
        "called"
        pass

    def sign_up(self, login : str, password : str, email : str):
        'called'
        self.add_user(login, password, email)
        pass

    def sign_out(self):
        'called'
        pass


class TestManager():
    def __init__(self):
        pass

    def create_test(self):
        pass

    def edit_test(test : Test):
        pass

    def delete_test(test : Test):
        pass
