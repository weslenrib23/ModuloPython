# É semelhante a um dicionário no mundo real,
# onde você pode procurar uma palavra (chave)
# e encontrar o seu significado (valor)
# associado.  ---- 'chave' : 'valor' ----

meuDicionario = {
    'nome'     : 'Wesley', 
    'sobrenome': 'Ribeiro',
    'anos'     : 37
    };

print(meuDicionario);

frutaDicionario = { 
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
};

print("Significado encontrado no dicionário : ", frutaDicionario["maçã"]);
print();

frutaDicionario["maçã"] = 5;
frutaDicionario["laranja"] = 10;

print("Nova quantidade de maçã: ", frutaDicionario["maçã"]);
print();
print(frutaDicionario);

print(frutaDicionario);
print();

animaisDicionario = {};
animaisDicionario["cachorro"] = "Melissa";
print(animaisDicionario);
print();

aluno = {
    'nome'     : 'Wesley', 
    'anos'     : 37 ,
    'hobbies'  : ['jogar', 'esportes']
    };

print(aluno);
print();

frutaDicionario = { 
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'laranja' : 10 
};

print();
print("Quantidade de maçãs: ", frutaDicionario.get("maçã"));
print("Quantidade de bananas: ", frutaDicionario.get("banana"));

print("Quantidade de morangos: ", frutaDicionario.get("morangos", "Não foi encontrado a definição de morango"));
print();

elementoRemovido = frutaDicionario.pop("laranja");

print(elementoRemovido);
print();
print("Dicionário atualizado: ", frutaDicionario);

frutaDicionario = {
  'maçã'      : 3,
  'banana'    : 6,
  'uva'       : 8,
  'laranja'   : 10
};

print();
print("Chaves encontradas no dicionário: ",frutaDicionario.keys());
print("Valores encontrados no dicionário: ", frutaDicionario.values());
print(frutaDicionario.items());