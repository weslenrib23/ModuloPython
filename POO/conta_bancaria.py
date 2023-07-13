class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero;
        self.titular = titular;
        self.saldo = saldo;

    def depositar(self, valor):
        self.saldo += valor;

    def depositar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
           print("Saldo insulficiente!");

    def exibir_informacoes(self):
        print(f"Conta: {self.numero}");
        print(f"Titular: {self.titular}"); 
        print(f"Saldo: {self.saldo}");

conta = Conta(123, "Wesley");

conta.depositar(1000);
conta.sacar(500);
conta.exibir_informacoes();