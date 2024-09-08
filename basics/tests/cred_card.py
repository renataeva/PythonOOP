class CreditCard:
    def __init__(self, number, name, pin, balance):
        self.__number = number
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def show_info(self):
        pin_input = int(input("Enter PIN: "))
        name_input = input("Enter name: ")
        if pin_input == self.__pin and name_input == self.name:
            print(f"Number: {self.__number}\nBalance: {self.__balance}")
        else:
            print("Wrong PIN or wrong name")

    def deposit(self):
        pin_input = int(input("Enter PIN: "))
        if pin_input == self.__pin:
            amount = int(input("Enter amount: "))
            self.__balance += amount
            print(f"New balance: {self.__balance}")
        else:
            print("Wrong PIN")

    def withdraw(self):
        pin_input = int(input("Enter PIN: "))
        if pin_input == self.__pin:
            amount = int(input("Enter amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"New balance: {self.__balance}")
            else:
                print("Not enough money")
        else:
            print("Wrong PIN")


card = CreditCard(123456789, "John", 1234, 1000)
card.show_info()
card.deposit()
card.withdraw()