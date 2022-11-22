import re

class Model:
    def __init__(self):
        pass

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

class Question():
    mark : int
    Name : str
    answers : list[str]

    def __init__(self):
        pass

class Test():
    time_limit : int
    deadline : int
    test_id : str
    questions : list[Question]

    def __init__(self):
        pass
    
    def add_question():
        pass

    def edit_question(question : Question):
        pass

    def delete_question(question : Question):
        pass

class User():
    password : str
    login : str
    name : str

    def __init__(self):
        self.password = self.login = self.name = None
        pass

class Teacher(User):
    def __init__(self):
        super().__init__(Teacher)
        pass

    def create_test(self) -> Test:
        pass

    def edit_test(self, test : Test) -> Test:
        pass

    def delete_test(self, test : Test) -> Test:
        pass 

class Student(User):
    def __init__(self):
        pass

    def pass_test(test : Test):
        pass