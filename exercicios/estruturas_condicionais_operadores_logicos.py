# 1 - Escreva um programa que solicite ao usuário dois números
# inteiros e exiba a soma, subtração, multiplicação e divisão entre
# esses números.

numero1 = int(input("Digite o primeiro número inteiro: "));
numero2 = int(input("Digite o segundo número inteiro: "));

soma          = numero1 + numero2
subtracao     = numero1 - numero2
multiplicacao = numero1 * numero2
divisao       = numero1 / numero2

print("Soma:", soma);
print("Subtração:", subtracao);
print("Multiplicação:", multiplicacao);
print("Divisão:", divisao);
print();


# 2 - Escreva um programa que solicite ao usuário uma temperatura
# em graus Celsius e verifique se ela está acima do ponto de
# ebulição da água (100°C). Caso positivo, exiba a mensagem "A
# água está fervendo!".

temperaturaCelsius = float(input("Digite a temperatura em graus Celsius: "));

if temperaturaCelsius > 100:
    print("A água está fervendo!");
print();

# 3 - Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "));

if numero % 2 == 0:
    print("PAR");
else:
    print("ÍMPAR");
print();

# 4 - Escreva um programa que solicite uma senha ao usuário e
# verifique se a senha está correta. Considere a senha correta como
# "123456".

senha = input("Digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("Senha correta!");
else:
    print("Senha incorreta!");
print();

# 5 - Escreva um programa que solicite ao usuário uma idade e
# verifique se ela está entre 18 e 30 anos (inclusive).

idade = int(input("Digite a idade: "));

if idade >= 18 and idade <= 30:
    print("A idade está entre 18 e 30 anos.");
else:
    print("A idade não está entre 18 e 30 anos.");
print();

# 6 - Escreva um programa que solicite ao usuário três números
# inteiros e verifique se pelo menos um deles é positivo.

numero1 = int(input("Digite o primeiro número inteiro: "));
numero2 = int(input("Digite o segundo número inteiro: "));
numero3 = int(input("Digite o terceiro número inteiro: "));

if numero1 > 0 or numero2 > 0 or numero3 > 0:
    print("Pelo menos um dos números é positivo.");
else:
    print("Nenhum dos números é positivo.");
print();

# 7 - Escreva um programa que solicite ao usuário uma letra e
# verifique se ela é uma vogal (a, e, i, o, u).

letra = input("Digite uma letra: ");

# Converter a letra para minúscula (caso tenha sido digitada em maiúscula)
letra = letra.lower();

if letra in ['a', 'e', 'i', 'o', 'u']:
    print("A letra é uma vogal.");
else:
    print("A letra não é uma vogal.");
print();

# 8 - Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é positivo, negativo ou zero.

numero = int(input("Digite um número inteiro: "));

if numero > 0:
    print("O número é positivo.");
elif numero < 0:
    print("O número é negativo.");
else:
    print("O número é zero.");
print();

# 9 - Escreva um programa que solicite ao usuário três números e
# verifique se eles estão em ordem crescente.

numero1 = float(input("Digite o primeiro número: "));
numero2 = float(input("Digite o segundo número: "));
numero3 = float(input("Digite o terceiro número: "));

if numero1 < numero2 < numero3:
    print("Os números estão em ordem crescente.");
else:
    print("Os números não estão em ordem crescente.");
print();

# 10 - Escreva um programa que solicite ao usuário um número
# inteiro e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo.

numero = int(input("Digite um número inteiro: "));

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é um múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("O número não é um múltiplo de 3 e 5 ao mesmo tempo.");



