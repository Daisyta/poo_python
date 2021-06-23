class User:
#Actualiza el metodo __init__ de la clase User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.08, balance=0)
    def make_deposit(self, amount):
#Actualiza el metodo make_deposit de la clase User
        self.account.deposit(amount)
        return self
    def make_withrawal (self, amount):
#Actualiza el metodo make_deposit de la clase User
        self.account.withdraw(amount)
        return self
    def display_user_balance (self):
#Actualiza el metodo make_deposit de la clase User
        print(f"usuario: {self.name}, saldo:  {self.account.display_account_info()}")
        return self
    # def transfer_money (self, other_user, amount):
    #     self.account.balance -= amount
    #      other_user.account.balance += amount


class BankAccount:
    def __init__(self, int_rate=0.08, balance=0):
    #def display_user_balance (self):
    #print(f"usuario: {self.name}, saldo: {self.account_balance}")// no dejar print en constructor
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
    #Agrega un método de depósito a la clase BankAccount
        self.balance += amount
        return self
    def withdraw(self, amount):
    #Agrega un método de retiro a la clase BankAccount
        if amount > self.balance:
            print(f"Fondos insuficientes: cobrar una tarifa de ${amount - self.balance}")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
    #Agrega un método display_account_info a la clase BankAccount
        return self.balance
    def yield_interest(self):
    # Agrega un método yield_interest a la clase BankAccount
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


usuario1 = User("guido", "guido@python.org")

usuario1.make_deposit(200).make_deposit(500).make_deposit(100)
usuario1.make_withrawal(300)
usuario1.display_user_balance()