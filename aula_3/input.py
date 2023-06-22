# Utilizando o input para pegar um nome informado pelo usuário

nome = input("Nome: ");
# print(nome);
print();


# Insertindo as variáveis no print com f

frase = "Ola Mundo, "
# sobre_nome = "Ribeiro";
sobre_nome = input("Sobrenome: ");
print();
print(f"Bem vindo, {nome} {sobre_nome}");
print("Bem vindo, {} {}".format(nome, sobre_nome));
print();

# Concatenando strings

print("Concatenando strings: ");
outraFrase = "Bem vindo ";
fraseCompleta = frase + outraFrase;
print(fraseCompleta);
print();

# Tamanho da strings

tamanho = len(frase);
print("Tamanho; ", tamanho);
print();

# Divindo uma string em sub strings

print("Divindo a string");
palavra = fraseCompleta.split();
print(palavra);
print();


# Substituindo partes das strings

print("Substituindo partes das strings: ");
novaFrase = frase.replace("mundo", "Python");
print(novaFrase);
print();

# Convertendo para letras maiúsculoas e minúsculas

print("Convertendo para letras maiúsculoas e minúsculas; ");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());