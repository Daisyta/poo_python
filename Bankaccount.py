listadeclientes = []
class Cuentabancaria:
    def __init__(self, nombre, apellido, email,int_rate = 0.01,balance_cuenta= 0):  # constructor
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.int_rate = int_rate
        self.registrarLog("objeto creado")
        self.balance_cuenta = balance_cuenta
        
    def getBalance(self):
        self.registrarLog("el usuario solicito un balance.")
        return f" SALDO: $ {self.balance_cuenta}"

    def hacer_deposito(self, monto):
        self.balance_cuenta += monto
        self.registrarLog(f"El usuario acaba de hacer un depósito de {monto} a {self.nombre} {self.apellido} quedando un saldo de : {self.getBalance()}")
        return self


    def hacer_giro(self, monto):
        if self.balance_cuenta < monto:
            print(f"NO TIENE SALDO SUFICIENTE- SALDO: {self.balance_cuenta} falta: { monto - self.balance_cuenta } ")
            return self
        self.balance_cuenta -= monto
        self.registrarLog(f"el usuario realizó un giro de {monto} a {self.nombre} {self.apellido} quedando un saldo de  : {self.getBalance()}")
        return self
    
    def registrarLog(self, mensaje):
        f = open("historialdemovimientos.txt","a",encoding="utf8")  #para guardar estos registros,se usa esto,a de append para que no borre el historial previo
        f.write(mensaje + "\n")
        f.close()
        return self

    def transferencia(self, usuario_destino, monto):
        if self.balance_cuenta < monto:
            print(f"NO TIENE SALDO SUFICIENTE {self.nombre}- SALDO: {self.balance_cuenta} falta: { monto - self.balance_cuenta } ")
            return self

        self.hacer_giro(monto)
        usuario_destino.hacer_deposito(monto)

        return self
    
    def saldoConInteres(self):
        if self.balance_cuenta > 0:
            self.totalInteres = (self.balance_cuenta * self.int_rate)
            self.totalCuenta = self.balance_cuenta + self.totalInteres
        else:
            print('No hay saldo disponible')
        return self

    def __str__(self): 
        self.registrarLog("El usuario imprimio el objeto usuario")
        return "Objeto Usuario:\t" + self.nombre + " " + self.apellido

usuario1 = Cuentabancaria("Daisy","Castillo", "pie@jaja.com")
print(usuario1)
usuario1.hacer_deposito(1000).hacer_deposito(22500).hacer_deposito(500).hacer_giro(5000).saldoConInteres()
print(usuario1.getBalance())

usuario2 = Cuentabancaria("Antonio", "Riquelme", "lolo@olo.com")
print(usuario2)
usuario2.hacer_deposito(12200).hacer_deposito(1000).hacer_giro(200).hacer_giro(400).hacer_giro(20).hacer_giro(100).saldoConInteres()
print(usuario2.getBalance())
