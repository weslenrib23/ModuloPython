# Estruturas Condicionais Operadores Logicos 

# ---------------------------

# Verificação de idade para entrada em clube noturno

idade = int(input("Digite sua idade: "));

if idade >= 18:
    print("Bem-vindo(a), você pode entrar na festa!");
else:
    print("Desculpa, você não tem idade suficiente para entrar na festa.");

# Verificar se um número está dentro de um interavlo entre 10 e 20.

numero = 15;

if (numero >= 10) and (numero <= 20):
    print("O número está dentro do intervalo.");
else:
    print("O número está fora do intervalo.");

# Comparar o tamnaho de duas listas

lista1 = [1,2,3,4,5];
lista2 = [1,2,3];

if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista 2.");
elif len(lista2) > len(lista1):
    print("A lista 2 é maior que a lista 1.");
else:
    print("As listas tem o mesmo tamanho.");

# Verificação de acesso um sistema

senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Usuário logado com sucesso.");
else:
    print("A senha informada está errada!");

# Verificação de acesso um sistema com login e senha

usuario = input("Digite o seu usuário: ");
senha = input("Digite sua senha: ");

usuarioCorreto = "admin";
senhaCorreta = "admin";

if (usuario == usuarioCorreto) and (senha == senhaCorreta):
    print("Login bem-sucedido");
else:
    print("Usuário ou senha incorreto!");

# Ou

if(usuario != usuarioCorreto and senha != senhaCorreta):
  print("Usuário e senha incorretos!");
elif usuario != usuarioCorreto:
  print("O usuário está incorreto!");
elif not (senha == senhaCorreta):
  print("A senha está incorreta!"); 
else: 
  print("Login bem-sucedido");

# Verificação de múltiplas condições com "and" ou "or"

numero = 10;

if (numero > 0 and numero < 5) or (numero > 10 and numero < 15):
    print("O número atende aos critérios");
else:
    print("O número não atende aos critérios");

# Verificação de uma condição negada
# Verificar se uma pessoa está apta a dirigir

idade = int(input("Informe sua idade; "));
possuiCarteira = False;

if idade >= 18 and not possuiCarteira:
  print("Você precisa de ter a carteira de motorista!");
else:
  print("Você está apto a dirigir");

# Match Case

camando = 'Olá, Mundo!'

match camando:
    case 'Olá, Mundo!':
        print("Olá para você também");
    case 'Adeus, Mundo':
        print("Adeus!");
    case _:
        print("Sem resultados!");