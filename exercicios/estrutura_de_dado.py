# 1 - Crie duas variáveis, nome e idade, e atribua a elas seus
# próprios valores. Em seguida, use a formatação de strings para
# imprimir a seguinte mensagem: "Olá, meu nome é [nome] e eu
# tenho [idade] anos."

nome = "Wesley";
idade = 36;
print();

# OU

nome = input("Seu nome: ");
idade = input("Seu idade: ");
print();

mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem);

# 2 - Crie uma variável chamada frase e atribua a ela uma string. Em
# seguida, use a função len() para imprimir o comprimento da frase.

frase = "Quanto mais fortes forem as suas provações, maiores serão suas vitórias.";
tamanho = len(frase);

print("Comprimento da frase: " ,tamanho);

# 3 - Crie duas variáveis, nome e sobrenome, e atribua a elas seus
# próprios valores. Concatene as variáveis para criar uma nova
# variável chamada nome_completo e imprima o resultado.

nome = "Wesley";
sobrenome = "Ribeiro";

nome_completo = nome + " " + sobrenome;

print(nome_completo);

# 4 - Crie uma variável chamada frase e atribua a ela uma string. Use
# o método upper() para imprimir a frase em letras maiúsculas.

frase = "Quanto mais fortes forem as suas provações, maiores serão suas vitórias.";

print(frase.upper());

# 5 - Crie uma variável chamada frase e atribua a ela uma string
# contendo uma frase completa. Use o método split() para dividir a
# frase em uma lista de palavras e imprima o resultado.

frase = "Quanto mais fortes forem as suas provações, maiores serão suas vitórias.";

divido_lista = frase.split();

print(divido_lista);

# 6 - Crie uma variável chamada frase e atribua a ela uma string. Use
# o método replace() para substituir uma palavra específica na
# frase por outra palavra de sua escolha. Imprima a frase
# modificada.

frase = "Quanto mais fortes forem as suas provações, maiores serão suas vitórias.";

modificada = frase.replace("fortes", "fraços");

print(modificada);

# 7 - Crie duas váriaveis, “numero1” e “numero2” e atribua valores
# númerico a elas, depois crie uma váriavel resultado e armazene o
# resultado da soma das váriaveis “numero1” e “numero2”. Ao final
# imprima o resultado.

numero1 = 5;
numero2 = 10;

resultado = numero1 + numero2;

print(resultado);

# 8 - Escreva um programa que solicite ao usuário que digite dois
# números inteiros e exiba a multiplicação desses números

numero1 = int(input("Digite o primeiro número inteiro: "));
numero2 = int(input("Digite o segundo número inteiro: "));
print();

resultado = numero1 * numero2

print("A multiplicação dos números é:", resultado);