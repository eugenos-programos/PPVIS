from tkinter import ttk
import tkinter as tk
from Model import Test
from time import sleep

def bind_textbox(frame, def_text, size=(1, 10)):
    textbox = tk.Text(frame, height=size[0], width=size[1])
    textbox.insert(tk.END, def_text)

    def default(event):
        current = textbox.get('1.0', tk.END)
        if current[:-1] == def_text:
            textbox.delete('1.0', tk.END)
        elif current == '\n':
            textbox.insert('1.0', def_text)

    textbox.bind("<FocusIn>", default)
    textbox.bind("<FocusOut>", default)

    return textbox

class View():
    def __init__(self, parent):
        self.parent = parent

        self.test_ui = TestUI(parent, self)

        self.frame = tk.Frame(parent)
        self.frame.grid(row=10, column=0, padx=80, pady=160)
        self.parent.title('Sign in')

        self.enter_as_a_teacher_button = ttk.Button(self.frame, text='Enter as a teacher', command=self.enter_as_a_teacher)
        self.enter_as_a_student_button = ttk.Button(self.frame, text='Enter as a student', command=self.enter_as_a_student)

        self.enter_as_a_teacher_button.grid(row=1, column=0, padx=10, pady=10)
        self.enter_as_a_student_button.grid(row=4, column=0, padx=10, pady=10)

    def enter_as_a_teacher(self):
        self.frame.destroy()
        self.user_ui = TeacherUI(self.parent, self)
        self.user_ui.sign_in()

    def enter_as_a_student(self):
        self.frame.destroy()
        self.user_ui = StudentUI(self.parent, self)
        self.user_ui.sign_in()

    def set_controller(self, controller):
        self.controller = controller


class UserUI():
    def __init__(self, parent, view):

        self.frame = tk.Frame(parent)
        self.view = view
        self.parent = parent

        self.frame.grid(row=10, column=0, padx=80, pady=160)
        self.parent.title('Sign in')

    def clean_up_frame(self):
        for widg in self.frame.winfo_children():
            widg.destroy()

    def sign_in(self):
        login_entry = bind_textbox(self.frame, 'Type login...', (2, 15))
        self.login = login_entry.get('1.0', tk.END)
        login_entry.grid(row=1, column=1, sticky=tk.NSEW)

        password_entry = bind_textbox(self.frame, 'Type password...', (2, 20))
        password_entry.grid(row=2, column=1, sticky=tk.NSEW)
        self.password = password_entry.get('1.0', tk.END)

        self.sign_in_button = ttk.Button(self.frame, text='Sign in', command=self.profile)
        self.sign_in_button.grid(row=3, column=1, padx=10, pady=10)

        self.sign_up_button = ttk.Button(self.frame, text='Sign up', command=self.sign_up)
        self.sign_up_button.grid(row=4, column=1, padx=10, pady=10)


    def sign_up(self):
        self.parent.title('Sign up')
        self.clean_up_frame()

        login_entry = bind_textbox(self.frame, 'Type new login...', (2, 15))
        login_entry.grid(row=1, column=1, sticky=tk.NSEW)

        password_entry = bind_textbox(self.frame, 'Type new password...', (2, 20))
        password_entry.grid(row=2, column=1, sticky=tk.NSEW)

        email_entry = bind_textbox(self.frame, 'Type your email...', (2, 20))
        email_entry.grid(row=3, column=1, sticky=tk.NSEW)

        login = login_entry.get('1.0', tk.END)
        password = password_entry.get('1.0', tk.END)
        email = email_entry.get('1.0', tk.END)
        
        self.create_acc_button = ttk.Button(self.frame, text='Create account',\
                                             command=self.sign_out)
        self.create_acc_button.grid(row=4, column=1, padx=10, pady=10)

    def sign_out(self):
        self.parent.title('Sign out')
        self.view.controller.user_manager.sign_out()
        self.clean_up_frame()
        ttk.Label(self.frame, text='Account was created').pack()

    def profile(self):
        pass

