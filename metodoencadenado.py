class User:  # aqui está lo que tenemos hasta ahora
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_deposit(self, amount):  # toma un argumento que es el monto del depósito
        self.account_balance += amount  # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self
    # agrega el método deposit
    def make_withdrawal(self, amount):  # toma un argumento que es el monto del retiro
        self.account_balance -= amount  # la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self
    def display_user_balance(self):  # haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
        return f" El cliente {self.name} tiene un saldo de {self.account_balance}"

    def transfer_money (self, other_user, amount): # que tengo que hacer para transferir dinero?
        other_user.make_deposit(amount) #hacer un deposito a otro usuario
        self.make_withdrawal(amount) #de mi mismo hacer un giro para transferirlo
        self.display_user_balance() #una vez hecho el giro,ver mi saldo
        other_user.display_user_balance() #una vez hecha la transferencia,ver el saldo del otro usuario
        
user1 = User("Daisy", "daisyktbpa@gmail.com", 3000)  # haz que el user 1 tenga 3 depositos,1 retiro y luego,que muestre su saldo
user1.make_deposit(100).make_deposit(30).make_deposit(40).make_withdrawal(20).display_user_balance()
print(user1.display_user_balance())


user2 = User("Guido", "polili@gmail.com", 2000) # Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
user2.make_deposit(100).make_deposit(50).make_withdrawal(25).make_withdrawal(30).display_user_balance()
print(user2.display_user_balance())

user3 = User("Maria", "kik@gmail.com", 300) # Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
user3.make_deposit(2200).make_withdrawal(20).make_withdrawal(30).make_withdrawal(50).display_user_balance()
print(user3.display_user_balance())


    
    
    
    
    



