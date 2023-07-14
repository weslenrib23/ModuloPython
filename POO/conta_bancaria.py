class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero;
        self.titular = titular;
        self.saldo = saldo;

    def depositar(self, valor):
        self.saldo += valor;

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor;
        else:
           print("Saldo insuficiente!");

    def exibir_informacoes(self):
        print(f"Conta: {self.numero}");
        print(f"Titular: {self.titular}"); 
        # print(f"Saldo: {self.saldo:,.2f}");
        valorReal = f'R${self.saldo:_.2f}';
        valorReal = valorReal.replace('.',',').replace('_','.');

        print(f"Saldo: {valorReal}")

conta = Conta(123, "Wesley");
conta.depositar(1000);
conta.sacar(500);
conta.exibir_informacoes();

contaZoio = Conta(321, "Zoio");
contaZoio.depositar(1500);
contaZoio.sacar(350);
contaZoio.exibir_informacoes();