class TeacherUI(UserUI):
    def __init__(self, parent, view):
        super().__init__(parent, view)

    def profile(self):
        self.clean_up_frame()

        login = self.view.user_ui.login
        password = self.view.user_ui.password

        self.view.controller.user_manager.sign_in(login, password)
        self.parent.title('Teacher profile')

        view_tests_button = tk.Button(self.frame, text='View tests', command=self.view_tests)
        create_test_button = tk.Button(self.frame, text='Create test', command=self.create_test)
        exit_button = tk.Button(self.frame, text='Exit', command=exit)

        view_tests_button.grid(row=1, column=1, padx=10, pady=10)
        create_test_button.grid(row=2, column=1, padx=10, pady=10)
        exit_button.grid(row=3, column=1, padx=10, pady=10)

    def view_student(self):
        self.clean_up_frame()
        self.view.controller.user_data

    def create_test(self):
        self.clean_up_frame()
        self.parent.title('Test creation')
        self.view.test_ui.create_test()

    def view_tests(self):
        self.clean_up_frame()

        self.label_test = ttk.Label(self.frame, text='All tests')
        self.label_test.grid(row=1, column=2)

        for i in range(3, 6):
            test_button = tk.Button(self.frame, text=f'Test {i - 2}', command=None)
            del_button = tk.Button(self.frame, text=f'Del', command=self.delete_test)
            edit_button = tk.Button(self.frame, text=f'Edit', command=self.edit_test)

            test_button.grid(row=i, column=1)
            del_button.grid(row=i, column=2)
            edit_button.grid(row=i, column=3)

    def edit_test(self):
        self.view.test_ui.edit_test()

    def delete_test(self):
        self.view.test_ui.delete_test()

class StudentUI(UserUI):
    def __init__(self, parent, view):
        super().__init__(parent, view)

    def profile(self):
        self.clean_up_frame()

        login = self.view.user_ui.login
        password = self.view.user_ui.password

        self.parent.title('Student profile')
        self.view.controller.user_manager.sign_in(login, password)

        view_tests_button = tk.Button(self.frame, text='View tests', command=self.view_tests)
        exit_button = tk.Button(self.frame, text='Exit', command=self.sign_out)

        view_tests_button.grid(row=1, column=1, padx=10, pady=10)
        exit_button.grid(row=3, column=1, padx=10, pady=10)

    def view_tests(self):
        self.clean_up_frame()

        self.label_test = ttk.Label(self.frame, text='All tests')
        self.label_test.grid(row=1, column=1)

        for i in range(3, 5):
            test_button = tk.Button(self.frame, text=f'Test {i - 2}', command=self.view.test_ui.pass_test)
            test_button.grid(row=i, column=1)

    def pass_test(self, test : Test):
        pass

class TestUI(ttk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent)
        self.view = view
        self.parent = parent

    def clean_up_frame(self):
        for widg in self.frame.winfo_children():
            widg.destroy()

    def create_test(self):
        self.frame = self.view.user_ui.frame

        text_name_entry = bind_textbox(self.frame, 'Text name...', (2, 20))
        question_n_entry = bind_textbox(self.frame, 'Question count...', (1, 20))
        time_entry = bind_textbox(self.frame, 'Time...')

        text_name_entry.grid(row=1, column=1)
        question_n_entry.grid(row=2, column=1)
        time_entry.grid(row=3, column=1)

        contin_button = tk.Button(self.frame, text='Continue', command=self.edit_test)
        contin_button.grid(row=4, column=1, padx=10, pady=10)

    def edit_test(self):
        self.frame = self.view.user_ui.frame
        self.clean_up_frame()

        text_number_entry = bind_textbox(self.frame, 'Question number...', (1, 20))
        question_entry = bind_textbox(self.frame, 'Question...', (3, 25))

        text_number_entry.grid(row=1, column=1)
        question_entry.grid(row=1, column=2)

        for i in range(3, 7):
            tk.Checkbutton(self.frame, text='').grid(row=i, column=1)
            answer = bind_textbox(self.frame, f'{i - 2} answer...', (2, 15))
            answer.grid(row=i, column=2)

        contin_button = tk.Button(self.frame, text='Continue', command=self.exit_test)
        contin_button.grid(row=8, column=1, padx=10, pady=10)

    def delete_test(self):
        self.frame = self.view.user_ui.frame
        self.clean_up_frame()
        ttk.Label(self.frame, text='Test was deleted.').pack()

    def pass_test(self):
        self.view.user_ui.clean_up_frame()
        self.frame = self.view.user_ui.frame


        question = tk.Label(self.frame, text='Question 1 : \n ..........')
        question.grid(row=1, column=1)

        for i in range(3, 7):
            tk.Checkbutton(self.frame, text='<Answer .... >').grid(row=i, column=1)

        contin_button = tk.Button(self.frame, text='Continue', command=self.mark_test)
        contin_button.grid(row=8, column=1, padx=10, pady=10)

    def exit_test(self):
        self.clean_up_frame()
        ttk.Label(self.frame, text='Test ended').pack()

    def start_test(self):
        pass

    def mark_test(self):
        self.clean_up_frame()
        ttk.Label(self.frame, text='Test ended. Your mark - 10)))').pack()
