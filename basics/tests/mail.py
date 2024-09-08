import re

def is_email_valid(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def email(self):
        return self.__email

    def get_mail(self):
        self.__email = input("Email: ")
        if is_email_valid(self.__email):
            print(self.__email)
        elif not is_email_valid(self.__email):
            print("Invalid email. Please try again.")

k = UserMail("BEBEBE", "hjhj@gmail.com")
k.get_mail()
