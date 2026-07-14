class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self): # getter
        return self.__balance

    @balance.setter
    def balance(self, value): # setter
        if value < 0:
            raise ValueError("No negatives")
        self.__balance = value

almaz = Account(1500)
print("almaz:", almaz.balance)  # Output: 1500