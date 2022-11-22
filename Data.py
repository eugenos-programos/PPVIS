from Model import *

class UserData():

    students : list[Student]
    teachers : list[Teacher]

    def __init__(self):
        self.students = list()
        self.teachers = list()


class TestData():

    access : dict[User : list[Test]]
    tests : list[Test]

    def __init__(self) -> None:
        self.access = dict()
        self.tests = list()
        